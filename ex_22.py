'''nome = str(input('Qual é seu nome: ')).strip()
nome1 = nome.replace(" ", "")
tamanho = (len(nome1))
nome2 = nome.split()
tamanho2 = (len(nome2[0]))
print(f'Minuscula:{nome.lower()}')
print(f'Maiuscula:{nome.upper()}')
print(f'Tem ao todo {tamanho} letras')
print(f'o primeiro nome tem {tamanho2} letras')'''


nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {(len(nome) - nome.count(" ")}')
