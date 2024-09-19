#fiz sem if e else como um desafio pessoal
número = int(input('insira um número: '))

resultado = ['O número é par', 'O número é impar']

print(resultado[bool(número%2)])