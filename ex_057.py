sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print(f'Tente novamente! ')
print(f'Obrigado pela informação {sexo}!')

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')'''