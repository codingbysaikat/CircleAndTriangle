from manim import *

class CircleAndTriangle(Scene):
    def construct(self):
        text = Text("Simple Geometry")
        text.to_edge(UP)
        circle = Circle().scale(1.5)
        triangle = Triangle().scale(1.5)



        circle.shift(UP * 2)
        triangle.shift(DOWN * 2)

        self.play(Write(text))

        self.play(Create(circle), Create(triangle))
        self.wait()

        self.play(
            circle.animate.shift(DOWN * 2),
            triangle.animate.shift(UP * 2),
        )

        self.play(Rotate(triangle,4*PI, about_point= circle.get_center()), run_time = 3)
        self.wait()












