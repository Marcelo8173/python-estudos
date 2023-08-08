nome = input('qual é seu nome? ')
idade = input('qual é a sua idade? ')

print(nome, idade)
print(type(nome), type(idade))
print(f'O nome é {nome} e a idade é {idade}')

num1 = int(input('numero 1 '))
num2 = int(input('numero 2 '))


print('a soma dos números {num1} e {num2} é: {soma} '.format(num1, num2, soma=num1 + num2))