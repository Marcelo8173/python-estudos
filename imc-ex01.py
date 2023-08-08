peso = 136
altura = 1.86

imc = peso/(altura ** 2)

print('calculo do imc', imc)

if(imc < 16.0):
    print('Magreza grave')
else:  
    if (imc >= 16.0 and imc <= 17.8):
        print('magreza moderada')
    else: 
        if(imc >= 17.0 and imc <= 25.0):
            print('normal')
        else: 
            if(imc >= 25.0):
                print('Sobrepeso')
print(f'voce tem {peso} quilos e {altura} de altura e o seu imc é: {imc:.2f}')

# f string é usada para interpolar strings `${}` => mesmo conceito
# ele habilita formatação :.2f duas casas decimais apos a ,
        
        
"""
    Usando o format
"""
# tudo python é um obejto
a = 'a'
b = 'b'
c = 1.1
format = 'a={}'.format(a,b,c)

print(format)
msg = 'formatando msg com o format, sua altura é altura={} e o seu peso é peso={}, imc é imc={:.2f}'.format(altura, peso, imc)
print(msg)

# parametro nomeados
msg_nomeda = 'formatando msg com o format e parametros nomeados, sua altura é altura={} e o seu peso é peso={}, imc é imc={value_imc:.2f}'.format(altura, peso, value_imc=imc)
print(msg_nomeda)

