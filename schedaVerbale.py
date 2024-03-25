

class Scheda():

    def __init__(self, codice, descrizione, logotipo, matricola, qty, descProv, dataProv, varProv, dataVar, azienda, delegato):
        
        self.__codice = codice
        self.__descrizione = descrizione
        self.__logotipo = logotipo
        self.__matricola = matricola
        self.__qty = qty
        if varProv == "":
            self.__provvedimento = f"{descProv} del {dataProv}"
        else:
            self.__provvedimento = f"{descProv} del {dataProv} Var. {varProv} del {dataVar}"
        self.__azienda = azienda
        self.__delegato = delegato

    @property
    def codice(self):
        return self.__codice
    
    @property
    def descrizione(self):
        return self.__descrizione
    
    @property
    def logotipo(self):
        return self.__logotipo

    @property
    def matricola(self):
        return self.__matricola

    @property
    def qty(self):
        return self.__qty

    @property
    def provvedimento(self):
        return self.__provvedimento

    @property
    def azienda(self):
        return self.__azienda

    @property
    def delegato(self):
        return self.__delegato