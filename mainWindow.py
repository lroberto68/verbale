from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from dbConnect import DbConnect as db
from schedaVerbale import Scheda
from datetime import datetime as dt 
from verbPdf import VerbPdf

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.__layout3()
        self.__dtB = db('data/verbali.db')
        
    
    def __layout(self):

        self.title("Verbali")
        self.geometry("800x500")

        ttk.Style().configure("frame1.TFrame", background="green")

        self.frame1 = ttk.Frame(self, width=400, height=500, style="frame1.TFrame")
        
        inputVal = tk.IntVar()
        self.entry1 = ttk.Entry(self.frame1, textvariable=inputVal)
        self.entry1.pack(padx=10, pady=10, side="left")
        
        outputVal = tk.StringVar()
        self.label1 = ttk.Label(self.frame1, textvariable=outputVal, background="red")
        self.label1.pack(side="left")

        self.frame1.pack(side="left")

        self.frame2 = ttk.Frame(self)
        self.frame2.pack(side="right")

        self.button1 = ttk.Button(self.frame2, text="Ok",command= lambda: outputVal.set(inputVal.get()))
        self.button1.pack(padx=10, side="top")

    def __layout2(self):
        
        #window
        self.title("Windows & Widgets")
        self.geometry("800x500")
        
        #ttk label
        self.label1 = ttk.Label(master=self, text="This is a test")
        self.label1.pack()
        
        #tk text
        self.text1 = tk.Text(master=self)
        self.text1.pack(pady=10, padx=10)

        #ttk entry
        self.entry1 = ttk.Entry(master=self)
        self.entry1.pack(pady=10)

        #ttk button
        self.button1 = ttk.Button(master=self, text="A Button", command=self.__button1Func)
        self.button1.pack()

    def __layout3(self):

        #window
        self.title("Getting and setting widgets")
        self.geometry("800x500")

        #widgets
        self.label1 = ttk.Label(master=self, text='Some text')
        self.label1.pack()

        self.entry1 = ttk.Entry(master=self)
        self.entry1.pack()
        self.entry1.focus()

        self.entry2 = ttk.Entry(master=self)
        self.entry2.pack()

        self.button1 = ttk.Button(master=self, text='The Button', command=self.__button1Func1)
        self.button1.pack()

        self.button2 = ttk.Button(master=self, text='Another Button', command=self.__button2Func1)
        self.button2.pack()

    def __button1Func(self):
        print("A Button is pressed")

    def __button1Func1(self):
        print(self.entry1.get())
        self.label1['text'] = self.entry1.get()
        self.label1['background'] = 'cyan'
        self.entry1.focus()
        self.button1['state'] = 'disabled'

    def __button2Func1(self):

        self.__modelli = []
        self.label1['text'] = 'some text'
        self.button1['state'] = 'enabled'
        self.__dtB.ApriConnessione()
        dati, number = self.__dtB.SelectModelli(self.entry1.get())
        for r in dati:
            self.__modelli.append(Scheda(r[0],r[1], r[2], int(r[3]) + 1, int(self.entry2.get()), r[4], r[5], r[6], r[7], r[8], f"{r[9]} {r[10]}"))
            self.__dtB.InserScheda((r[13], int(r[3]) + 1, int(r[3]) + int(self.entry2.get()), r[14], dt.now()))
            self.__dtB.UpdateMatricola((int(r[3]) + int(self.entry2.get()), r[15]))
        if number > 0:
            pdf = VerbPdf(scheda=self.__modelli, data=dt.now())
        else:
            print ("Verbale non creato")
        self.__dtB.ChiudiConnessione()
        