import tkinter

class GameGui:

    def __init__(self):
        self.root = tkinter.Tk()

        self.label = tkinter.Label(master=self.root, text="type a dcommand and press return (enter)")
        self.entry = tkinter.Entry(master=self.root)
        self.entry.bind("<Return>", self.entry_entered)
        self.canvas = tkinter.Canvas(master=self.root, width=600, height=400, background="darkgray")

        self.canvas.create_rectangle(20, 20, 40, 60, fill="green")

        self.canvas.pack()
        self.label.pack()
        self.entry.pack()

    def entry_entered(self, event):
        self.label.config(text=self.entry.get())

    def run(self):
        self.root.mainloop()
