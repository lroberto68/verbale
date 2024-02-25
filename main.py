from verbPdf import VerbPdf
from schedaVerbale import Scheda
from datetime import datetime as dt 
import csv

if __name__ == "__main__":
    
    with open(file='data/elenco.csv', mode='r') as f:
        reader = csv.reader(f)
        modelli = []
        for d in reader:
            modelli.append(Scheda(d[0],d[1], d[2], int(d[3]), int(d[4]), d[5], d[6], d[7]))

    pdf = VerbPdf(scheda=modelli, data=dt.now())