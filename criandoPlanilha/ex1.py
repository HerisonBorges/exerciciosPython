import openpyxl

arquivoEx = openpyxl.load_workbook('PlanilhaDeCompras.xlsx')
planilha = arquivoEx['Frutas']

conjunto = tuple(planilha['A2':'C6'])


for linha in conjunto:
    
    fruta = linha[0].value
    preco = linha[2].value
    preçoFruta = float(preco)
    if preçoFruta > 5.00:

        print(fruta, preçoFruta)