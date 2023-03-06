from manim import *
import os


class CicleWithTriangle(Scene):
    def construct(self):
        inner_circle = Arc(radius=2.5, start_angle=-PI/4, angle=2*PI)
        inner_circle.set_color(WHITE)
        inner_circle.set_x(0)

        outer_circle = Arc(radius=3, start_angle=PI/2, angle=2*PI)
        outer_circle.set_color(WHITE)
        outer_circle.set_x(0)

        triangle_upward = Triangle().scale(2.45)
        triangle_upward.set_x(0)
        triangle_upward.set_y(0.6)
        triangle_upward.set_color(WHITE)
        
        triangle_downward = Triangle().scale(2.45).rotate(60*DEGREES)
        triangle_downward.set_x(0)
        triangle_downward.set_y(-0.6)
        triangle_downward.set_color(WHITE)

        self.play(Create(inner_circle), Create(outer_circle))
        self.play(Create(triangle_upward))
        self.play(FadeOut(triangle_upward))
        self.play(Create(triangle_downward))
        self.play(FadeOut(triangle_downward))
        self.play(Create(triangle_upward))
        self.play(Create(triangle_downward))


if __name__ == "__main__":
    os.system("manim -p -ql ./manim/test_manim_example.py CicleWithTriangle")
