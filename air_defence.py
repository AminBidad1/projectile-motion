from vpython import *
import math

# Web VPython 3.2


scene.caption = """
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
"""


def equal_approximation(val1, val2):
    if (val2 - val1)/val1 <= 0.01:
        return True
    return False


def main():
    g = 10
    dt = 0.01
    ey = float(input("Enter your enemy Y0: "))
    ex = float(input("Enter your enemy X0: "))
    ez = float(input("Enter your enemy Z0: "))
    evy = float(input("Enter your enemy Vy: "))
    evx = float(input("Enter your enemy Vx: "))
    evz = float(input("Enter your enemy Vz: "))
    y = float(input("Enter your Y0: "))
    x = float(input("Enter your X0: "))
    z = float(input("Enter your Z0: "))
    vy = float(input("Enter your Vy: "))
    vx = float(input("Enter your Vx: "))
    vz = float(input("Enter your Vz: "))
    t = 0
    ball = sphere(pos=vector(x, y, z), radius=10, color=color.blue, make_trail=True,
                  trail_type='points', interval=10, retain=500)
    enemy = sphere(pos=vector(ex, ey, ez), radius=10, color=color.red, make_trail=True,
                   trail_type='points', interval=10, retain=500)
    running = True

    final_time = ex/(vx - evx)
    if equal_approximation(final_time, ez/(vz - evz)):
        delta = (evy - vy)**2 - 2*g*ey
        if delta >= 0:
            t1 = (vy - evy + math.sqrt(delta))/g
            t2 = (vy - evy - math.sqrt(delta))/g
            if equal_approximation(final_time, t1) or equal_approximation(final_time, t2):
                scene.append_to_caption(f"The collision is done at time : {final_time}s")
    while True:
        rate(100)
        if running:
            ay = -g  # ay at beginning of interval
            y += vy * dt  # use old vy to calculate new y
            vy += ay * dt  # use old ay to calculate new vy
            x += vx * dt
            z += vz * dt
            ball.pos = vector(x, y, z)

            ey += evy * dt
            ex += evx * dt
            ez += evz * dt
            enemy.pos = vector(ex, ey, ez)
            t += dt
            if y < 0:
                running = False
                print(x, y, z)
                scene.append_to_caption(f"{x} {y} {z}")


if __name__ == "__main__":
    main()
