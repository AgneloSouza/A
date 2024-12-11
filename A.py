from candidato import Candidato
from concurso import Concurso

def main():
	c0 = Candidato('Rui Barbosa',80)
	c1 = Candidato("Machado de Assis",90)
	co = Concurso("Senado Federal")
	co.inscrever(c0)
	co.inscrever(c1)
	co.remove('Rui Barbosa')
	print(co)

main()