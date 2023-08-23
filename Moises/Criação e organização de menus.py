# Importando a biblioteca PySimpleGUI com o alias 'sg'
import PySimpleGUI as sg
# Importando a biblioteca sqlite3 com o alias 'banco'
import sqlite3 as banco

# Estabelecendo conexão com o banco de dados "clientes.db" localizado no caminho especificado
conn = banco.connect("C:/Backup/Desktop/Moises/clientes.db")
# Criando um cursor para interagir com o banco de dados
c = conn.cursor()

# Configurando o tema visual da interface gráfica para "DarkTeal12"
sg.theme("DarkTeal12")
# Criando um layout para a interface gráfica
layout = [
    # Criando um menu dropdown na interface
    [sg.Menu([
        # Opções do menu "Cadastrar" com subitens de tipos de cadastro
        ["Cadastrar", ('Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadoras')],
        # Opções do menu "Consulta" com subitens de tipos de consulta
        ["Consulta", ('Consulta Clientes', 'Consulta Fornecedores', 'Consulta Transportadoras')],
        # Opções do menu "Relatório" com subitens de tipos de relatórios
        ["Relatório", ('Relatório Clientes', 'Relatório Fornecedores', 'Relatório Transportadoras')]
    ], tearoff=False)]
]

# Criando uma janela com o título "Sistema de Cadastro Vs.1.0", usando o layout definido e tamanho específico
window = sg.Window("Sistema de Cadastro Vs.1.0", layout, size=(300, 200))

# Iniciando um loop para interagir com a janela
while True:
    # Lendo os eventos e valores da janela
    event, values = window.read()

    # Verificando se o evento é o fechamento da janela
    if event == sg.WINDOW_CLOSED:
        # Encerrando o loop caso a janela seja fechada
        break