
class SchedaEcr():

    def __init__(self, codice, descrizione, logotipo, matricola, descProv, dataProv, varProv, 
                 dataVar, azienda):
        
        self.__codice = codice
        self.__descrizione = descrizione
        self.__logotipo = logotipo
        self.__matricola = matricola
        
        if varProv == "":
            self.__provvedimento = f"{descProv} del {dataProv}"
        else:
            self.__provvedimento = f"{descProv} del {dataProv} Var. {varProv} del {dataVar}"
        self.__azienda = azienda

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
    def provvedimento(self):
        return self.__provvedimento

    @property
    def azienda(self):
        return self.__azienda

class Scheda(SchedaEcr):

    def __init__(self, codice, descrizione, logotipo, matricola, descProv, dataProv, varProv, 
                 dataVar, azienda, qty, delegato, marchio):
        
        super().__init__(codice, descrizione, logotipo, matricola, descProv, dataProv, varProv, 
                         dataVar, azienda)
        self.__qty = qty
        self.__delegato = delegato
        self.__marchio = marchio
    
    @property
    def qty(self):
        return self.__qty

    @property
    def delegato(self):
        return self.__delegato
    
    @property
    def marchio(self):
        return self.__marchio