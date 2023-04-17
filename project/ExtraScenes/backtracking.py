from manim import *

class CreateIntroScene(Scene):

    def construct(self):

        topic = Text("Backtracking - Generating Increasing Subsequences", color=(BLUE)).scale(0.7).shift(UP*2)
        self.add(topic)
        self.wait(3)
        exp = Text("Creating only increasing subsequence instead of creating all possible subsequences.").next_to(topic, 2*DOWN).scale(0.45)
        self.play(FadeIn(exp))
        self.wait(15)
        sequence = Text("[6, 3, 5, 2, 7, 8, 1]").next_to(exp, 2*DOWN)
        self.play(Write(sequence))
        self.wait(10)
        sequence_1 = Text("[6, 3, 5, 2, 7, 8, 1]", t2c={'6, 3, 5, 2, 7, 8,': '#FFFFFF','1': '#fbb003' }).next_to(exp, 2*DOWN)
        self.play(FadeIn(sequence_1))
        self.wait(14)
        sequence_2 = Text("[6, 3, 5, 2, 7, 8, 1]", t2c={'6, 3, 5, 2, 7,': '#FFFFFF','8': '#fbb003','1': '#FFFFFF' }).next_to(exp, 2*DOWN)
        self.play(FadeIn(sequence_2))
        self.wait(16)
        self.play(FadeOut(topic,exp,sequence,sequence_1,sequence_2))



        
       