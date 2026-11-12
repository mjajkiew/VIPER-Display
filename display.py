import arcade
import constants as c

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.
        """

        super().__init__()

        self.text = ""

        # Create a 2 dimensional array
        self.grid = []
        for row in range(c.ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(c.COLUMN_COUNT):
                print(f"ROW: {row}")
                print(f"COL: {column}")
                self.grid[row].append(0)  # Append a cell

        self.background_color = arcade.color.BLUEBERRY

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        null_coord_found = False

        # Draw the grid
        for row in range(c.ROW_COUNT):
            for column in range(c.COLUMN_COUNT):
                # Draw the color for the box based on the current number
                for i in c.NULL_COORDS:
                    if(row == i[0] and column == i[1]):
                        null_coord_found = True

                if(null_coord_found):
                    color = arcade.color.TRANSPARENT_BLACK
                else:
                    color = arcade.types.Color.from_hex_string(c.GRAPH_CLRS[self.grid[row][column]])

                # Do the math to figure out where the box is
                x = (c.MARGIN + c.WIDTH) * column + c.MARGIN + c.WIDTH // 2
                y = (c.MARGIN + c.HEIGHT) * row + c.MARGIN + c.HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, c.WIDTH, c.HEIGHT), color)

                # Draw the value on the box
                null_coord_found = False
                
            arcade.draw_text(self.text, 250, 450, arcade.color.BLACK, 24, anchor_x='center')


                

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (c.WIDTH + c.MARGIN))
        row = int(y // (c.HEIGHT + c.MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column}).")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < c.ROW_COUNT and column < c.COLUMN_COUNT:

            print(f"Box value: {self.grid[row][column]}")
            # Clicking changes the value, once max (35) is reached, clicking again will result in 0
            self.grid[row][column] += 1
            if(self.grid[row][column] >= 35):
                self.grid[row][column] = 0
       
    def on_key_press(self, key, key_modifiers):
        if(key == 65288):
            if(len(self.text) >= 1):
                #print(self.text.removesuffix(self.text[-1]))
                self.text = self.text.removesuffix(self.text[-1])
        else:
            self.text += chr(key)
        #print(self.text)


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