import openpyxl
import random
book = openpyxl.Workbook()

planilha = book.active

planilha.title = 'Lista de Presentes'

planilha.append(['Nome', 'Prensente?'])

nomes = ['Ana', 'Bruno', 'Carla', 'Diego', 'Fernanda', 
         'Gabriel', 'Helena', 'Igor', 'Juliana', 'Lucas']


for nome in nomes:
    presente =  random.choice(['Sim', 'Não'])

    planilha.append([nome, presente])


book.save('ListadePresentes.xlsx')