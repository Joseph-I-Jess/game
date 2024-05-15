import tkinter

def button_clicked(label, entry):
    label.config(text=entry.get())

def main():
    root = tkinter.Tk()

    label = tkinter.Label(master=root, text="this is a label")
    entry = tkinter.Entry(master=root)
    button = tkinter.Button(master= root, text="click the button!", command=lambda: button_clicked(label, entry))

    label.pack()
    entry.pack()
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()