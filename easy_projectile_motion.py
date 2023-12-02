from vpython import *

# Web VPython 3.2


scene.caption = """
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
"""


def main():
    g = 9.8
    dt = 0.01

    y = float(input("Enter your y0: "))
    x = float(input("Enter your x0: "))
    z = float(input("Enter your z0: "))
    vy = float(input("Enter your Vy: "))
    vx = float(input("Enter your Vx: "))
    vz = float(input("Enter your Vz: "))
    t = 0
    ball = sphere(pos=vector(x, y, z), radius=10, color=color.blue, make_trail=True,
                  trail_type='points', interval=10, retain=500)

    running = True
    while True:
        rate(100)
        if running:
            ay = -g  # ay at beginning of interval
            y += vy * dt  # use old vy to calculate new y
            vy += ay * dt  # use old ay to calculate new vy
            x += vx * dt
            z += vz * dt
            ball.pos = vector(x, y, z)
            t += dt
            if y < 0:
                running = False
                print(x, y, z)
                scene.append_to_caption(f"{x} {y} {z}")


if __name__ == "__main__":
    main()
