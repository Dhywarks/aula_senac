import PySimpleGUI as sg
import sqlite3 as banco

# INICIANDO A CONEXÃO COM O BANCO DE DADOS
conn = banco.connect("C:/Backup/Desktop/Moises/clientes.db")
c = conn.cursor()

# Definir tema e layout do menu principal
sg.theme("DarkTeal0")
menu_layout = [
    ["Cadastrar", ("Cadastro Clientes", "Cadastro Fornecedores", "Cadastro Transportadoras")],
    ["Consulta", ("Consulta Clientes", "Consulta Fornecedores", "Consulta Transportadoras")],
    ["Relatório", ("Relatório Clientes", "Relatório Fornecedores", "Relatório Transportadoras")]
]
main_layout = [
    [sg.Menu(menu_layout, tearoff=False)],
    [sg.Text("Selecione uma opção no menu.")]
]
window = sg.Window("Sistema de Cadastro Vs.1.0", main_layout, size=(300, 200))

# Função para editar um registro no banco de dados
def edit_record(new_value, old_product):
    c.execute("UPDATE clientes SET nome = ? WHERE UPPER(nome) = ?", (new_value, old_product))
    conn.commit()

# Loop principal da aplicação
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if "Cadastro" in event:
        # Código para cadastrar clientes, fornecedores ou transportadoras

    elif "Consulta" in event:
        # Código para consultar clientes, fornecedores ou transportadoras

    elif "Relatório" in event:
        # Código para gerar relatórios de clientes, fornecedores ou transportadoras

    # Outras partes do código

window.close()
conn.close()
