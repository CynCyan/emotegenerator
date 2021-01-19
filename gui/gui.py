import os
from tkinter import *


# This function surrounds the imported text with the prefix
def genEmotes(lb1, lb2, e1, e2, b1):
    # format the prefix for discord
    prefix = ":" + str(e1.get()) + ":"
    message = e2.get("1.0", END)
    newmessage = ""
    i = 0
    # wraps the prefix around the message by inserting each letter over #
    for x in message:
        if str.isalpha(message[i:i + 1]):
            newmessage = newmessage + prefix.replace("#", message[i:i + 1]) + " "
        elif message[i:i + 1] == " ":
            newmessage = newmessage + "   "
        else:
            newmessage = newmessage + message[i:i + 1]
        i = i + 1
    # newmessage = newmessage[:(len(newmessage)-len(prefix)-1)]
    printEmotes(newmessage)


# display the emotes in a separate window
def printEmotes(message):
    outputBox = Tk()
    outputBox.title("output")

    # create exit button at top of print
    menubar = Menu(outputBox)
    menubar.add_command(label="Close Window", command=lambda: outputBox.destroy())
    outputBox.config(menu=menubar)

    # button to copy to clipboard
    menubar.add_command(label="Copy to Clipboard", command=lambda: clipit(message))

    outText = Text(outputBox, width=100)
    outText.insert(END, message)
    outText.grid(row=0)


# copies message to clipboard
def clipit(message):
    c = Tk()
    c.withdraw()
    c.clipboard_clear()
    c.clipboard_append(message)
    c.update()
    c.destroy()


# converts message in entry box to uppercase
def upperbox(e2):
    newmessage = e2.get("1.0", END)
    newmessage = str.upper(newmessage)
    e2.delete("1.0", END)
    e2.insert("1.0", newmessage)


# converts message in entry box to lowerbox
def lowerbox(e2):
    newmessage = e2.get("1.0", END)
    newmessage = str.lower(newmessage)
    e2.delete("1.0", END)
    e2.insert("1.0", newmessage)


# The GUI, opens a window with text boxes to enter in the prefix and message
def main():
    # All the elements of the GUI
    global LB1, LB2, ENTR1, ENTR2, butto1
    root = Tk()
    root.title("Emote Generator")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root.iconbitmap(r'' + dir_path + '\eg.ico')

    # create menubar at top of gui
    menubar = Menu(root)
    menubar.add_command(label="Close Application", command=lambda: root.destroy())
    root.config(menu=menubar)

    # first label and entry box
    LB1 = Label(root, text="Emote Prefix", font=('Arial', 21))
    ENTR1 = Entry(root, bd=1, text="regional_indicator_#")
    ENTR1.insert(0, "regional_indicator_#")

    # second label and entry box
    LB2 = Label(root, text="Message to be formatted", font=('Arial', 20))
    ENTR2 = Text(root, width=31, height=10)
    startText = "use # to specify the letter location in a prefix, enter the message here. emotes are case sensitive."
    ENTR2.insert("1.0", startText)

    # buttons to convert entry text to upper or lower
    butto2 = Button(root, text="Make Text Uppercase", font=('Arial', 14),
                    command=lambda: upperbox(ENTR2))
    butto3 = Button(root, text="Make Text Lowercase", font=('Arial', 14),
                    command=lambda: lowerbox(ENTR2))

    # final button that generates the emotes
    butto1 = Button(root, text="Output text", font=('Arial', 20),
                    command=lambda: genEmotes(LB1, LB2, ENTR1, ENTR2, butto1))

    # all elements packed into gui grid
    LB1.grid(row=1, column=0, columnspan=3)
    ENTR1.grid(row=2, column=0, columnspan=3)
    LB2.grid(row=3, column=0, columnspan=3)
    ENTR2.grid(row=4, column=0, columnspan=3)
    butto2.grid(row=5, column=0)
    butto3.grid(row=5, column=2)
    butto1.grid(row=6, column=0, columnspan=3)

    root.mainloop()


main()
