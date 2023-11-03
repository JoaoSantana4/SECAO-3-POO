import json

CAMINHO_ARQUIVO = 'aula08.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 18)
p2 = Pessoa('Luis', 17)
p3 = Pessoa('Luiz', 18)
bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE É O  __main__')
    fazer_dump()