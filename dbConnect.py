import sqlite3
from tkinter import messagebox
from schedaVerbale import SchedaEcr
import csv

class DbConnect():

    def __init__(self, pathDb) -> None:

        self.__db = pathDb
        
    #Metodo pubblico per aprire la connessione al Db
    def ApriConnessione(self):
        
        try:            
            self.__connection = sqlite3.connect(self.__db)
            print ("connessione aperta")
            self.__cursor = self.__connection.cursor()
            
            #Attiva foreign keys
            self.__connection.execute("PRAGMA foreign_keys = ON")
        
        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {e}")
            print ("Connessione non aperta")

    #Metodo pubblico per la chiusura della connessione al Db
    def ChiudiConnessione(self):

        self.__connection.close()
        print ("Connessione chiusa")

    def LeggiVersione(self):
        
        try:
            query = "SELECT sqlite_version()"
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            print (f"Versione database: {result}")

        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")

    #Metodo pubblico per la creazione delle tabelle ed inserimento dati di default nel Db a mezzo file script
    def CreaTabelle(self):

        try:
            pathScript = "data/verbali_dati.sql"
            with open( pathScript, "r") as sqlFile:
                sqlScript = sqlFile.read()

            self.__cursor.executescript(sqlScript)
             
        except FileNotFoundError as e:
            print (f"Il file {pathScript} non è stato trovato")
            messagebox.showerror(title="ERRORE", message=f"Il file {pathScript} non è stato trovato")

        except sqlite3.Error as e:
            print (f"Abbiamo quest' errore {sqlite3.Error}")

    #Metodo privato per generazione ed inserimento della lista di tuple nella tabella del Db
    def __InserimentoDati(self, pathCsvFile, query):
        
        try:
            with open(file=pathCsvFile, mode="r") as f:
                reader = csv.reader(f)
            
                #Converte in integer il valore che contiene solo cifre numeriche
                output = list(tuple(int(x) if x.isdigit() else x for x in line) for line in reader)
                #Elimina la tupla contenente le intestazioni dalla lista
                output = output[1:]

            print (output)

            self.__cursor.executemany(query, output)
            self.__connection.commit()
        
        except FileNotFoundError:
            messagebox.showerror(title="ERRORE", message=f"file {pathCsvFile} non trovato")

        except sqlite3.Error as e:    
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")
    
    #Metodo pubblico per inserire i dati della tabella Logotipo
    def CaricaLogotipo(self):
        pathCsvFile = "data/logotipo_202403122217.csv"
        query = '''INSERT INTO Logotipo(IdLog, Logotipo, UltimaMatricola, Cifre, CifreSottassieme,  FlagAnno)
                    VALUES (?,?,?,?,?,?)'''
        self.__InserimentoDati(pathCsvFile=pathCsvFile, query=query)

    #Metodo pubblico per inserire i dati della tabella Azienda
    def CaricaAziende(self):
        pathCsvFile = "data/aziende_20240318.csv"
        query = "INSERT INTO Azienda(IdAzi, DescAzienda) VALUES (?, ?)"
        self.__InserimentoDati(pathCsvFile=pathCsvFile, query=query)

    #Metodo pubblico per inserire i dati della tabella Delegato
    def CaricaDelegati(self):
        pathCsvFile = "data/delegati_20240319.csv"
        query = "INSERT INTO Delegato(IdDeleg, Nome, Cognome, IdAzi) VALUES (?, ?, ?, ?)"
        self.__InserimentoDati(pathCsvFile=pathCsvFile, query=query)

    #Metodo pubblico per inserire i dati della tabella Provvedimento
    def CaricaProvvedimenti(self):
        pathCsvFile = "data/provvedimenti_20240319.csv"
        query = "INSERT INTO Provvedimento(IdProv, DescProvvedimento, DataProv, VarProvvedimento, \
            DataVariante, IdAzi) VALUES (?, ?, ?, ?, ?, ?)"
        self.__InserimentoDati(pathCsvFile=pathCsvFile, query=query)

    #Metodo pubblico per inserire i dati della tabella Ecr
    def CaricaEcr(self):
        pathCsvFile = "data/list_ecr_202403122223.csv"
        query ="INSERT INTO Ecr(IdEcr, CodEcr, DescEcr, IdLogotipo, \
            IdProvv, StatusRec) VALUES (?, ?, ?, ?, ?, ?)"
        self.__InserimentoDati(pathCsvFile=pathCsvFile, query=query)

    #Metodo privato per eseguire query al database
    def __SelectQuery(self, query):
        try:        
            dati =self.__connection.execute(query)
            number = len(self.__connection.execute(query).fetchall())
            #Ritorna il cursore con i record ed il numero di record (zero record che il cursore è vuoto)
            return dati, number
        
        except sqlite3.Error as e:    
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")

    #Metodo pubblico per generare lista record dei modelli da verbalizzare
    def SelectModelli(self, codEcr):
        query = f'''SELECT Ecr.CodEcr,
                Ecr.DescEcr,
                Logotipo.Logotipo,
                Logotipo.UltimaMatricola,
                Provvedimento.DescProvvedimento,
                Provvedimento.DataProv,
                Provvedimento.VarProvvedimento,
                Provvedimento.DataVariante,
                Azienda.DescAzienda,
                Delegato.Nome,
                Delegato.Cognome,
                strftime("%d-%m-%Y", date('now', 'localtime')) AS Data,
                time('now', 'localtime') AS Time,
                Ecr.IdEcr,
                Delegato.IdDeleg,
                Logotipo.IdLog,
                Delegato.Marchio
            FROM Ecr,
                Logotipo,
                Provvedimento,
                Azienda,
                Delegato
            WHERE Ecr.CodEcr LIKE '{codEcr}' AND 
                Ecr.IdLogotipo = Logotipo.IdLog AND
                Ecr.IdProvv = Provvedimento.IdProv AND 
                Azienda.IdAzi = Provvedimento.IdAzi AND 
                Delegato.IdAzi = Azienda.IdAzi;'''
            
        dati, number  = self.__SelectQuery(query)
        return dati, number
    
    
       
    #Metodo pubblico per ricerca modelli
    """ def CercaModelli(self, codEcr):
        query = f''' SELECT Ecr.CodEcr,
                Ecr.DescEcr,
                Logotipo.Logotipo,
                Logotipo.UltimaMatricola,
                Provvedimento.DescProvvedimento,
                Provvedimento.DataProv,
                Provvedimento.VarProvvedimento,
                Provvedimento.DataVariante,
                Azienda.DescAzienda
            FROM Ecr,
                Logotipo,
                Provvedimento,
                Azienda
            WHERE Ecr.CodEcr LIKE '%{codEcr}%' AND 
                Ecr.IdLogotipo = Logotipo.IdLog AND
                Ecr.IdProvv = Provvedimento.IdProv AND 
                Azienda.IdAzi = Provvedimento.IdAzi;'''
        
        dati, number = self.__SelectQuery(query)
        return dati, number """

    def CercaModelli(self, codEcr):
        query = f''' SELECT Ecr.CodEcr,
                Ecr.DescEcr,
                Logotipo.Logotipo,
                Logotipo.UltimaMatricola,
                Provvedimento.DescProvvedimento,
                Provvedimento.DataProv,
                Provvedimento.VarProvvedimento,
                Provvedimento.DataVariante,
                Azienda.DescAzienda
            FROM Ecr,
                Logotipo,
                Provvedimento,
                Azienda
            WHERE Ecr.CodEcr LIKE '%{codEcr}%' AND 
                Ecr.IdLogotipo = Logotipo.IdLog AND
                Ecr.IdProvv = Provvedimento.IdProv AND 
                Azienda.IdAzi = Provvedimento.IdAzi;'''
        
        dati, number = self.__SelectQuery(query)
        schedes = []
        for d in dati:
            schedes.append(SchedaEcr(codice=d[0], descrizione=d[1], 
                                     logotipo=d[2], matricola=d[3], 
                                     descProv=d[4], dataProv=d[5], varProv=d[6],
                                     dataVar=d[7], azienda=d[8]))
        return schedes

    #Metodo pubblico per inserire record dei modelli verbalizzati nella tabella Scheda
    def InserScheda (self, task):
        try:

            query = '''
                    INSERT INTO Scheda(IdEcr, PriMatricola, SecMatricola, IdDeleg, Data) 
                    VALUES (?, ?, ?, ?, ?)
                    '''
            self.__cursor.execute(query, task)
            self.__connection.commit()

        except sqlite3.Error as e:    
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")     

    #Metodo pubblico per aggiornare il record della tabella Logotipo
    def UpdateMatricola (self, task):
        try:
    
            query = '''
                    UPDATE Logotipo
                    SET 
                        UltimaMatricola = ?
                    WHERE IdLog = ?;'''
            
            self.__cursor.execute(query, task)
            self.__connection.commit()

        except sqlite3.Error as e:    
            messagebox.showerror(title="ERRORE", message=f"Abbiamo quest' errore {e} - {e.sqlite_errorcode}")