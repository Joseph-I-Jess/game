import tkinter

def main():
    root = tkinter.Tk()

    label = tkinter.Label(master=root, text="this is a label")
    entry = tkinter.Entry(master=root)
    button = tkinter.Button(master= root, text="click the button!")

    label.pack()
    entry.pack()
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()