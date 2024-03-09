from fpdf import FPDF, XPos, YPos
from schedaVerbale import Scheda
from tkinter import messagebox

class VerbPdf(FPDF):

    def __init__(self, scheda:Scheda, data):
        
        #chiama il super costruttore per configurare orientation, unit e format pagina
        super().__init__(orientation = "P", unit = "mm", format= "A4")
        
        #acquisice elenco modelli da inserire nel verbale
        self.__scheda = scheda

        self.__data = data
        
        #imposta un font unicode
        self.add_font("dejavu-serif", style="", fname='font/DejaVuSerif.ttf')
        self.add_font("dejavu-serif", style="B", fname='font/DejaVuSerif-Bold.ttf')
        self.set_font("dejavu-serif", size=12)
        
        #imposta i margini pagina a 18 mm
        self.set_left_margin(18)
        
        #chiama metodo privato per generare le pagine del verbale
        self.__crea_pagine()

    def header(self) -> None:
        
        #chiama il metodo privato per scrivere la stessa intestazione per ogni pagina
        self.__header_layout()

    #metodo privato per creare la tabella in ogni pagina
    def __crea_tabella(self, matr_i, matr_f, logotipo):

        #configura font size per contenuto tabella
        self.set_font_size(8)

        #inserisce riga intestazione per ciascuna tabella / pagina        
        intestazione = [[13, 5, "N. ord/"], [23, 5, "N. ro Matr. /"], [17,5, "N. riord./"], [6, 5, ""], [22, 5, "N. ro causali"], [9, 5, ""], 
                        [13, 5, "N. ord/"], [23, 5, "N. ro Matr. /"], [17,5, "N. riord./"], [6, 5, ""], [22, 5, "N. ro causali"]]
       
        self.set_font(style="B")
        self.set_line_width(0.50)
        for i in intestazione:
            w = i[0]
            h = i[1]
            t = i[2]
            self.cell(w=w, h=h, text=t, border=True)
        self.set_y(self.get_y() + 5)
        self.set_font(style="")
        self.set_line_width(0)

        #memorizza posizione inizio tabella di ogni pagina
        xPos = self.get_x()
        yPos = self.get_y()
    
        #inserisce sottassieme matricole nella tabella
        for m in range(matr_i, matr_f +1):
            
            if (m - matr_i) == 25:
                #salta a tabella di destra per il secondo lotto da 25 matricole
                self.set_xy(xPos + 90.0, yPos)
                co = "\t"
            self.cell(w=13, h=5, border=True, text=str(m - matr_i +1), align="R")
            self.cell(w=23, h=5, border=True, text=f"{logotipo} {str(m).zfill(6)}")
            #inserisce celle colonne vuote
            self.cell(w=17, h=5, border=True, text="")
            self.cell(w=6, h=5, border=True, text="")
            self.cell(w=22, h=5, border=True, text="")
            self.cell(w=9, h=5, border=False, text="", new_x=XPos.LEFT, new_y=YPos.NEXT)
            #posizione cursore per nuova riga
            self.set_x(self.get_x() - 81)
            
        #inserisce celle vuote nella tabella, nel caso che il numero delle matricole sia inferiore a 50
        resto =50 - (matr_f - matr_i + 1)
        for m in range(matr_f - matr_i + 1, resto + matr_f - matr_i + 1,):
          
            if m == 25:
                #salta a tabella di destra per il secondo lotto da 25 celle vuote
                self.set_xy(xPos + 90.0, yPos)
            
            self.cell(w=13, h=5, border=True, text=str(m), align="R")
            self.cell(w=23, h=5, border=True, text="")
            #inserisce celle colonne vuote
            self.cell(w=17, h=5, border=True, text="")
            self.cell(w=6, h=5, border=True, text="")
            self.cell(w=22, h=5, border=True, text="")
            self.cell(w=9, h=5, border=False, text="", new_x=XPos.LEFT, new_y=YPos.NEXT)
            #posiziona cursore per nuova riga
            self.set_x(self.get_x() - 81)
        
        #incrementa spessore bordo esterno della tabella
        self.set_xy(xPos, self.get_y() - 130)
        self.set_line_width(0.50)
        self.cell(w=171, h=130, text="", border=True)
        self.ln(1)   
        self.set_font_size(12) 
        self.set_line_width(0)

    #metodo privato per generare il verbale completo, in pdf
    def __genera_pdf(self, provvedimento, azienda, descrizione, data, delegato, matr_i, matr_f, logotipo):

        #top pagina
        self.__top_layout(provvedimento=provvedimento, azienda=azienda, descrizione=descrizione)
        
        #tabella centro pagina
        self.__crea_tabella(matr_i= matr_i, matr_f= matr_f, logotipo=logotipo)

        #piede pagina
        self.set_y(-65)
        self.__footer_layout(data=data, delegato=delegato)

    #metodo privato per aggiungere le pagine per ogni modello, in riferimento alla relativa qty matricole
    def __crea_pagine(self):

        #itera la lista modelli da verbalizzare
        for v in self.__scheda:
            matr_f = v.matricola -1
            n= int(v.qty / 50)
            n_pagine = n + 1 if v.qty % 50 != 0 else n

            #aggiunge le pagine per ciascun modello, rilevando la matricola iniziale e finale per ogni tabella / pagina
            for pag in range(1, n_pagine + 1):
                self.add_page()
                if pag < n_pagine:
                    #per tabella/pagina completa di 50 matricole
                    matr_i = v.matricola + 50 * (pag -1)
                    matr_f = matr_i + 49
                else:
                    #per tabella/pagina con qty matricola inferiore a 50
                    matr_i = matr_f + 1
                    matr_f = v.matricola + v.qty - 1
                #chiama metodo privato per generare pdf del verbale
                self.__genera_pdf(provvedimento=v.provvedimento, azienda=v.azienda, descrizione=v.descrizione,\
                             data=self.__data, delegato=v.delegato, matr_i=matr_i, matr_f=matr_f, logotipo=v.logotipo)
        self.__save_pdf(data=self.__data)        
   
    #metodo privato per top pagina    
    def __top_layout(self,provvedimento, azienda, descrizione):
        mes1 = f"Gli apparecchi misuratori fiscali, di cui all' elenco, qui di seguito riportato, presentati al controllo di conformità presentano la stessa qualità, sono stati fabbricati nelle stesse condizioni con gli stessi componenti e sostanzialmente nello stesso periodo di tempo e sono conformi al modello approvato e depositato presso il Ministero delle Finanze. **A.E.E.: {provvedimento}**"
        mes2 = f"DICHIARAZIONE DI RESPONSABILITA' DELLA SOC. {azienda}"
        mes5 = f"ELENCO DEGLI AMF DA SOTTOPORRE AL CONTROLLO DI CONFORMITA'\nMod.: {descrizione}"

        self.set_font(size=12, style="B")
        self.cell(w=75, h=8, txt=mes2, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font(size=12, style="")
        self.multi_cell(w=175, h=5, txt=mes1, align="J", markdown=True, new_x =XPos.LMARGIN, new_y = YPos.NEXT)
        self.ln(1)
        self.set_font(size=12, style="B")
        self.set_char_spacing(-1.5)
        self.multi_cell(w=175, h=5, text=mes5, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT )
        self.set_char_spacing(0)
        self.set_font(size=10, style="")
        self.ln(2)

    #metodo privato per layout header pdf
    def  __header_layout(self):

        self.set_font(size=26, style="B")
        self.set_line_width(0.75)
        self.cell(w=95, h=30, txt="DITRON S.R.L.", border=True, align="C", new_x=XPos.RIGHT)
        self.set_font(size=13, style="B")
        self.set_fill_color(192, 192, 192)
        self.cell(w=80, h=6, txt="SISTEMA DI QUALITA'", fill=True, border=True, align="C", new_y=YPos.NEXT, new_x = XPos.LEFT)
        self.cell(w=80, h=18, txt="Mod. 01 QAS-IO-06", border=True, align="C", new_y=YPos.NEXT, new_x=XPos.LEFT)
        self.set_font(size=10)
        self.cell(w=80, h=6, txt="Foglio 1 di 1", border=True, align="C", new_y=YPos.NEXT, new_x=XPos.LMARGIN)
        self.ln(2)  
        self.set_font(size=12, style="")      
        self.cell(w=110, h=8, txt="All. \"A\"", align="L")
        self.cell(w=65, h=8, text="PAGINA [  ]", align="C", new_y=YPos.NEXT, new_x=XPos.LMARGIN)

    #metodo privato per layout footer pdf
    def __footer_layout(self, data, delegato):
        mes1 = f"L' elenco segue alla pag. successiva per AMF superiori a N° 50.\
            \n\nSugli AMF segnati con {chr(945)} sono stati effettuati i controlli tipo A\
            \nSugli AMF segnati con {chr(946)} sono stati effettuati i controlli tipo B\
            \nSugli AMF segnati con {chr(947)} sono stati effettuati i controlli tipo C1-C2/C3"
        mes2 = f"VISTO il presente elenco fa parte integrante del verbale N°           del {data.strftime('%d / %m / %Y')}      "
        mes3 = f"Il delegato della Società \n{delegato}"
        self.set_font_size(10)
        self.multi_cell(w=175, h=5, text=mes1, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        self.cell(w=108, h=5, text=mes2, align="L")
        xPos = self.get_x()
        yPos = self.get_y()
        self.line(xPos, yPos+4, xPos+11, yPos+4)
        self.line(xPos+18, yPos+4, xPos+45, yPos+4)
        self.ln(8)
        self.multi_cell(w=150, h=5, text=mes3, align="R")
        self.line(xPos-5, yPos+20, xPos+45, yPos+20)

    #metodo privato per salvataggio pdf completo e finito              
    def __save_pdf(self, data):

        try:

            nomeFile = f"verbale_{data.strftime('%d_%m_%Y-%H_%M')}.pdf"
            self.output(f"output/{nomeFile}")

        except FileNotFoundError as e:
            print (f"errore: {e.strerror}: {e.filename}")
            messagebox.showerror(title="ERRORE", message=f"errore: {e.strerror}: {e.filename}")