class Node:
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return "%s" % (self.valor)

n = Node(1)
print(n)