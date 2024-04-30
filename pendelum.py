from manim import *
from pathlib import Path
import os

from numpy import angle

FLAG=f"-pqh"
SCENE="MyScene"

if __name__=="__main__":
    script=f"{Path(__file__).resolve()}"
    os.system(f"manim {script} {SCENE} {FLAG}")


class MyScene(Scene):
    def construct(self):
        
        times=ValueTracker(0)
        theta_max=PI/6
        l=3
        w=np.sqrt(15/3)
        T=2*PI/w

        refpoint=2*UP


        theta=DecimalNumber().set_color(BLACK).move_to(15*RIGHT)
        theta.add_updater(lambda m: m.set_value(theta_max * np.sin(w*times.get_value())))
        
        self.add(theta)



        def get_line1(x,y):
            line = Line(start=ORIGIN+refpoint, end=x*RIGHT+y*UP+refpoint,color=BLUE)
            global verticalline 
            verticalline = DashedLine(start=line.get_start(),end=line.get_start()+3*DOWN)
            return line

        
        line=always_redraw(lambda: get_line1(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))

        self.add(verticalline,line)

        def angle_arc(theta):
            global angle
            global arc_text
            if theta==0:
                angle=VectorizedPoint().move_to(10*RIGHT)
                arc_text=VectorizedPoint().move_to(10*RIGHT)
            elif theta>0:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=True,color=YELLOW, fill_opacity=0)
            else:
                angle = Angle(line, verticalline, quadrant=(1,1), other_angle=False,color=YELLOW, fill_opacity=0)
            return angle

        angle= always_redraw(lambda: angle_arc(theta.get_value()))
        self.add(angle)

        arctext=MathTex(r"\theta").scale(0.5).add_updater(lambda m: m.next_to(angle,DOWN))

        self.add(arctext)
        def get_ball(x,y):
            dot=Dot(fill_color=BLUE,fill_opacity=1).move_to(x*RIGHT+y*UP+refpoint).scale(l)
            return dot

        ball=always_redraw(lambda: get_ball(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))

        self.add(ball)

        
        self.play(times.animate.set_value(3*T),rate_func=linear,run_time=3*T)