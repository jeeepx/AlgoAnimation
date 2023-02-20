from manim import *


def create_textbox(color, string):
    result = VGroup()  # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=3, fill_color=color,
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string, font_size=24).move_to(box.get_center())  # create text
    result.add(box, text)  # add both objects to the VGroup
    return result


def box_formatter(A, ss):
    return "["+', '.join(map(str, A))+']'+'\n'+'ss = [' + ', '.join(map(str, ss)) + ']'

def isSorted(a):
    return np.all(a[:-1] <= a[1:])

class CreateLCSTree(MovingCameraScene):
    sequence = [6, 3, 5, 2, 7]

    def construct(self):
  
        #position of x and y coordinate relative to the root
        x_position_offset = [0,32,16,8,4,2]
        y_position_offset = [0,2,5,8,11,13.5]

        """
        dictionary stores a tuple  (x coordinate position, subsequence) of each node
        """
        dict = {}
        mod_arr = np.asarray(self.sequence).astype(int)

        # root node creation
        n01 = create_textbox(color=BLUE, string=box_formatter(self.sequence, []))
        self.add(n01)
        dict['n01'] = (0,[])

        # all other node creation
        for level in range(1, 6):
            for node in range(2**level):
                parent_node = 'n'+str(level-1)+str((node+2)//2)

                cur_node = 'n'+str(level)+str(node+1)
                print("Level", level, "Child", cur_node)
                to_store = None
                if node % 2 == 0: #left child
                    to_store = dict[parent_node][1]
                    locals()[cur_node] = create_textbox(color=BLUE, string=box_formatter(mod_arr[:-1], to_store))
                else:
                    to_store = np.concatenate((np.array(mod_arr[-1:]), dict[parent_node][1])).astype(int)
                    locals()[cur_node] = create_textbox(color=BLUE, string=box_formatter(mod_arr[:-1], to_store))
                dist = 0
                if node < 2**level/2:
                    if(node % 2 == 0):
                        dist = dict[parent_node][0] + x_position_offset[level]
                        locals()[cur_node].shift((dist)*LEFT)
                    else:
                        dist = dict[parent_node][0] - x_position_offset[level]
                        locals()[cur_node].shift(dist*LEFT)
                else:
                    if(node % 2 == 0):
                        dist = dict[parent_node][0] - x_position_offset[level]
                        locals()[cur_node].shift((dist)*RIGHT)
                    else:
                        dist = dict[parent_node][0] + x_position_offset[level]
                        locals()[cur_node].shift(dist*RIGHT)
                dict[cur_node] = (dist, to_store)
                locals()[cur_node].shift((y_position_offset[level])*DOWN)
                self.add(locals()[cur_node])
                self.add(Line(locals()[parent_node].get_edge_center(DOWN), locals()[cur_node].get_edge_center(UP)))
            mod_arr = mod_arr[:-1]

        #root node animation
        self.play(self.camera.frame.animate.set(
            width=n01.width*25).move_to(n01))
        self.camera.frame.save_state()
        self.wait(1)

        self.play(self.camera.frame.animate.set(
            width=n01.width*3).move_to(n01))
        self.wait(1)
        self.play(Restore(self.camera.frame))

        #all other nodes animation
        for level in range(1, 6):
            for time in range(2**level):
                if (time) % 2 == 0 and level != 1:
                    parent_node = 'n'+str(level-1)+str((time+2)//2)
                    self.play(self.camera.frame.animate.set(
                        width=n01.width*3).move_to(locals()[parent_node]))
                    self.wait(1)
                cur_node = 'n'+str(level)+str(time+1)
                self.play(self.camera.frame.animate.set(
                    width=n01.width*5).move_to(locals()[cur_node]))
                self.wait(1)
                if level == 5:
                    if isSorted(dict[cur_node][1]):
                        locals()[cur_node].set_fill(GREEN, opacity=0.25)
                    else:
                        locals()[cur_node].set_fill(RED, opacity=0.25)
                    text = Text(box_formatter(mod_arr, dict[cur_node][1]), font_size=24).move_to(locals()[cur_node].get_center())
                    locals()[cur_node].add(text)

            self.play(Restore(self.camera.frame))
