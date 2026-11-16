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

        self.null_coord_found = False

        self.background_color = arcade.color.BLUEBERRY

        self.manager = arcade.gui.UIManager()

        self.grid = arcade.gui.UIGridLayout(
            column_count=9, row_count=8, horizontal_spacing=10, vertical_spacing=10
        )

        #loop to create textboxes in the grid layout widget
        for rw in range(c.ROW_COUNT):
            for col in range(c.COLUMN_COUNT):
                for i in c.NULL_COORDS:
                    #if null coordinate exists, then null coord found == true
                    if(rw == i[0] and col == i[1]):
                        self.null_coord_found = True
                #if it is not a null coordinate, add an input textbox to the grid layout at cuur coord
                if(self.null_coord_found == False):
                    self.input_field = arcade.gui.UIInputText(
                                        width=40,
                                        height=40,
                                        text="0",
                                        text_color=arcade.color.BLACK
                                    ).with_background(color=arcade.types.Color.from_hex_string(c.GRAPH_CLRS[3]))
                    self.grid.add(self.input_field, column=col, row=rw)
                #reset back to false
                self.null_coord_found = False

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid,
        )
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

    lst = []
    #self.grid.children is a list of all the children of the grid. it is NOT a perfect square, so 
    #converting to a 2D list requires to keep track of what index we should be looking at for the grid layout widget
    #if the coordinate is not represented in the grid layout, we put -1 in its place in the 2D list
    grid_idx = 0
    for rw in range(c.ROW_COUNT):
        row_list = []
        for col in range(c.COLUMN_COUNT):
            for i in c.NULL_COORDS:
                #if null coordinate exists, then null coord found == true
                if(rw == i[0] and col == i[1]):
                    self.null_coord_found = True
            #if it is not a null coordinate, we ap
            if(self.null_coord_found == False):
                row_list.append(self.grid.children[grid_idx])
                grid_idx += 1
            else:
                row_list.append(-1)
            self.null_coord_found = False
        #append the row we made to the overall list
        lst.append(row_list)
        #make row_list empty again to create the next row in the grid
        row_list = []
    return lst



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