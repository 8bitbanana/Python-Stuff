import os, psutil
from tkinter import *

programs = [
    ["Steam","C:/Program Files (x86)/Steam/Steam.exe"],
    ["Discord","C:/Users/8bitb/AppData/Local/Discord/app-0.0.300/Update.exe"],
    ["OneDrive","C:/Users/8bitb/AppData/Local/Microsoft/OneDrive/OneDrive.exe"],
    ["ShareX","C:/Program Files/ShareX/ShareX.exe"],
    ["qBittorrent","C:/Program Files (x86)/qBittorrent/qbittorrent.exe"],
    ["DesktopOK","C:/Users/8bitb/Desktop/DesktopOK/DesktopOK.exe"],
    ["Rainmeter","C:/Program Files/Rainmeter/Rainmeter.exe"],
    ["Sandboxie","C:/Program Files/Sandboxie/SbieCtrl.exe"],
    #["Folding@Home","C:\Program Files (x86)\FAHClient\HideConsole.exe\" \"FAHClient.exe"]
    ]

presets = [
    'none','all', # Presets 1 and 2
        [ # Preset 2 (default)
        "Steam",
        "Discord",
        "OneDrive",
        "ShareX",
        "DesktopOK",
        #"Folding@Home"
        ],
        [ # Preset 3 (light)
        "OneDrive",
        "DesktopOK",
        "Folding@Home"
        ]
    ]


def checkprocess(program):
    program = os.path.split(program)[1]
    return program in (p.name() for p in psutil.process_iter())

class MainApp:
    def __init__(self, master):
        self.statevars=[]
        for x in programs:
            self.statevars.append(IntVar())
        presetvar = IntVar()
        frame = Frame(master)
        frame.pack()
        index = 0
        for x in programs:
            Label(frame, text=x[0]).grid(row=index,column=0)
            Checkbutton(frame, variable=self.statevars[index]).grid(row=index,column=1)
            index+=1
        Button(frame, text="None", command=lambda: self.setpreset(0)).grid(row=index,column=0,sticky="WE")
        Button(frame, text="Full", command=lambda: self.setpreset(1)).grid(row=index,column=1,sticky="WE")
        Button(frame, text="Default", command=lambda: self.setpreset(2)).grid(row=index+1,column=0,sticky="WE",ipadx=15)
        Button(frame, text="Light", command=lambda: self.setpreset(3)).grid(row=index+1,column=1,sticky="WE",ipadx=15)
        Button(frame, text="TRIGGER", command=lambda: self.trigger()).grid(row=index+2,column=0,ipadx=30,columnspan=2,sticky="WE",ipady=10,padx=5,pady=10)
        self.setpreset(2)

    def setpreset(self, preset):
        preset = presets[preset]
        if preset == 'none':
            for x in range(0,len(self.statevars)):
                self.statevars[x].set(0)
        elif preset == 'all':
            for x in range(0,len(self.statevars)):
                self.statevars[x].set(1)
        else:
            for x in range(0, len(self.statevars)):
                trigger = False
                for y in preset:
                    if programs[x][0]==y:
                        trigger = True
                if trigger:
                    self.statevars[x].set(1)
                else:
                    self.statevars[x].set(0)

    def trigger(self):
        index = 0
        for program in programs:
            if self.statevars[index].get() == 1:
                print("launch " + program[1])
                os.startfile(program[1])
            index += 1
        

root = Tk()
app = MainApp(root)
root.mainloop()
