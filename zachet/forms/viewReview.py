from Zachet import funcs
from tkinter import *
import tkinter as tk
from tkinter import ttk

class viewReview(tk.Tk):
    def __init__(self,info):
        super().__init__()
        frame = ttk.Frame(self)
        self.title(f"Отзывы по {info} ")
        self.geometry('300x300')
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

        self.table = ttk.Treeview(frame, show="headings", selectmode="browse")
        self.table.grid(row=0, column=0)
        xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL, command=self.table.xview)
        xscrollbar.grid(row=2, column=0, sticky=EW)
        self.table.configure(xscrollcommand=xscrollbar.set)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        self.table.config(height=20)

        sql = f"SELECT * FROM Reviews where FMID = '{info}' "
        df = funcs.getTables(sql)
        rows = df.values
        headings = list(df.columns)
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings

        for head in headings:
            self.table.heading(head, text=head, anchor=tk.CENTER)
            self.table.column(head, anchor=tk.CENTER)

        for row in rows:
            self.table.insert('', tk.END, values=tuple(row))

        ttk.Button(frame, text="Удалить", command=self.deleteView).grid(row=3, column=0,columnspan=2)

        frame.pack()

    def deleteView(self):
        i = self.table.focus()
        if(i):
            item = list(self.table.item(i).values())[2]
            sql = f"DELETE FROM Reviews where FMID = '{item[0]}' AND FirstName ='{item[1]}' AND " \
                  f"LastName ='{item[2]}' AND Comment = '{item[3]}' AND rate ='{item[4]}';"
            funcs.setTables(sql)
        self.destroy()
        pass