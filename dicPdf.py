from fpdf import FPDF, XPos, YPos
from schedaVerbale import Scheda
from tkinter import messagebox

class DicPdf(FPDF):
    
    def __init__(self, scheda:Scheda, data):

        #chiama il super costruttore per configurare orientation, unit e format pagina
        super().__init__(orientation='P', unit='mm', format='A5')

        self.__scheda = scheda
        self.__data = data