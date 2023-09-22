from tkinter import *


def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Diary(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Diary Main')
        self.master.iconname("Diary")

        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)


        # for relied in [SUNken]:
        #     f = Frame
        #     for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        #         f = Frame(root, borderwidth=2, relief=relief)
        #     Label(f, text=relief, width=10).pack(side=LEFT)
        #     f.pack(side=LEFT, padx=5, pady=5)


if __name__ == '__main__':
    Diary().mainloop()
