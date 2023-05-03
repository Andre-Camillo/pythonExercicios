from num2words import num2words
num = 276
print(f"{num}\nEM DECIMAL: {num2words(num, lang='pt-br')}.\nEM ORDINAL: {num2words(num, lang='pt-br', to='ordinal')}.")
