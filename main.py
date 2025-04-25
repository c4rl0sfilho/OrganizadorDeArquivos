import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma Pasta')

lista_de_arquivos = os.listdir(caminho)

locais = {
    'imagens': ['.png', '.jpg', '.svg', '.jpeg'],
    'pdfs': ['.pdf'],
    'docx': ['.docx'],
    'executaveis': ['.exe'],
    'msi': ['.msi']
}

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivo)  
    for pasta in locais:
        if extensao.lower() in locais[pasta]: 
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
