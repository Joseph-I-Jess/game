import tkinter

class GameGui:

    def __init__(self):
        self.root = tkinter.Tk()

        self.label = tkinter.Label(master=self.root, text="this is a label")
        self.entry = tkinter.Entry(master=self.root)
        self.entry.bind("<Return>", self.button_clicked)

        self.label.pack()
        self.entry.pack()

    def button_clicked(self, event):
        self.label.config(text=self.entry.get())

    def run(self):
        self.root.mainloop()
