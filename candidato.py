class Candidato:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.anterior = None
        self.posterior = None
    
    def __str__(self):
        return '[%s:%d]' % (self.nome, self.nota)