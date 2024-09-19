#fiz sem if como forma de desafio pessoal
import random

continuar = True
resultados = {
    ('PEDRA', 'PEDRA'): 'Empate!',
    ('PEDRA', 'PAPEL'): 'Você perdeu!',
    ('PEDRA', 'TESOURA'): 'Você ganhou!',
    ('PAPEL', 'PEDRA'): 'Você ganhou!',
    ('PAPEL', 'PAPEL'): 'Empate!',
    ('PAPEL', 'TESOURA'): 'Você perdeu!',
    ('TESOURA', 'PEDRA'): 'Você perdeu!',
    ('TESOURA', 'PAPEL'): 'Você ganhou!',
    ('TESOURA', 'TESOURA'): 'Empate!'
}

contadores = {
    'Empate!': 'empates',
    'Você ganhou!': 'vitórias',
    'Você perdeu!': 'derrotas'
}
status = {'vitórias': 0, 'derrotas': 0, 'empates': 0}

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']

while(continuar):
    compMove = jogadas[random.randint(0, 2)]
    move = input('escolha entre pedra papel ou tesoura: ').upper()
    resultado = resultados.get((move, compMove), 'Movimento inválido!')
    status[contadores.get(resultado, 'empates')] += 1
    print(resultado)
    resposta = input('se deseja continuar, pressione enter, se não, precione qualquer outra tecla: ')
    continuar = bool(not resposta)
print(status)