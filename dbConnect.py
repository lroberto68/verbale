import sqlite3
from tkinter import messagebox

class DbConnect():

    def __init__(self, pathDb) -> None:

        self.__db = pathDb
        

    def ApriConnessione(self):
        
        try:
            
            self.__connection = sqlite3.connect(self.__db)
            print ("connessione aperta")
            self.__cursor = self.__connection.cursor()
        
        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {e}")
            print ("Connessione non aperta")

    def ChiudiConnessione(self):

        self.__connection.close()
        print ("Connessione chiusa")

    def LeggiVersione(self):
        
        try:

            query = "SELECT sqlite_versdion()"
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            print (f"Versione database: {result}")

        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")

    def CreaTabelle(self):

        try:
            pathScript = "data/verbaliesql"
            with open( pathScript, "r") as sqlFile:
                sqlScript = sqlFile.read()

            self.__cursor.executescript(sqlScript)
             
        except FileNotFoundError as e:
            print (f"Il file {pathScript} non è stato trovato")
            messagebox.showerror(title="ERRORE", message=f"Il file {pathScript} non è stato trovato")

        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {sqlite3.Error}")