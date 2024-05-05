from verbPdf import VerbPdf
from schedaVerbale import Scheda
from datetime import datetime as dt 
from dbConnect import DbConnect as db
from tkinter import messagebox
from mainWindow import MainWindow
import os
import csv

def mainFromFile (pathCsvFile):

    try:
        pathDbFile = 'data/verbali.db'
        flagDbExists = os.path.exists(pathDbFile)
        dtB = db(pathDb=pathDbFile)
        dtB.ApriConnessione()
        dtB.LeggiVersione()
        if not flagDbExists:
             dtB.CreaTabelle()
        else:
            with open(file= pathCsvFile, mode='r') as f:
                reader = csv.reader(f)
                modelli = []
                for d in reader:
                    dati, number = dtB.SelectModelli(d[0])
                    for r in dati:
                        print(r)
                        modelli.append(Scheda(r[0],r[1], r[2], int(r[3]) + 1, r[4], r[5], r[6], r[7], r[8], int(d[1]), f"{r[9]} {r[10]}"))
                        dtB.InserScheda((r[13], int(r[3]) + 1, int(r[3]) + int(d[1]), r[14], dt.now()))
                        dtB.UpdateMatricola((int(r[3]) + int(d[1]), r[15]))

            if len(modelli) > 0:
                pdf = VerbPdf(scheda=modelli, data=dt.now())
            else:
                #Nessun modello individuato e quindi verbale vuoto
                print("Verbale non creato")
        
        dtB.ChiudiConnessione()

    except FileNotFoundError:
            messagebox.showerror(title="ERRORE", message=f"file {pathCsvFile} non trovato")

    except TypeError:
            messagebox.showerror(title="ERRORE", message=f"database {pathDbFile} non trovato")

def mainFromWindows ():
     root = MainWindow()
     root.mainloop()

if __name__ == "__main__":
    mainFromFile('data/elencoPunz.csv')
    #mainFromWindows()
    