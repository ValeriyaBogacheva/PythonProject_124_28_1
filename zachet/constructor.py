import numpy as np
import pandas as pd

from Zachet import funcs
from Zachet.forms.searcherInfo import searcher
import math
from tkinter import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Фермерские рынки")
        self.geometry('800x600')
        #self.columnconfigure(0, minsize=1)
        #self.columnconfigure(1, minsize=10)
        #self.columnconfigure(2, minsize=10)
        #self.columnconfigure(3, minsize=10)
        tab_control = ttk.Notebook(self)


        #Вкладки
        self.getTab1(tab_control)
        self.getTab2(tab_control)
        self.getTab3(tab_control)
        self.getTab4(tab_control)



        tab_control.pack(expand=1, fill='both')

        self.mainloop()


    def getTab1(self,tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text='Главная')
        ttk.Label(tab,text='Приложение для работы с данными фермерских рынков.').grid(row=0,column=0)


    def getTab2(self,tab_control):
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Общая база')

        table = ttk.Treeview(tab2, show="headings", selectmode="browse")

        xscrollbar = ttk.Scrollbar(tab2, orient=HORIZONTAL, command=table.xview)
        xscrollbar.grid(row=1, column=0, sticky=EW)
        table.configure(xscrollcommand=xscrollbar.set)
        tab2.grid_columnconfigure(0, weight=1)
        tab2.grid_rowconfigure(0, weight=1)

        table.config(height=20)
        data = funcs.getTables("Select * from Farms")
        data2 = funcs.getTables("select fmid,avg(rate) as rating from Reviews group by fmid ;")
        data2["FMID"]=data["FMID"].astype(int)
        df = data.merge(data2,on="FMID",how='left')
       #[df.values, list(df.columns)]
        rows = df.values
        headings = list(df.columns)
        table["columns"] = headings
        table["displaycolumns"] = headings
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER,command=lambda _col = head:self.sort(table,_col,False))
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        table.grid(column=0, row=0, sticky=NSEW)

    def getTab3(self,tab_control):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text='Поиск')
        tab.rowconfigure(1, weight=15)

        ttk.Label(tab,text="Введите город: ").grid(row=0,column=0,sticky=W)
        self.findEntryCity = Entry(tab)
        self.findEntryCity.grid(row=0, column=0)
        ttk.Label(tab,text="Введите Штат: ").grid(row=1,column=0,sticky=W)
        self.findEntryState = Entry(tab)
        self.findEntryState.grid(row=1, column=0)
        ttk.Label(tab,text="Введите ZIP: ").grid(row=2,column=0,sticky=W)
        self.findEntryZip = Entry(tab)
        self.findEntryZip.grid(row=2, column=0)

        self.tableSearcher = ttk.Treeview(tab, show="headings", selectmode="browse")

        xscrollbar = ttk.Scrollbar(tab, orient=HORIZONTAL, command=self.tableSearcher.xview)
        xscrollbar.grid(row=5, column=0,columnspan=7, sticky=EW)
        self.tableSearcher.configure(xscrollcommand=xscrollbar.set)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(0, weight=1)
        self.tableSearcher.config(height=20)
        self.tableSearcher.grid(column=0, row=4,columnspan=7, sticky=NSEW)
        ttk.Button(tab, text="Поиск", command=lambda: self.search(False,self.tableSearcher)).grid(row=3, column=0,sticky=W)

    def getTab4(self,tab_control):
        tab = ttk.Frame(tab_control)
        tab.rowconfigure(1, weight=15)
        tab_control.add(tab, text='Поиск по координатам')

        ttk.Label(tab, text="Введите x: ").grid(row=0, column=0,sticky=W)
        self.findEntryX = Entry(tab)
        self.findEntryX.grid(row=0, column=0)

        ttk.Label(tab, text="Введите y: ").grid(row=1, column=0,sticky=W)
        self.findEntryY = Entry(tab)
        self.findEntryY.grid(row=1, column=0)

        ttk.Label(tab, text="Введите максимальное расстояние: ").grid(row=2, column=0,sticky=W)
        self.findEntryZ = Entry(tab)
        self.findEntryZ.grid(row=2, column=0)

        tableCoordsSearcher = ttk.Treeview(tab, show="headings", selectmode="browse")

        xscrollbar = ttk.Scrollbar(tab, orient=HORIZONTAL, command=tableCoordsSearcher.xview)
        xscrollbar.grid(row=5, column=0, columnspan=4, sticky=EW)
        tableCoordsSearcher.configure(xscrollcommand=xscrollbar.set)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(0, weight=1)
        tableCoordsSearcher.config(height=20)
        tableCoordsSearcher.grid( row=4,column=0, columnspan=4, sticky=NSEW)
        ttk.Button(tab, text="Поиск", command=lambda:self.search(True,tableCoordsSearcher)).grid(row=3, column=0,sticky=W)


    def search(self,status,tree):
        sql = "Select * from Farms where "
        tree.delete(*tree.get_children())
        if(status == False):

            sqlCity = ""
            sqlState = ""
            sqlZip = ""

            if(self.findEntryCity.get() != ""):
                sqlCity = f"city ='{self.findEntryCity.get()}'"

            if (self.findEntryState.get() != ""):
                sqlState = f"State = '{self.findEntryState.get()}'"

            if(self.findEntryZip.get() != ""):
                sqlZip =  f"zip = '{self.findEntryZip.get()}'"

            if(sqlCity != ""):
                sql = sql + sqlCity

                if(sqlState != ""):
                    sql = sql + " AND " + sqlState

                    if(sqlZip != ""):
                        sql = sql + " AND " + sqlZip

                elif(sqlZip != ""):
                    sql = sql+" AND " + sqlZip

            elif(sqlState !=""):
                sql = sql + sqlState
                if(sqlZip != ""):
                    sql = sql +" AND " + sqlZip
            elif(sqlZip != ""):
                sql = sql + sqlZip
            else:
                return

            data = funcs.getTables(sql)
            data2 = funcs.getTables("select fmid,avg(rate) as rating from Reviews group by fmid ;")
            data2["FMID"] = data["FMID"].astype(int)
            df = data.merge(data2, on="FMID", how='left')
            rows = df.values
            headings = list(df.columns)
            tree.bind('<<TreeviewOpen>>', self.selectSearchTable)
            tree["columns"] = headings
            tree["displaycolumns"] = headings

        else:
            if(self.findEntryY.get() != "" and self.findEntryX.get() != "" and self.findEntryZ.get() != ""):
                try:
                    x = float(self.findEntryX.get())
                    y = float(self.findEntryY.get())
                    z = float(self.findEntryZ.get())
                    sql = "Select * from Coords"
                    data = funcs.getTables(sql).values
                    array=[]
                    for i in data:
                        s = math.sqrt(math.pow(i[1]-x,2) + math.pow(i[2]-y,2))
                        if(s<z):
                            array.append(i)
                    data = np.array(array)
                    data3 = pd.DataFrame(data,columns=["FMID",'x','y','Location'])
                    print(type(data))
                    data = funcs.getTables("select * from Farms")
                    data2 = funcs.getTables("select fmid,avg(rate) as rating from Reviews group by fmid ;")
                    data2["FMID"] = data["FMID"].astype(int)
                    df = data.merge(data3, on="FMID")

                    df = df.merge(data2,on="FMID", how='left')
                    rows = df.values
                    headings = list(df.columns)
                    tree["columns"] = headings
                    tree["displaycolumns"] = headings
                except:
                    print("ERROR")
                    return



        for head in headings:
            tree.heading(head, text=head, anchor=tk.CENTER)
            tree.column(head, anchor=tk.CENTER)

        for row in rows:
            tree.insert('', tk.END, values=tuple(row))


    def sort(self, tree, col, reverse):
        # получаем все значения столбцов в виде отдельного списка
        l = [(tree.set(k, col), k) for k in tree.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index, (_, k) in enumerate(l):
            tree.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        tree.heading(col, command=lambda: self.sort(tree,col, not reverse))

    def selectSearchTable(self,event):
        curitem = self.tableSearcher.focus()
        item = self.tableSearcher.item(curitem)
        listMarket = list(item.values())[2]
        searcherInfo = searcher([listMarket[0],listMarket[1]])










