import tkinter

class GameGui:

    def __init__(self):
        root = tkinter.Tk()

        label = tkinter.Label(master=root, text="this is a label")
        entry = tkinter.Entry(master=root)
        button = tkinter.Button(master= root, text="click the button!", command=lambda: self.button_clicked(label, entry))

        label.pack()
        entry.pack()
        button.pack()
    
        root.mainloop()

    def button_clicked(self, label, entry):
        label.config(text=entry.get())

def main():
    my_game = GameGui()


if __name__ == "__main__":
    main()