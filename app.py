from tkinter import *
from tkinter import ttk
import tkinter, random, pyesave

save = pyesave.newSave("Win10", "getRandomProject", "items", "json")
if not pyesave.doesSaveExist("getRandomProject", "items", "json"):
    save.createSave({})
save.loadSave()

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.pack(fill=BOTH, expand=1)
        addButton = Button(self, text="Add", command=self.clickAddButton)
        addButton.grid(row=0, column=0, pady=2, padx=2)
        removeButton = Button(self, text="Remove", command=self.clickRemButton)
        removeButton.grid(row=3, column=2, pady=2, padx=2)
        randomButton = Button(self, text="Random", command=self.clickRandButton)
        randomButton.grid(row=3, column=1, pady=2, padx=2)
        label = ttk.Label(self, text = "Enter New Item")
        label.grid(column = 1, row = 0)
        labelDes = ttk.Label(self, text = "Enter New Des")
        labelDes.grid(column = 1, row = 1)
        global name
        name = tkinter.StringVar()
        nameEntered = ttk.Entry(self, width = 15, textvariable = name)
        nameEntered.grid(column = 2, row = 0)
        global nameDes
        nameDes = tkinter.StringVar()
        nameDesEntered = ttk.Entry(self, width = 15, textvariable = nameDes)
        nameDesEntered.grid(column = 2, row = 1)
        global item
        item = ttk.Label(self, text = "Item")
        item.grid(column = 1, row = 2)
        global itemDes
        itemDes = ttk.Label(self, text = "Description")
        itemDes.grid(column = 2, row = 2)

    def clickAddButton(self):
        save.changeData({name.get(): nameDes.get()})

    def clickRemButton(self):
        save.removeData({name.get(): nameDes.get()})

    def clickRandButton(self):
        x = random.choice(list(save.data.keys()))
        item.configure(text = x)
        itemDes.configure(text = save.data[x])

root = Tk()
app = Window(root)
root.wm_title("Give me a random project")
root.geometry("320x200")
root.mainloop()