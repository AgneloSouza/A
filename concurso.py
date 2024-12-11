class Concurso:
    def __init__(self, nome):
        self.primeiro_inscrito = None
        self.nome = nome
        self.inscritos = 0
    
    def inscrever(self, candidato):
        if(self.primeiro_inscrito==None):
            self.primeiro_inscrito = candidato
            candidato.posterior = candidato
            candidato.anterior = candidato
        else:
            aux = self.primeiro_inscrito
            while(aux.posterior!=self.primeiro_inscrito):
                aux = aux.posterior
            aux.posterior = candidato
            candidato.anterior = aux
            candidato.posterior = self.primeiro_inscrito
            self.primeiro_inscrito.anterior = candidato
        self.inscritos+=1
    
    def busca(self, nome ):
        if(self.primeiro_inscrito==None):
            return None
        else:
            aux = self.primeiro_inscrito
            while(aux.posterior!=self.primeiro_inscrito and aux.nome!=nome):
                aux = aux.posterior
            if(aux.nome==nome):
                return aux
            else:
                return None
    
    def remove(self, nome):
        if(self.primeiro_inscrito.nome==nome and self.inscritos==1):
            self.primeiro_inscrito = None
            self.inscritos-=1
            return True
        elif(self.primeiro_inscrito.nome==nome):
            aux = self.primeiro_inscrito.anterior
            self.primeiro_inscrito = self.primeiro_inscrito.posterior
            aux = self.primeiro_inscrito
            self.primeiro_inscrito.posterior = self.primeiro_inscrito
            self.inscritos-=1
            return True
        else:
            buscado = self.busca(nome)
            if(buscado==None):
                return False
    
    def __str__(self):
        if(self.primeiro_inscrito==None):return '%s[]' % (self.nome)
        else:
            saida = "%s" % (self.nome)
            aux = self.primeiro_inscrito
            saida+=aux.__str__()
            aux = aux.posterior
            while(aux!=self.primeiro_inscrito):
                saida += aux.__str__()
                aux = aux.posterior
            return saida