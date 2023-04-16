from manim import *

class CreateIntroScene(Scene):
    sequence = [6, 3, 5, 2, 7, 8, 1]

    def construct(self):

        topic = Text("LIS(A[1...n])", color=(BLUE)).scale(0.6).shift(2.7*UP)
        
        text2 = Paragraph('Case 1: The longest increasing subsequence does not contain A[n].\n\n\t\t This means that LIS(A[1...n]) is LIS(A[1...n-1]',color=WHITE).scale(0.45).next_to(topic, 2*DOWN)
        # text3 = Text('This means that LIS(A[1...n]) is LIS(A[1...n-1]', color=BLUE).scale(0.35).next_to(text2, DOWN)

        # self.add(text2)

        text4 = Paragraph('Case 2: The longest increasing subsequence contains A[n].\n\n\t\tThis means that we have to find the longest increasing subsequence in A, \n\n\t\twhere each number in the sequence is less than A[n].', color=WHITE).scale(0.45).next_to(text2, DOWN*2)
        # text3 = Text('This means that LIS(A[1...n]) is LIS(A[1...n-1]', color=BLUE).scale(0.35).next_to(text2, DOWN)
        self.add(topic,text2, text4)
        # self.wait(1)
        text5 = Paragraph('\t\tA more general problem is LIS_smaller( A[1..n], x), \n\n\t\t which returns the longest increasing subsequence in A, \n\n\t\twhere each number in the sequence is less than x.', color=GREEN).scale(0.45).next_to(text4, DOWN)
        self.add(text5)

        
class RunTime(Scene):
    def construct(self):

        topic = Text("Naive Recursion Enumeration - Time Complexity", color=(BLUE)).scale(0.7).shift(2*UP)
        
        
        runTime = MathTex(r"\text{Time Complexity: } O(n2^n)").scale(0.8).next_to(topic,DOWN*1)      # text3 = Text('This means that LIS(A[1...n]) is LIS(A[1...n-1]', color=BLUE).scale(0.35).next_to(text2, DOWN)

        runTime1 = MathTex(r"2^n \text{comes from the fact that there are } 2^n \text{subsequences of a sequence.}\\ O(n) \text{ is the time taken to check if a given sequence is increasing.}").scale(0.8).next_to(runTime,DOWN*1)      # text3 = Text('This means that LIS(A[1...n]) is LIS(A[1...n-1]', color=BLUE).scale(0.35).next_to(text2, DOWN)
        self.add(topic,runTime1,runTime)


class DP(Scene):
    def construct(self):

        topic = Text("Dynamic Programming - Number of Distinct Problems", color=BLUE).scale(0.7).shift(2*UP)
        
        text2 = Paragraph('1.The variable x can only be one of the n values in the input scene.',color=WHITE).scale(0.35).next_to(topic, 2*DOWN)

        text4 = Paragraph('2. The input sequence can only be a prefix of the original input. \n\n\t\tTherefore, there are only n input prefixes that A can be.', color=WHITE).scale(0.35).next_to(text2, DOWN*2)
        
        nsquare = MathTex(r"\text{Total distinct subproblems: } O(n^2)").scale(0.5).next_to(text4,DOWN*2) 

        self.add(topic,text2,text4,nsquare)

class DPRec(Scene):
    def construct(self):

        topic = Text("Naming Sub-Problems and Recursive Equation", color=(BLUE)).scale(0.7).shift(2*UP)
        
        rec = Text("LIS(i,j) returns the length of the longest increasing sequence in A[1...i] consisting of numbers less than A[j].", t2c = {}).scale(0.42).next_to(topic, 1.5*DOWN)
        baseCase = Text('Base case: LIS(0,j) = 0    for 1 ≤ j ≤ n+1',t2c={'Base case:': '#fbb003' }).scale(0.45).next_to(rec, 1.5*DOWN)
        # recCase = Text('Recursive relation: ',t2c={'Recursive relation:': '#fbb003' }).scale(0.45).next_to(baseCase, DOWN)
        recCase1 = Text('Recursive relation:    LIS(i,j) = LIS(i-1,j)   if A[i] ≥ A[j]', color=WHITE, t2c={'Recursive relation:': '#fbb003' }).scale(0.45).next_to(baseCase, DOWN)
        recCase2 = Text('LIS(i,j) = max( LIS(i-1,j), 1 + LIS(i-1,i) )   if A[i] < A[j]',color=WHITE).scale(0.45).next_to(recCase1, DOWN)

        self.add(topic)
        self.wait(0.1)
        self.add(rec)
        self.wait(0.1)
        self.add(baseCase)
        self.wait(0.1)
        self.add(recCase1)
        self.wait(0.1)
        self.add(recCase2)
        self.wait(0.1)



class RunTimeBackTracking(Scene):
    def construct(self):

        topic = Text("Dynamic Programming - Time Complexity", color=(BLUE)).scale(0.7).shift(1.5*UP)
        
        
        runTime = MathTex(r"\text{Worst Case Time Complexity: } O(2^n)").scale(0.8).next_to(topic,DOWN*1.5)      

        runTime1 = MathTex(r"2^n \text{comes from the fact that there are } 2^n \text{ subsequences of a sequence.}").scale(0.8).next_to(runTime,DOWN*1)    
        self.add(topic,runTime1,runTime)


class RunTimeDP(Scene):
    def construct(self):

        topic = Text("Dynamic Programming - Time Complexity", color=(BLUE)).scale(0.7).shift(1.5*UP)
        
        
        runTime = MathTex(r"\text{Time Complexity: } O(n^2)").scale(0.8).next_to(topic,DOWN*1.5)      

        runTime1 = MathTex(r"n^2 \text{comes from the number of total distinct subproblems.}").scale(0.8).next_to(runTime,DOWN*1)    
        self.add(topic,runTime1,runTime)

class Conclusion(Scene):
    def construct(self):

        topic = Text("Longest Increasing Subsequence Problem Summary:", color=(BLUE)).scale(0.7).shift(1.5*UP)
                
        runTime = MathTex(r"\text{Recursive Problem: }  O(n2^n)").scale(0.8).next_to(topic,DOWN*1.5)      
        runTime1 = MathTex(r"\text{Backtracking:  }  O(2^n)").scale(0.8).next_to(runTime,DOWN*1.25)      
        runTime2 = MathTex(r"\text{Dynamic Programing: }  O(n^2)").scale(0.8).next_to(runTime1,DOWN*1.25)      

        self.add(topic)
        self.add(runTime)
        self.add(runTime1)
        self.add(runTime2)