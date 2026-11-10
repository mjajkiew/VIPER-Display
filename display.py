import arcade

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 9

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_TITLE = "VIPER Display"

# 35 graph colors 
GRAPH_CLRS = ["#ffffff",
              "#f8f8f8",
              "#f0f0f0",
              "#efefef",
              "#e8e8e8",
              "#e0e0e0",
              "#dfdfdf",
              "#d8d8d8",
              "#d0d0d0",
              "#cfcfcf",
              "#c8c8c8",
              "#c0c0c0",
              "#bfbfbf",
              "#b8b8b8",
              "#b0b0b0",
              "#afafaf",
              "#a8a8a8",
              "#a0a0a0",
              "#9f9f9f",
              "#989898",
              "#909090",
              "#8f8f8f",
              "#888888",
              "#808080",
              "#7f7f7f",
              "#787878",
              "#707070",
              "#6f6f6f",
              "#686868",
              "#606060",
              "#5f5f5f",
              "#505050",
              "#4f4f4f",
              "#404040",
              "#303030",]

#coordinates that cannot be filled in
NULL_COORDS = [[0,0], [0,1], [1,0], [0,6], [0,7], [0,8], [1,7], [1,8], [2,8], [6,0], [7,0], [7,1], [7,6], [7,7], [7,8], [6,7], [6, 8], [5,8]]


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.
        """

        super().__init__()

        # Create a 2 dimensional array
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        self.background_color = arcade.color.BLUEBERRY

        #submit textbox
        self.submit_num = "0"

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        null_coord_found = False

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Draw the color for the box based on the current number
                for i in NULL_COORDS:
                    if(row == i[0] and column == i[1]):
                        null_coord_found = True

                if(null_coord_found):
                    color = arcade.color.TRANSPARENT_BLACK
                else:
                    color = arcade.types.Color.from_hex_string(GRAPH_CLRS[self.grid[row][column]])

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, WIDTH, HEIGHT), color)

                # Draw the value on the box
                null_coord_found = False
                

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column}). Box value: {self.grid[row][column]}")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Clicking changes the value, once max (35) is reached, clicking again will result in 0
            self.grid[row][column] += 1
            if(self.grid[row][column] >= 35):
                self.grid[row][column] = 0


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()