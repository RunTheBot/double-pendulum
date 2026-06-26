# Double Inverted Pendulum
Controls project, showing off inverting a double pendulum. Uses a motor belt drive on a MGN12 Rail. Software uses the USB to CAN function of the Spark Max to do current control from a LQR controller. 

## But why?

I have recently graduated highschool and finished with FRC, now being a alum, and I wanted to put the things I learnt to use. The pendulum tests my knowledge in design, physics, math, and control theory. It also allows me to explore a LQR, a controller I have not used before while staying with a relitivly simple design.

## Instructions

### Hardware
The cart is the only really strict part. Make sure wires are routed nicely. Second stage encoder wires should go through the middle of the first stage shatft.

The main rail may be made of multiple section of rail, given that they get joined properly. 

### Software

Have UV set up with a python interpreter [Here](https://docs.astral.sh/uv/getting-started/installation/)

1. Run `uv sync`
2. Run `uv run LQR_Gains.py`

<img width="2478" height="3504" alt="Assembly 2" src="https://github.com/user-attachments/assets/f7db4e86-a321-4156-8523-1838f20c18d3" />

## Links 
[BOM](https://docs.google.com/spreadsheets/d/1-U5WBOVTvKiIzWNRjWvPPcvkB_1N992BvFvAFU30PCg/edit?usp=drivesdk)
[CAD](https://cad.onshape.com/documents/92e4efa3a70eb3967f83ba85/w/20c97743881ff1b44bc084d7/e/63d9b33b154e04c3994da71a) 
[Simulator/Software](https://github.com/RunTheBot/double-inverted-pendulum-sim)
