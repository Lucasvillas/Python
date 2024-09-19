#estou fazendo o codigo sem if como forma de desafio pessoal
turma = ('André', 'Fernanda', 'Luiz')
nome = input('Digite um nome: ')
resposta = ['Não exite na tupla', 'Existe na tupla']
x = False
i = 0
while not x and i < len(turma):
    x = bool(nome == turma[i])
    i+=1
print(f'{nome} {resposta[x]}')