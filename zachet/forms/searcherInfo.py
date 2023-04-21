
from Zachet import funcs
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Zachet.forms.review import review
from Zachet.forms.viewReview import viewReview

class searcher(tk.Tk):
    def __init__(self,info ):
        super().__init__()
        frame = ttk.Frame(self)
        self.info=info
        self.title(f"Информация по {info[1]} ")
        self.geometry('400x400')
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

        table = ttk.Treeview(frame,show="headings", selectmode="browse")
        table.grid(row=0,column=0)

        xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL, command=table.xview)
        xscrollbar.grid(row=2, column=0,sticky=EW)
        table.configure(xscrollcommand=xscrollbar.set)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)


        sql=f"SELECT * FROM Products where FMID = '{info[0]}' "
        data = funcs.getTables(sql)
        data2 = funcs.getTables("select fmid,avg(rate) as rating from Reviews group by fmid ;")
        data2["FMID"] = data["FMID"].astype(int)
        df = data.merge(data2, on="FMID", how='left')
        rows = df.values
        headings = list(df.columns)
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))
        ttk.Button(frame, text="Просмотреть отзывы", command=self.viewReview).grid(row=3, column=0)
        ttk.Button(frame, text="Оставить отзыв", command=self.addRewiew).grid(row=4, column=0)
        frame.pack()

    def addRewiew(self):
        rev = review(self.info[0])
        self.destroy()
        pass

    def viewReview(self):
        vrev = viewReview(self.info[0])
        self.destroy()
        pass