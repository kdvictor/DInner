import tkinter
import os

class Dinner:
    def __init__(self, master):
        self.master = master
        self.mainfram = tkinter.Frame(self.master, bg = 'darkcyan')
        self.mainfram.pack(fill = tkinter.BOTH, expand = True)

        self.timeDic = {"MON":tkinter.IntVar(), "TUE":tkinter.IntVar(), "WED":tkinter.IntVar(),
                        "THU":tkinter.IntVar(), "FRI":tkinter.IntVar(), "SAT":tkinter.IntVar(), "SUN":tkinter.IntVar()}

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
                 bg = 'darkcyan', text = '加班餐', fg = 'white', font = ('楷体', 24))
        banner.grid(row = 0, column = 0, sticky = 'ew', padx = 0, pady = 0)

    def BuildTimer(self):
        buildFrame = tkinter.Frame(self.mainfram)
        buildFrame.grid(row = 1, column =0, sticky = 'nsew', padx = 0, pady = 0)

        buildFrame.columnconfigure(0, weight = 4)
        buildFrame.columnconfigure(1, weight = 2)
        buildFrame.columnconfigure(2, weight = 2)
        buildFrame.columnconfigure(3, weight = 4)
        buildFrame.rowconfigure(0, weight = 1)
        buildFrame.rowconfigure(1, weight = 1)
        buildFrame.rowconfigure(2, weight = 1)
        buildFrame.rowconfigure(3, weight = 1)
        buildFrame.rowconfigure(4, weight = 1)
        buildFrame.rowconfigure(5, weight = 1)
        buildFrame.rowconfigure(6, weight = 1)

        self.lable = tkinter.Label(buildFrame, bg = 'darkcyan')
        self.lable.grid(row = 0, rowspan = 7, column = 0, sticky = 'nesw')

        self.lable = tkinter.Label(buildFrame, bg = 'darkcyan')
        self.lable.grid(row = 0, rowspan = 7, column = 3, sticky = 'nesw')

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

        self.mondyCheck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["MON"])
        self.mondyCheck.select()
        self.mondyCheck.grid(row = 0, column = 2, sticky = 'nsew')

        self.tuesdayCheck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["TUE"])
        self.tuesdayCheck.select()
        self.tuesdayCheck.grid(row = 1, column = 2, sticky = 'nsew')

        self.wednesdayCheck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["WED"])
        self.wednesdayCheck.select()
        self.wednesdayCheck.grid(row = 2, column = 2, sticky = 'nsew')

        self.thursdayCheck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["THU"])
        self.thursdayCheck.select()
        self.thursdayCheck.grid(row = 3, column = 2, sticky = 'nsew')

        self.fridayCheck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["FRI"])
        self.fridayCheck.select()
        self.fridayCheck.grid(row = 4, column = 2, sticky = 'nsew')

        self.satuadayCkeck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["SAT"])
        self.satuadayCkeck.select()
        self.satuadayCkeck.grid(row = 5, column = 2, sticky = 'nsew')

        self.sundayCkeck = tkinter.Checkbutton(buildFrame, bg = 'darkcyan', variable = self.timeDic["SUN"])
        self.sundayCkeck.grid(row = 6, column = 2, sticky = 'nsew')

    def BuildButton(self):
        buildFram = tkinter.Frame(self.mainfram)
        buildFram.grid(row = 2, sticky = 'nesw')

        buildFram.columnconfigure(0, weight = 10)
        buildFram.columnconfigure(1, weight = 2)
        buildFram.columnconfigure(2, weight = 2)
        buildFram.rowconfigure(0, weight = 1)

        self.lable = tkinter.Label(buildFram, text = "如有建议请联系：huan.liu@united-imaging.com",
                                   bg = 'darkcyan', fg = 'white', font = ('楷体', 16))
        self.lable.grid(row = 0, column = 0, sticky = 'nsew')

        button = tkinter.Button(buildFram, text = '确定', command = self.OnPositiveCommandRaised__)
        button.grid(row = 0, column = 1, sticky = 'nsew')

        self.lableNull = tkinter.Label(buildFram, bg = 'darkcyan')
        self.lableNull.grid(row = 0, column = 2, sticky = 'nesw')

    def OnPositiveCommandRaised__(self):
        self.timeString = self.GetTimeString()
        self.creatTaskString = 'SCHTASKS /Create /SC WEEKLY /D ' + self.timeString + ' /ST 11:00 /TN dinner /TR ./runDinner.exe'
        self.file = open('./creatDinnerTask.bat', 'w')
        self.file.truncate()
        self.file.write('SCHTASKS /Delete /TN dinner /F' + '\n')
        self.file.write(self.creatTaskString)
        self.file.close()
        #运行.bat程序
        os.system('D:\Dinner\creatDinnerTask.bat')

    def GetTimeString(self):
        timeString = ''
        for key in self.timeDic.keys():
            if self.timeDic[key].get() == 1:
                timeString += key
                timeString += " "
        return  '\"'+ timeString + '\"'



if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("800x800")
    Dinner(root)
    root.mainloop()

