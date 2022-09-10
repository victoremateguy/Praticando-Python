frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(junto, inverso)

if junto == inverso:
    print('A frase é um PALINDROMO!')
else:
    print('A frase NÃO é um PALINDROMO!')












#frase2 = frase.replace(' ', '')

