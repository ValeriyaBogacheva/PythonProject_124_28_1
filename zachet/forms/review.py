
from Zachet import funcs
from tkinter import *
import tkinter as tk
from tkinter import ttk

class review(tk.Tk):
    def __init__(self,info):
        super().__init__()
        self.info=info
        frame = ttk.Frame(self)
        self.title(f"Информация по {info} ")
        self.geometry('400x600')
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

        ttk.Label(frame,text="Ваше имя: ").grid(row=0,column=0)
        ttk.Label(frame,text="Ваша Фамилия: ").grid(row=1,column=0)
        ttk.Label(frame,text="Отзыв: ").grid(row=2,column=0)
        ttk.Label(frame,text="Рейтинг: ").grid(row=3,column=0)

        self.entryName = Entry(frame)
        self.entryLastName = Entry(frame)
        self.comment = Entry(frame)

        OPTIONS=['0','1','2','3','4','5']
        self.variable = StringVar(frame)
        self.variable.set(OPTIONS[1])
        rating = ttk.OptionMenu(frame,self.variable,*OPTIONS)

        self.entryName.grid(row=0,column=1)
        self.entryLastName.grid(row=1,column=1)
        self.comment.grid(row=2,column=1)
        rating.grid(row=3,column=1)

        ttk.Button(frame, text="Сохранить", command=self.saveInfo).grid(row=4, column=0,columnspan=2)

        frame.pack()

    def saveInfo(self):
        print("TrySave")
        if(self.entryName.get() == ""):
            return
        if(self.entryLastName.get() == ""):
            return
        print("SQL")
        sql = f"INSERT INTO Reviews values('{self.info}','{self.entryName.get()}','{self.entryLastName.get()}'," \
              f"'{self.comment.get()}','{self.variable.get()}');"
        funcs.setTables(sql)
        pass