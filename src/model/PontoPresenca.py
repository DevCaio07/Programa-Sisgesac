from abc import ABC, abstractmethod

class ponto_presenca: 
    def __init__(self, idGesac, upload, download, beam):
        self.idGesac = idGesac
        self.upload = upload
        self.download = download
        self.beam = beam


    def consultar(self): 
        return{

            "idGesac": self.idGesac,
            "Upload:": self.upload, 
            "Download": self.download,
            "Beam": self.beam
        }    

    @abstractmethod
    def cadastrar(self, bd):
        pass

    #O que aconteceu aqui? 
    #``