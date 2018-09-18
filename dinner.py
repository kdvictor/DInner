import tkinter

class Dinner:
    def __init__(self, master):
        self.master = master
        self.mainfram = tkinter.Frame(self.master, bg = 'darkcyan')
        self.mainfram.pack(fill = tkinter.BOTH, expand = True)

        self.BuildGride()
        self.BuildBanner()
        self.BuildTimer()
        self.BuildButton()


    def BuildGride(self):
        self.mainfram.columnconfigure(0, weight = 1)
        self.mainfram.rowconfigure(0, weight = 0)
        self.mainfram.rowconfigure(1, weight = 1)
        self.mainfram.rowconfigure(2, weight = 0)

    def BuildBanner(self):
        banner = tkinter.Label(self.mainfram,
                 bg = 'darkcyan', text = '永远的TA', fg = 'white', font = ('楷体', 24))
        banner.grid(row = 0, column = 0, sticky = 'ew', padx = 0, pady = 0)

    def BuildTimer(self):
        buildFrame = tkinter.Frame(self.mainfram)
        buildFrame.grid(row = 1, column =0, sticky = 'nsew', padx = 0, pady = 0)

        buildFrame.columnconfigure(0, weight = 1)
        buildFrame.columnconfigure(1, weight = 1)
        buildFrame.columnconfigure(2, weight = 1)
        buildFrame.columnconfigure(3, weight = 1)
        buildFrame.columnconfigure(4, weight = 1)
        buildFrame.rowconfigure(0, weight = 1)
        buildFrame.rowconfigure(1, weight = 1)
        buildFrame.rowconfigure(2, weight = 1)
        buildFrame.rowconfigure(3, weight = 1)
        buildFrame.rowconfigure(4, weight = 1)
        buildFrame.rowconfigure(5, weight = 1)
        buildFrame.rowconfigure(6, weight = 1)

        self.monday = tkinter.Label(buildFrame, text = '星期一', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.monday.grid(row = 0, column = 1, sticky = 'nsew')

        self.tuesday = tkinter.Label(buildFrame, text = '星期二', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.tuesday.grid(row = 1, column = 1, sticky = 'nsew')

        self.wednesday = tkinter.Label(buildFrame, text = '星期三', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.wednesday.grid(row = 2, column = 1, sticky = 'nsew')

        self.thursday = tkinter.Label(buildFrame, text = '星期四', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.thursday.grid(row = 3, column = 1, sticky = 'nsew')

        self.friday = tkinter.Label(buildFrame, text = '星期五', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.friday.grid(row = 4, column = 1, sticky = 'nsew')

        self.satuaday = tkinter.Label(buildFrame, text = '星期六', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.satuaday.grid(row = 5, column = 1, sticky = 'nsew')

        self.sunday = tkinter.Label(buildFrame, text = '星期天', bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.sunday.grid(row = 6, column = 1, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 0, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 1, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 2, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 3, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 4, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 5, column = 3, sticky = 'nsew')

        self.IsMonday = tkinter.Checkbutton(buildFrame)
        self.IsMonday.grid(row = 6, column = 3, sticky = 'nsew')

    def BuildButton(self):
        button = tkinter.Button(self.mainfram, text = '确定')
        button.grid(row = 2, column = 4, sticky = 'ew')


if __name__ == '__main__':
    root = tkinter.Tk()
    Dinner(root)
    root.mainloop()

