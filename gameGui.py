import tkinter

class GameGui:

    def __init__(self, map_cell_locations=[]):
        """
        params:
            map_data: a list of (x,y) pairs that represent where map cells should be drawn
        """
        self.width = 800
        self.height = 600

        self.canvas_width = 600
        self.canvas_height = 400
        
        self.cell_size = 50 # size of a cell in our game
        self.cell_buffer = 2 # buffer away from edge of canvas?
        
        self.root = tkinter.Tk()
        self.root.geometry(f"{self.width}x{self.height}")

        self.label = tkinter.Label(master=self.root, text="type a command and press return (enter)")
        self.entry = tkinter.Entry(master=self.root)
        self.entry.bind("<Return>", self.entry_entered)
        self.canvas = tkinter.Canvas(master=self.root, width=self.canvas_width, height=self.canvas_height, background="darkgray")

        # draw grid of map cells
        for map_cell_location in map_cell_locations:
            # recall that the locations are in cell placement, so we need to multiply the location data by the size of a cell!
            self.canvas.create_rectangle(
                (map_cell_location[0] * self.cell_size) + self.cell_buffer,
                (map_cell_location[1] * self.cell_size) + self.cell_buffer,
                (map_cell_location[0] * self.cell_size) + self.cell_size + self.cell_buffer,
                (map_cell_location[1] * self.cell_size) + self.cell_size + self.cell_buffer)

        self.player = self.canvas.create_rectangle(10, 10, 30, 50, fill="green") # canvas created objects start at index 1

        self.canvas.pack()
        self.label.pack()
        self.entry.pack()

        self.entry.focus()

    def entry_entered(self, event):
        input = self.entry.get()

        # movement
        player_coords = self.canvas.coords(self.player)
        if input == "right" and player_coords[0] < self.canvas_width - self.cell_size:
            self.canvas.move(self.player, self.cell_size, 0) # move x and y distance of a given index in canvas
        elif input == "left"  and player_coords[0] > self.cell_size:
            self.canvas.move(self.player, -self.cell_size, 0) # move x and y distance of a given index in canvas
        elif input == "down" and player_coords[1] < self.canvas_height - self.cell_size:
            self.canvas.move(self.player, 0, self.cell_size) # move x and y distance of a given index in canvas
        elif input == "up" and player_coords[1] > self.cell_size:
            self.canvas.move(self.player, 0, -self.cell_size) # move x and y distance of a given index in canvas

    def run(self):
        self.root.mainloop()
