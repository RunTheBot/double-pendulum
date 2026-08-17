# Journal
Starting after June 19th as physical build was extramly incovinient to lapse

## June 21 
Hours: 2

Switched Hex shaft in CAD to a bored out hex shaft

<img width="637" height="604" alt="image" src="https://github.com/user-attachments/assets/2a9cd31d-1357-4252-bca0-9dfdf1ac5349" />

## June 28th

Hours: 1
Ordered all parts from vendors

## July 4th

Hours: 1
Played with neo vortex over USB, Kinda dagourous holding it in my hand, wont do that again.
Did some research on controlling it over usb and decided that latency was too much, can was my only option.

## July 6th

Hours: 10

All part arrived, build begins. Attached MGN12H Rail to 2020 extrution. 

Learnt how to opperated the Omio X6, as I was not familiar with Mach3 and only have ever done light machining on a old machine hooked up with gSender (see: https://github.com/RunTheBot/AstralCNC)

Mach3 is a big peice of garbage and I hate it with a burning passion

## July: 7th
Hours: 8

Made the stand for the project, comprised of a couple peices of 2020

Bored out a 3in peice of hex shaft. Ts took 3 tries, way harder than anticipated. 

1. Cut the length wrong (Whops!)
2. the holes were no concentric on both sides so it ended up not working
3. Finally good, I expanded it small steps to that they'd stay concentric.

## July 8th
Hours: 10

### Electronics/Wiring
I swapped to the rev through bore cuz the amt was pissing me off due to bad design and the need for exact alignment. Luckily the holes just work.

I got decived by the SPI mode for like 2 hours. I switch to the correct ABI mode and it worked. 

I then encotered issues with PWM abs input. I "solved" it with a PIO program (this will come back later) instead of using interupts and it worked

### Assembly

Lots of assembly done, carrage was made

## July 9th 

Hours: 4

Chud day. Worked on amt alignment for second stage, quite fast, went through 4 iteration, testing and calculating spacing ending up making the tool below
did the wireing for the amt

<img width="437" height="357" alt="image" src="https://github.com/user-attachments/assets/99ad5ea1-1dc9-4370-a945-d7518fdd10cf" />

## July 10th
Hours: 8

Both encoders working all wireing done except for CAN. Remade the amt mount cuz I lwk forgot wire holes and bearing sizes were wrong. reprinted the mount and did a lot of modifacations after cuz im bad at design and there was even more intersecting geometry.

## July 11th

Hours: 6

I bashed my head at the CAN adapter for 6 hours, turns out... it was the adapter NOT ME!!!!! wtf the clock was 8mHz so it can't do 1mbps CAN to spec. Now I need to order a new one.

## July 12th 

Hours: 7

Read the CAN spec for like forever
Bashed my head with the new controller for more hours, I got the motor to enable, but it was jumoy (This was because of a dumb mistake)


## July 13th
Hours: 10

New day new me! Turns out the jumpy was me forgetting to send a usb lock so my laptop was sening stop signals. 

I then worked on reading the encoder, bashed my hear for another 3 ish hours before seeing that the spec I was reading was old and outdated, so I read the new version.

it simply wokred by reading a different frame.

### Lock in time

implimented a dashboard (Vibecoded) with a bunch of safty and then started implimenting LQR. 

I quickly gave up on LQR and swithced to a double PID controller. 

Kinda worked but not too well, so I removed the second stage and it just worked far better.

and thats a wrap!

## July 24th
Hours: 1h

Journaling...

## Aug 10th to 12
Hours: 4
Very slow CADing of a redesign. Using a stepper motor now soo yay.
<img width="889" height="890" alt="image" src="https://github.com/user-attachments/assets/0e0084c7-19bf-4b58-b872-98def38fdf63" />

## Aug 13th

Hours: 1
3D printing...


## Aug 14th
Hours: 4h
Started on rewiring, Using a SKR Pico for a stepper this time. passing encoder through a RP2350 since its a 5v sensor.
<img width="2480" height="3307" alt="image" src="https://github.com/user-attachments/assets/cc54e00a-602b-4202-8dbe-26373b488637" />

Im using a SKR pico now sooooo... I first feed the 5V encoder signal through a Pico 2 to translate it to 3.3v

## Aug 15
Hours: 4h
Programming... Got motor and encoder working. Motor was way to slow to be observalble so I thougt it wasnt working for an hour 😭

## Aug 16 
Hours: 4h
Programming... AND TUNING!!!! and testing. No challange here really, smooth sailing

[<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/d9969e3a-fe50-4f8b-a0c2-fca6e6d424be" />
](https://www.youtube.com/watch?v=KhN0Yt5W-70)
