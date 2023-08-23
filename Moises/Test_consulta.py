import PySimpleGUI as sg
import sqlite3 as banco
# INICIANDO A CONEXÂO COM O BANCO DE DADOS
conn = banco.connect("C:/Backup/Desktop/Moises/clientes.db")
c = conn.cursor()


# BOTÂO DO MENU PRINCIPAL COM A OPÇÂO DE CADASTRAR
sg.theme("DarkTeal12")

if event == "Consulta Clientes":
        
        consulta_layout = [
            [sg.Text("Clientes")],
            [sg.InputText(key="clientes")],
            [sg.Button("Consultar")],
            [sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["nome","cpf","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
        ]    
        consulta_window = sg.Window("Consulta de Clientes", consulta_layout, resizable=True)

        while True:
            event, values = consulta_window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_window.close()
                break

            produto_busca = values["clientes"].upper()
            c.execute("SELECT nome, cpf, endereco, telefone, cidade, estado FROM clientes WHERE UPPER(nome) = ?", (produto_busca,))
            registros = c.fetchall()

            tabela = consulta_window["tabela"]
            tabela.update(values=registros)

        consulta_window.close()

