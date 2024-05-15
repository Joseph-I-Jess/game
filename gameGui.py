import tkinter

class GameGui:

    def __init__(self):
        self.root = tkinter.Tk()

        self.label = tkinter.Label(master=self.root, text="type a dcommand and press return (enter)")
        self.entry = tkinter.Entry(master=self.root)
        self.entry.bind("<Return>", self.entry_entered)
        self.canvas = tkinter.Canvas(master=self.root, width=600, height=400, background="darkgray")

        self.player = self.canvas.create_rectangle(20, 20, 40, 60, fill="green") # canvas created objects start at index 1

        self.canvas.pack()
        self.label.pack()
        self.entry.pack()

        self.entry.focus()

    def entry_entered(self, event):
        input = self.entry.get()

        if input == "right":
            self.canvas.move(self.player, 10, 0) # move x and y distance of a given index in canvas
            

    def run(self):
        self.root.mainloop()
