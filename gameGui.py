import tkinter

class GameGui:

    def __init__(self):
        self.width = 800
        self.height = 600

        self.canvas_width = 600
        self.canvas_height = 400
        
        self.cell_size = 50 # size of a cell in our game
        
        self.root = tkinter.Tk()
        self.root.geometry(f"{self.width}x{self.height}")

        self.label = tkinter.Label(master=self.root, text="type a dcommand and press return (enter)")
        self.entry = tkinter.Entry(master=self.root)
        self.entry.bind("<Return>", self.entry_entered)
        self.canvas = tkinter.Canvas(master=self.root, width=self.canvas_width, height=self.canvas_height, background="darkgray")

        # draw grid
        for row in range(0, self.canvas_height, self.cell_size): # recall that range is exclusive of its upper end!
            self.canvas.create_line(0, row,  self.canvas_width, row)
        for column in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line(column, 0, column, self.canvas_height)

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
