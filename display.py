import arcade
import arcade.gui
import constants as c
from arcade.gui.events import (
    UIEvent,
    UIKeyEvent,
    UIMouseDragEvent,
    UIMouseEvent,
    UIMousePressEvent,
    UIMouseReleaseEvent,
    UIMouseScrollEvent,
    UIOnChangeEvent,
    UIOnClickEvent,
    UITextInputEvent,
    UITextMotionEvent,
    UITextMotionSelectEvent,
)

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.

        param:
            self

        return:
            nothing
        """

        super().__init__()

        self.left_null_coord_found = False

        self.right_null_coord_found = False

        self.background_color = arcade.color.BLUEBERRY

        self.manager = arcade.gui.UIManager()

        self.left_eye_grid = arcade.gui.UIGridLayout(
            column_count=9, row_count=8, horizontal_spacing=10, vertical_spacing=10
        )

        self.right_eye_grid = arcade.gui.UIGridLayout(
             column_count=9, row_count=8, horizontal_spacing=10, vertical_spacing=10
        )

        #loop to create textboxes in the grid layout widget
        for rw in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                for i in range(c.NULL_COORDS_LEN):
                    #if null coordinate in left exists, then left null coord found == true
                    if(rw == c.LEFT_NULL_COORDS[i][0] and col == c.LEFT_NULL_COORDS[i][1]):
                        self.left_null_coord_found = True
                    if(rw == c.RIGHT_NULL_COORDS[i][0] and col == c.RIGHT_NULL_COORDS[i][1]):
                            self.right_null_coord_found = True
                #if it is not a null coordinate, add an input textbox to the grid layout at cuur coord
                if(self.left_null_coord_found == False):
                    self.input_field = arcade.gui.UIInputText(
                                        width=40,
                                        height=40,
                                        text="0",
                                        text_color=arcade.color.BLACK
                                    ).with_background(color=arcade.types.Color.from_hex_string(c.GRAPH_CLRS[3]))
                    self.left_eye_grid.add(self.input_field, column=col, row=rw)
                if(self.right_null_coord_found == False):
                    self.input_field = arcade.gui.UIInputText(
                                        width=40,
                                        height=40,
                                        text="0",
                                        text_color=arcade.color.BLACK
                                    ).with_background(color=arcade.types.Color.from_hex_string(c.GRAPH_CLRS[3]))
                    self.right_eye_grid.add(self.input_field, column=col, row=rw)
                #reset back to false
                self.right_null_coord_found = False
                self.left_null_coord_found = False

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            align_x = -250,
            child=self.left_eye_grid,
        )

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            align_x = 250,
            child=self.right_eye_grid,
        )

        #hbox for eye title
        self.h_box1 = arcade.gui.UIBoxLayout(space_between=20, vertical=False)
        self.textbox = arcade.gui.UITextArea(text=f"Left Eye", text_color=arcade.color.BLACK, width=100, font_size=15)
        self.anchor.add(self.h_box1, anchor_x = "center_x", anchor_y= "top", align_y=-25)
        self.h_box1.add(self.textbox)

        #hbox for buttons
        self.h_box2 = arcade.gui.UIBoxLayout(space_between=20, vertical=False)
        self.anchor.add(self.h_box2, anchor_x="center_x", anchor_y="bottom", align_y=5)
        
        self.convert_button = arcade.gui.UIFlatButton(text="Convert to List", height= 30, width=150)
        self.h_box2.add(self.convert_button)

        @self.convert_button.event("on_click")
        def _(event):
            convert_to_list(self)
            print("printed!")

        self.manager.enable()

    def on_draw(self):
        """
        Render the screen.

        param:
            self
        
        return: 
            nothing
        """

        # This command has to happen before we start drawing
        self.clear()

        self.manager.draw()


def convert_to_list(self):
    """
    Convert the grid layout to a list

    param: 
        self

    return:
        The formatted list
    """

    left_eye_lst = []
    right_eye_lst = []
    #self.grid.children is a list of all the children of the grid. it is NOT a perfect square, so 
    #converting to a 2D list requires to keep track of what index we should be looking at for the grid layout widget
    #if the coordinate is not represented in the grid layout, we put -1 in its place in the 2D list
    left_grid_idx = 0
    right_grid_idx = 0
    for rw in range(c.ROW_COUNT):
        left_row_list = []
        right_row_list = []
        for col in range(c.COLUMN_COUNT):
            for i in range(c.NULL_COORDS_LEN):
                #if null coordinate in left exists, then left null coord found == true
                if(rw == c.LEFT_NULL_COORDS[i][0] and col == c.LEFT_NULL_COORDS[i][1]):
                    self.left_null_coord_found = True
                if(rw == c.RIGHT_NULL_COORDS[i][0] and col == c.RIGHT_NULL_COORDS[i][1]):
                        self.right_null_coord_found = True
            #if it is not a null coordinate, we append what is currently in the gridlayout to the list
            if(self.left_null_coord_found == False):
                left_row_list.append(int(self.left_eye_grid.children[left_grid_idx].text))
                left_grid_idx += 1 #cant have both grid indexes increase, MUST FIX!
            else:
                left_row_list.append(-1)
            if(self.right_null_coord_found == False):
                right_row_list.append(int(self.right_eye_grid.children[right_grid_idx].text))
                right_grid_idx += 1
            else:
                right_row_list.append(-1)
            self.left_null_coord_found = False
            self.right_null_coord_found = False
        #append the row we made to the overall list
        left_eye_lst.append(left_row_list)
        right_eye_lst.append(right_row_list)
        #make row_list empty again to create the next row in the grid
        left_row_list = []
        right_row_list = []
    print(left_eye_lst)
    print(right_eye_lst)

def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(c.WINDOW_WIDTH, c.WINDOW_HEIGHT, c.WINDOW_TITLE)

    # Create the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()