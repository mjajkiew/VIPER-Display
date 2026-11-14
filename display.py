import arcade
import arcade.gui
import constants as c

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

       #this is how you all a child in a gridlayout 
        #print(self.grid.children[0].text)

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
                                        text_color=arcade.color.WHITE
                                    ).with_border(color=arcade.color.WHITE, width=2)
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