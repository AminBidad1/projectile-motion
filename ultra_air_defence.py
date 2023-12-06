from vpython import *
import math

from sympy import Symbol, real_roots


# Web VPython 3.2

scene.caption = """
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.\n
"""


def equal_approximation(val1, val2):
    if abs((val2 - val1)/val1) <= 0.001:
        return True
    return False


def get_dt():
    dt = input("Enter yuor dt: ")
    if not dt:
        return 0.005
    return float(dt)


def main():
    g = 10
    ey = float(input("Enter your enemy Y0: "))
    ex = float(input("Enter your enemy X0: "))
    ez = float(input("Enter your enemy Z0: "))
    evy = float(input("Enter your enemy Vy: "))
    evx = float(input("Enter your enemy Vx: "))
    evz = float(input("Enter your enemy Vz: "))
    sy = 0
    sx = 0
    sz = 0
    v0 = float(input("Enter your V0 size: "))
    radius = float(input("Enter your radius: "))
    dt = get_dt()
    t = 0
    ball = sphere(pos=vector(sx, sy, sz), radius=radius, color=color.blue, make_trail=True,
                  trail_type='points', interval=10, retain=50000)
    enemy = sphere(pos=vector(ex, ey, ez), radius=radius, color=color.red, make_trail=True,
                   trail_type='points', interval=10, retain=50000)

    running = True
    a4 = (g**2) / 4
    a3 = g * evy
    a2 = evx**2 + evy**2 + evx**2 + g*ey - v0**2
    a1 = 2 * (evx*ex + evy*ey + evz*ez)
    a0 = ex**2 + ey**2 + ez**2
    x = Symbol('x', real=True)
    results = real_roots(a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0, x)
    print(results)
    vx = 0
    vy = 0
    vz = 0
    if not results:
        scene.append_to_caption("There is no collision\n")
    else:
        for time in results:
            if "I" not in str(time):
                time = float(time)
                if time > 0:
                    vx = (evx*time+ex)/time
                    vz = (evz*time+ez)/time
                    vy = (0.5*g*time**2 + evy*time + ey)/time
                    if equal_approximation(vx*time, evx*time + ex):
                        if equal_approximation(vz*time, evz*time + ez):
                            if equal_approximation(-0.5*g*time**2 + vy*time, evy*time + ey):
                                if evy*time + ey > 0:
                                    try:
                                        teta_x = math.degrees(math.acos(vx/v0))
                                        teta_z = math.degrees(math.acos(vz/v0))
                                        print(vy/v0)
                                        teta_y = math.degrees(math.acos(vy/v0))

                                        x_fianl = evx*time + ex
                                        y_final = evy*time + ey
                                        z_final = evz*time + ez
                                        scene.append_to_caption(f"teta x: {round(teta_x, 2)} |"
                                                                f" teta y: {round(teta_y, 2)} |"
                                                                f" teta z: {round(teta_z, 2)}")
                                        scene.append_to_caption("\n" + f"Vx: {round(vx, 2)}m/s |"
                                                                       f" Vy: {round(vy, 2)}m/s |"
                                                                       f" Vz: {round(vz, 2)}m/s")
                                        scene.append_to_caption(
                                            "\n" + f"fianl X: {round(x_fianl, 2)}m |"
                                                   f"final Y: {round(y_final, 2)}m |"
                                                   f"final Z: {round(z_final, 2)}m"
                                        )
                                        scene.append_to_caption("\n" +
                                                                f"final time: {round(time, 2)}s"
                                                                + "\n")
                                        break
                                    except Exception:
                                        scene.append_to_caption("There is no collision\n")

        else:
            scene.append_to_caption("There is no collision\n")
    enemy_running = True
    while True:
        rate(100)
        if running:
            ay = -g  # ay at beginning of interval
            sy += vy * dt  # use old vy to calculate new y
            vy += ay * dt  # use old ay to calculate new vy
            sx += vx * dt
            sz += vz * dt
            ball.pos = vector(sx, sy, sz)

            if enemy_running:
                ey += evy * dt
                ex += evx * dt
                ez += evz * dt
                enemy.pos = vector(ex, ey, ez)
                if ey < 0:
                    enemy_running = False
            t += dt
            if sy < 0:
                running = False
                print(sx, sy, sz)


if __name__ == "__main__":
    main()
