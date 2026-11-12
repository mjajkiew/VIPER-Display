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
NULL_COORDS = [[0,0], [0,1], [1,0], 
               [0,6], [0,7], [0,8], 
               [1,7], [1,8], [2,8], 
               [6,0], [7,0], [7,1], 
               [7,6], [7,7], [7,8], 
               [6,7], [6, 8], [5,8]]

