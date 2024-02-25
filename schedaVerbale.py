

class Scheda():

    def __init__(self, codice, descrizione, logotipo, matricola, qty, provvedimento, azienda, delegato):
        
        self.__codice = codice
        self.__descrizione = descrizione
        self.__logotipo = logotipo
        self.__matricola = matricola
        self.__qty = qty
        self.__provvedimento = provvedimento
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