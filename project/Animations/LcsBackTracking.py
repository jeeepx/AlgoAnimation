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


def box_formatter(A, ss, x):
    return "["+', '.join(map(str, A))+']'+'\n'+'ss = [' + ', '.join(map(str, ss)) + ']'+ '\n' + ' x = ' + x


def isSorted(a):
    return np.all(a[:-1] <= a[1:])

def x_helper(subsequence):
    if len(subsequence) < 1:
        return "inf"
    else:
        return str(subsequence[0])


class CreateLCSTree(MovingCameraScene):
    sequence = [6, 3, 5, 2, 7, 8, 1]

    def construct(self):

        # position of x and y coordinate relative to the root
        x_position_offset = [0, 80, 60, 34, 22, 12, 6, 2]
        y_position_offset = [0, 2, 5, 8, 11, 14, 16.5, 18]

        """
        dictionary stores a tuple  (x coordinate position, subsequence, X) of each node
        """
        dict = {}
        mod_arr = np.asarray(self.sequence).astype(int)

        # root node creation
        n01 = create_textbox(
            color=BLUE, string=box_formatter(self.sequence, [], x_helper([])))
        self.add(n01)
        dict['n01'] = (0, [], float('inf'))
        level = 1
        node = 0
        # all other node creation
        while level < 8:
            node = 0
            while node < 2**level:
                parent_node = 'n'+str(level-1)+str((node+2)//2)
                if  parent_node not in dict:
                    node = node + 1
                    continue
                cur_node = 'n'+str(level)+str(node+1)
                print("Level", level, "Child", cur_node)
                print("parentnode", parent_node)
                to_store = dict[parent_node][1]
                x = float('inf')
                
                if node % 2 == 0:  # left child
                    locals()[cur_node] = create_textbox(
                        color=BLUE, string=box_formatter(mod_arr[:-1], to_store, x_helper(to_store)))
                    x = dict[parent_node][2]
                else:
                    if dict[parent_node][2]  > mod_arr[-1]:
                        to_store = np.concatenate(
                            (np.array(mod_arr[-1:]), dict[parent_node][1])).astype(int)
                        x = mod_arr[-1]
                        locals()[cur_node] = create_textbox(
                    color=BLUE, string=box_formatter(mod_arr[:-1], to_store, x_helper(to_store)))
                    else: #skip that iteration bc right node not needed
                        node = node +  1
                        continue
                dist = 0
                if node < 2**level:
                    if(node % 2 == 0):
                        if dict[parent_node][2]  > mod_arr[-1]:
                            dist = dict[parent_node][0] + x_position_offset[level]
                        else:
                            dist = dict[parent_node][0] # if no right node, continue straight down
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
                dict[cur_node] = (dist, to_store, x)
                locals()[cur_node].shift((y_position_offset[level])*DOWN)
                self.add(locals()[cur_node])
                self.add(Line(locals()[parent_node].get_edge_center(
                    DOWN), locals()[cur_node].get_edge_center(UP)))
                node = node + 1
            mod_arr = mod_arr[:-1]
            level = level + 1

        # root node animation
        self.play(self.camera.frame.animate.set(
            width=n01.width*25).move_to(n01))
        self.camera.frame.save_state()
        self.wait(1)

        self.play(self.camera.frame.animate.set(
            width=n01.width*3).move_to(n01))
        self.wait(1)
        self.play(Restore(self.camera.frame))

        # all other nodes animation
        for level in range(1, 6):
            for time in range(2**level):
                cur_node = 'n'+str(level)+str(time+1)
                if cur_node not in dict:
                    continue
                if (time) % 2 == 0 and level != 1:
                    parent_node = 'n'+str(level-1)+str((time+2)//2)
                    self.play(self.camera.frame.animate.set(
                        width=n01.width*3).move_to(locals()[parent_node]))
                    self.wait(1)
                self.play(self.camera.frame.animate.set(
                    width=n01.width*5).move_to(locals()[cur_node]))
                self.wait(3)


            self.play(Restore(self.camera.frame))
