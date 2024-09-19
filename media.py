#fiz sem if como forma de desafio pessoal
notas = [6.3, 7.5, 9.2, 5.1, 6.8]
media = 0
acimadamedia = []
for i in range(len(notas)):
    media += notas[i]
    acimadamedia.append(notas[i] * bool(notas[i]>=6))
media/=len(notas)
while 0 in acimadamedia:
    acimadamedia.remove(0)
print(f'A media é: {media}')
print(f'notas acima da media: {acimadamedia}')