from tkinter import *
import os


def genEmotes(lb1, lb2, e1, e2, b1):
    print(e1.get())
    print(e2.get("1.0", END))
    prefix = ":" + str(e1.get()) + ":"
    message = e2.get("1.0", END)
    newmessage = ""
    i=0
    for x in message:
        if (message[i:i+1] != " "):
            newmessage = newmessage + prefix.replace("#", message[i:i+1]) + " "
        else:
            newmessage = newmessage + "   "
        i = i+1
    newmessage = newmessage[:(len(newmessage)-len(prefix)-1)]
    printEmotes(newmessage)


def printEmotes(message):
    outputBox = Tk()
    outputBox.title("output")
    outText = Text(outputBox, width=100)
    outText.insert(END, message)
    outText.grid(row=0)


# Main Body
def main():
    print(12)
    global LB1, LB2, ENTR1, ENTR2, butto1
    root = Tk()
    root.title("Emote Generator")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root.iconbitmap(r'' + dir_path + '\steg.ico')

    menubar = Menu(root)
    menubar.add_command(label="Close Application", command=lambda: root.destroy())
    root.config(menu=menubar)

    LB1 = Label(root, text="Emote Prefix", font=('Arial', 21))
    ENTR1 = Entry(root, bd=1)

    LB2 = Label(root, text="Message to be formatted", font=('Arial', 20))
    ENTR2 = Text(root, width=31, height=10)

    butto1 = Button(root, text="Output text", font=('Arial', 20),
                    command=lambda: genEmotes(LB1, LB2, ENTR1, ENTR2, butto1))

    LB1.grid(row=1, column=0, columnspan=3)
    ENTR1.grid(row=2, column=0, columnspan=3)
    LB2.grid(row=3, column=0, columnspan=3)
    ENTR2.grid(row=4, column=0, columnspan=3)
    butto1.grid(row=5, column=0, columnspan=3)

    root.mainloop()


main()
