import tkinter as tk
from tkinter import ttk
from dbConnect import DbConnect as db
from schedaVerbale import Scheda, SchedaEcr
from datetime import datetime as dt 
from verbPdf import VerbPdf

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__test1()
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
        if len(self.__modelli) > 0:
            pdf = VerbPdf(scheda=self.__modelli, data=dt.now())
        else:
            print ("Verbale non creato")
        self.__dtB.ChiudiConnessione()

    def __button3Func1(self):
        print (self.__testo.get())
        self.__testo.set("Button pressed")
        print (f"Valore radio button: {self.__radioVar.get()}")

    def __radioFunc(self):
        print (f"Valore checkbutton: {self.__check3Var.get()}")
        self.__check3Var.set(False)

    def __layout4(self):

        #window
        self.title("Tkinter variables")
        self.geometry("600x400")

        #tkinter variables
        self.__testo = tk.StringVar(value="Start Value")
    
        #widgets
        self.label1 = ttk.Label(master=self, textvariable=self.__testo)
        self.label1.pack()

        self.entry1 = ttk.Entry(master=self, textvariable= self.__testo)
        self.entry1.pack()

        self.button1 = ttk.Button(master=self, text='Button', command=self.__button3Func1)
        self.button1.pack()

        self.__button2String = tk.StringVar(value = "A basic button")
        self.button2 = ttk.Button(master=self, text= 'A button', command=lambda: print(self.__button2String.get()), textvariable=self.__button2String)
        self.button2.pack()

        #self.__check1Value = tk.StringVar(value="1")
        self.__check1Value = tk.BooleanVar(value=True)
        self.check1 = ttk.Checkbutton(master=self, text="Check1", 
                                      command=lambda: print(self.__check1Value.get()), 
                                      variable=self.__check1Value)
        self.check1.pack()

        self.__radioVar = tk.StringVar(value=2)
        self.radio1 = ttk.Radiobutton(master=self, text="Radio1", 
                                        value="Radio 1", variable= self.__radioVar, 
                                        command=lambda: print(self.__radioVar.get()))
        self.radio1.pack()

        self.radio2 = ttk.Radiobutton(master=self, text="Radio2", 
                                      value=2, variable=self.__radioVar,
                                      command=lambda: print(self.__radioVar.get()))
        self.radio2.pack()

        self.__check3Var = tk.BooleanVar(value=True)
        self.check3 = ttk.Checkbutton(master=self, text="Check3", variable= self.__check3Var, command=lambda:print(f"Valore radiobutton: {self.__radio34Var.get()}"))
        self.check3.pack()

        self.__radio34Var = tk.StringVar(value="A")
        self.radio3 = tk.Radiobutton(master=self, text="A", 
                                     value="A", variable=self.__radio34Var,
                                     command= self.__radioFunc)
        

        self.radio4 = tk.Radiobutton(master=self, text="B", 
                                     value="B", variable=self.__radio34Var, 
                                     command=self.__radioFunc)
        self.radio3.pack()
        self.radio4.pack()

        items = ['ice cream', 'pizza', 'broccoli']
        self.__cmbVar = tk.StringVar(value=items[0])
        self.combo = ttk.Combobox(master=self, textvariable=self.__cmbVar)
        self.combo['values'] = items
        self.combo.pack()

        self.combo.bind('<<ComboboxSelected>>', lambda event: print(f"Selected: {self.__cmbVar.get()}"))

        self.button2.bind('<Motion>', lambda event: print(f"x: {event.x} - y: {event.y}"))

    def __layout5(self):
        from random import choice

        #window
        self.title("Treeview test")
        self.geometry("600x400")

        #data
        first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']   
        last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

        #treeview
        self.treeview = ttk.Treeview(master=self, columns=('First', 'Last', 'Email'), show='headings', selectmode='browse')
        self.treeview.heading(column='First', text='First Name')
        self.treeview.heading(column='Last', text='Last Name')
        self.treeview.heading(column='Email', text='Email Adreess')
        self.treeview.pack(fill='both', expand=True)

        #insert data
        for i in range(100):
            first = choice(first_names)
            last = choice(last_names)
            email = f"{first[0]}{last}_{i}@email.com".lower()
            data = (first, last, email)
            self.treeview.insert(parent='', index=0, values=data)

        #event
        def itemSelect(_):
            for i in self.treeview.selection():
                print(self.treeview.item(i))

        def itemDelete(event):
            for id in self.treeview.selection():
                item = self.treeview.item(id)
                self.treeview.delete(id)
                print(f"{item['values']}: DELETED")

        self.treeview.bind('<<TreeviewSelect>>', func= itemSelect)
        self.treeview.bind('<Delete>', itemDelete)

        #listbox
        #self.lstbox = tk.Listbox(master=self)
        #self.lstbox.pack()

    """ def __cercaEcr(self):
        print(f"test {self.__codEcr.get()}")
        for item in self.treeEln.get_children():
            self.treeEln.delete(item)

        self.__dtB.ApriConnessione()
        dati, number = self.__dtB.CercaModelli(codEcr=self.__codEcr.get())
        print (f"Abbiamo trovato: {number} records")
        
        for d in dati:
            u = d[2] + ' ' + str(d[3])
            self.treeEln.insert(parent='', index=0, values=(d[0], d[1], u))
        self.__dtB.ChiudiConnessione() """
    
    def __cercaEcr(self):
        print(f"test {self.__codEcr.get()}")
        for item in self.treeEln.get_children():
            self.treeEln.delete(item)

        self.__dtB.ApriConnessione()
        modelli:SchedaEcr = self.__dtB.CercaModelli(codEcr=self.__codEcr.get())
        print (f"Abbiamo trovato: {len(modelli)} records")
        
        for m in modelli:
            
            self.treeEln.insert(parent='', index=0, 
                                values=(m.codice, m.descrizione, m.logotipo, m.matricola))
        
        self.__dtB.ChiudiConnessione()

    def __test1(self):
        #window
        self.title("Test N°1")
        self.geometry("800x600")

        #tk_variables
        self.__codEcr = tk.StringVar(value="cerca")

        #entry
        self.entryRic = ttk.Entry(master=self, textvariable=self.__codEcr)
        self.entryRic.pack(pady=15)

        #button
        self.btnRic = ttk.Button(master=self, text='Cerca', command= self.__cercaEcr)
        self.btnRic.pack(pady=10)

        #treeview
        self.treeEln = ttk.Treeview(master=self, columns=('Codice', 'Descrizione','Logotipo', 'UltimaMatr'), show='headings', selectmode='browse')
        self.treeEln.heading(column='Codice', text='Codice Ecr')
        self.treeEln.heading(column='Descrizione', text='Descrizione ECR')
        self.treeEln.heading(column='Logotipo', text='Logotipo')
        self.treeEln.heading(column='UltimaMatr', text='Ultima Matricola')
        #self.treeEln.insert(parent='', index=0, values=['LRIDEAL', 'ECR IDEAL', '2CIDE'])
        self.treeEln.pack(pady=10)

    