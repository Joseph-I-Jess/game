import tkinter

class GameGui:

    def __init__(self):
        self.root = tkinter.Tk()

        self.label = tkinter.Label(master=self.root, text="this is a label")
        self.entry = tkinter.Entry(master=self.root)
        self.button = tkinter.Button(master= self.root, text="click the button!", command=self.button_clicked)

        self.label.pack()
        self.entry.pack()
        self.button.pack()

    def button_clicked(self):
        self.label.config(text=self.entry.get())

    def run(self):
        self.root.mainloop()
