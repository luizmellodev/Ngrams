from nltk.util import ngrams
from collections import Counter
import os


nomearquivo = len(os.listdir('ngrams-results')) +1
num = 1

for folders, files, path in os.walk('resultados-ngramas/'):
    for file in files:
        filename, extension = os.path.splitext(file)
        print(f'{num} --- {folders} --- {filename}.{extension}')
        num += 1
        if(extension =='.txt'):
            print('Processando arquivo:', os.path.join(path, file))
            f = open(filename, "r")
            word_data = f.read()
            with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write(str(Counter(ngrams(word_data.split(), 3))))
            f = open(f'ngrams-results/{nomearquivo}.txt', "r")
            texto = f.read()
            quebra = texto.split(', (')
            quebra[0] = '(' + quebra[0].split('(')[2]
            quebra[-1] = quebra[-1].split('})')[0]
            with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write("\n(".join(quebra))
        #print('Finalização do arquivo-------')


# nomearquivo = len(os.listdir('ngrams-results')) +1
# f = open("resultados - filtro/2010/Estadão/Aquecimento global/ALIÁS/07 de março de 2010 - 01h18 - Uma_Terra_de_ninguém.txt", "r")
# word_data = f.read() #lê o arquivo
# with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
#     text.write(str(Counter(ngrams(word_data.split(), 3))))
# # lê e quebra as linhas escritas agora
# f = open(f'ngrams-results/{nomearquivo}.txt', "r")
# texto = f.read()
# quebra = texto.split(', (')
# quebra[0] = '(' + quebra[0].split('(')[2]
# quebra[-1] = quebra[-1].split('})')[0]
# with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
#     text.write("\n(".join(quebra))
