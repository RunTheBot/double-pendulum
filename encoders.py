import array
import board
import time
import rp2pio
import adafruit_pioasm
import rotaryio

# Corrected PIO Assembly
# 1. Added commas between destination and source (e.g., mov y, ~ null)
# 2. Added spaces around the '~' operator as per your note
# 3. Used lowercase for registers (cleaner for the parser)
pwm_in_asm = """
.program PwmIn
.wrap_target
start:
    mov y, ~ null       ; start with the value 0xFFFFFFFF
    mov x, ~ null       ; start with the value 0xFFFFFFFF
    wait 0 pin 0        ; wait for a 0
    wait 1 pin 0        ; wait for a 1 (rising edge)
timer_hp:               ; loop for high period
    jmp y-- test        ; count down for pulse width
    jmp start           ; timer reached 0, restart
test:
    jmp pin timer_hp    ; if pin is still 1, continue counting
timer_lp:               ; loop for low period
    jmp pin timerstop   ; if pin is 1, period over
    jmp x-- timer_lp    ; if pin is 0, count down
    jmp start           ; timer reached 0, restart
timerstop:
    mov isr, ~ y        ; move (0xFFFFFFFF - y) to ISR
    push noblock        ; push high period cycles
    mov isr, ~ x        ; move (0xFFFFFFFF - x) to ISR
    push noblock        ; push low period cycles
.wrap
"""

compiled_asm = adafruit_pioasm.assemble(pwm_in_asm)
enc = rotaryio.IncrementalEncoder(board.GP6, board.GP7)

INPUT_PIN = board.GP19
PIO_FREQ = 125_000_000 

sm = rp2pio.StateMachine(
    compiled_asm,
    frequency=PIO_FREQ,
    first_in_pin=INPUT_PIN, # Sets the base for 'wait pin 0'
    jmp_pin=INPUT_PIN,      # Sets the pin for 'jmp pin'
    in_pin_count=1,         # Explicitly tell PIO we are using 1 input pin
)

buffer = array.array("I", [0, 0])

print("Reading PWM with PIO...")

while True:
    if sm.in_waiting >= 2:
        sm.readinto(buffer)
        
        # Each loop cycle (timer_hp/timer_lp) takes 2 instructions
        # Instruction 1: jmp y-- / jmp x--
        # Instruction 2: jmp pin / jmp pin
        high_cycles = buffer[0]
        low_cycles = buffer[1]
        
        # Convert cycles to microseconds
        # (cycles * 2 instructions per loop) / (clock freq / 1,000,000)
        high_time_us = (high_cycles * 2) / (PIO_FREQ / 1_000_000)
        low_time_us = (low_cycles * 2) / (PIO_FREQ / 1_000_000)
        
        total_period_us = high_time_us + low_time_us
        
        if total_period_us > 0:
            frequency = 1_000_000 / total_period_us
            duty_cycle = (high_time_us / total_period_us) * 100
            print(f"Freq: {frequency:.1f} Hz | Angle: {abs(100-duty_cycle)/100*360:.1f} | High: {high_time_us:.2f} us | Secondary encoder angle: {-enc.position/2048*360:.1f}")
            
    time.sleep(0.1)
