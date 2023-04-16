from manim import *

class CreateTableExample(Scene):
 

        
    def construct(self):
        dict = {}
        sequence = [6,3,5,2,7,8,1,10000]
        #initialization
        for r in range(0,8):
            for l in range(0,8):
                dict[str(r)+str(l)] = 0

        #filling the table bottom up
        for r in range(len(sequence)):
            if sequence[0] <= sequence[r]:
                dict["0"+str(r)] = 1
        for r in range(1,8):
            for c in range(r,8):
                # print("cur rc", r,c)
                if(sequence[r]>= sequence[c]):
                    dict[str(r)+str(c)] = dict[str((r-1))+str(c)]
                else: 
                    dict[str(r)+str(c)] = max(dict[str((r-1))+str(c)], 1 + dict[str((r-1))+str(r)])
        
        for k, v in dict.items():
            print(k, v)
        
        table = Table(
            [["0", "0", "0", "0","0", "0", "0", "0"],
            ["-1", "0", "0", "0", "1", "1","0","1"],
            ["-1", "-1", "1", "0", "1", "1","0","1"],
            ["-1", "-1", "-1", "0", "2", "2","0","2"],
            ["-1", "-1", "-1", "-1", "2", "2","0","2"],
            ["-1", "-1", "-1", "-1", "-1", "3","0","3"],
            ["-1", "-1", "-1", "-1", "-1", "-1","0","4"],
            ["-1", "-1", "-1", "-1", "-1", "-1","-1","4"],
            ],
            row_labels=[Text("[]", color=BLUE), Text("[6]", color=BLUE), Text("[6,3]", color=BLUE), Text("[6,3,5]", color=BLUE), Text("[6,3,5,2]", color=BLUE), Text("[6,3,5,2,7]", color=BLUE), Text("[6,3,5,2,7,8]", color=BLUE), Text("[6,3,5,2,7,8,1]", color=BLUE)],
            col_labels=[Text("A[1] = 6"), Text("A[2] = 3"), Text("A[3] = 5"), Text("A[4] = 2"),  Text("A[5] = 7"),  Text("A[6] = 8"),  Text("A[7] = 1"),  Text("inf")],
            include_outer_lines=True, color=BLACK)

        ent = table.get_entries_without_labels()
        for k in range(64):
            if (k in [8,16,17,24,25,26,32,33,34,35,40,41,42,43,44,48,49,50,51,52,53] or 56<= k<=62):
                ent[k].set_color(GREY)
            else:
                ent[k].set_color(BLACK)
        table.scale(0.4)
        self.play(table.create(), run_time = 2)
        for r in range(2,10):
            for l in range(2,r):
                table.add_highlighted_cell((r,l), color=GREY)
        row_des = Text("The column represents the prefix sub-array i.", color=(BLUE)).scale(0.4).shift(DOWN*2.8).shift(4.06*LEFT)
        col_des = Text("The row represents the limiter j.").scale(0.4).shift(2.8*UP).shift(RIGHT*4.8)
        self.add(table,row_des,col_des)
        self.wait(0.3)

        for r in range(2,10):
            for l in range(r,10):
                if r>3:
                    if sequence[r-2]< sequence[l-2]:
                        table.add_highlighted_cell((r-1,l), color=GREEN)
                        self.wait(2)
                        table.add_highlighted_cell((r-1,r-1), color=GREEN)
                        self.wait(2)
                        table[0].set_opacity(0)
                        table[1].set_opacity(0)
                        if dict[str(r-1-3)+str(l-2)] > dict[str(r-1-3)+str(r-3)] + 1:
                            table.add_highlighted_cell((r-1,l), color=ORANGE)
                        elif dict[str(r-1-3)+str(l-2)] == dict[str(r-1-3)+str(r-3)] + 1:
                            table.add_highlighted_cell((r-1,l), color=ORANGE)
                            table.add_highlighted_cell((r-1,r-1), color=ORANGE)
                        else:
                            table.add_highlighted_cell((r-1,r-1), color=ORANGE)
                        self.wait(2.5)
                        table[0].set_opacity(0)
                        table[1].set_opacity(0)
                        table[2].set_opacity(0)

                                      
                table.get_entries((r,l)).set_color(BLUE)
                self.wait(0.2)
                table.get_entries((r,l)).set_color(WHITE)
                self.wait(1)

                                
        self.play(table.create())
        self.wait(3)

