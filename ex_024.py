cidade = str(input('Qual a sua cidade: ')).strip()
cidade2 = cidade.lower()
santo = (cidade2[:5] == 'santo')
print(f'começa com santo:{santo}')