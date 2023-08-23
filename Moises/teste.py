import PySimpleGUI as sg
import sqlite3 as banco

# Função para cadastrar um registro
def cadastrar_registro(tipo):
    fields = ["nome", "cpf", "endereco", "telefone", "cidade", "estado"]
    layout = [
        [sg.Text("Cadastro de " + tipo)],
        *[[sg.Text(field.capitalize()), sg.InputText(key=field)] for field in fields],
        [sg.Button("Cadastrar"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Cadastro de " + tipo, layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancelar":
            break

        if all(values[field] for field in fields):
            c.execute(f"INSERT INTO {tipo} VALUES (?, ?, ?, ?, ?, ?)", [values[field] for field in fields])
            conn.commit()
            sg.popup(f"{tipo.capitalize()} cadastrado com sucesso!", title="Cadastro")
            window.close()
            break
        else:
            sg.popup_error("Preencha todos os campos!")

# Função para consultar registros
def consultar_registro(tipo):
    layout = [
        [sg.Text(f"Consultar {tipo.capitalize()}")],
        [sg.InputText(key=tipo), sg.Button("Consultar"), sg.Button("Cancelar")],
        [sg.Table(values=[], headings=["Nome", "CPF/CNPJ", "Endereço", "Telefone", "Cidade", "Estado"], auto_size_columns=False, num_rows=10, key="tabela")],
    ]

    window = sg.Window(f"Consulta de {tipo.capitalize()}", layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancelar":
            break

        search_term = values[tipo].strip().upper()
        if search_term:
            c.execute(f"SELECT * FROM {tipo} WHERE UPPER(nome) = ?", (search_term,))
            registros = c.fetchall()
            window["tabela"].update(values=registros)
        else:
            sg.popup_error("Digite um termo para consulta!")

    window.close()

# Função para gerar relatórios
def gerar_relatorio(tipo):
    layout = [
        [sg.Text(f"Gerar Relatório de {tipo.capitalize()}")],
        [sg.InputText(key=tipo), sg.Button("Gerar Relatório"), sg.Button("Cancelar")],
    ]

    window = sg.Window(f"Relatório de {tipo.capitalize()}", layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancelar":
            break

        search_term = values[tipo].strip().upper()
        if search_term:
            c.execute(f"SELECT * FROM {tipo} WHERE UPPER(nome) = ?", (search_term,))
            registro = c.fetchone()

            if registro:
                with open(f"Relatorio_{tipo}.html", "w") as f:
                    f.write("<html><head></head><body>")
                    f.write(f"<h1>Relatório<h1><table border='1'><tr>")
                    f.write("".join([f"<th>{field.capitalize()}</th>" for field in registro]))
                    f.write("</tr>")
                    f.write("".join([f"<td>{value}</td>" for value in registro]))
                    f.write("</tr></table></body></html>")
                sg.popup(f"Relatório de {tipo.capitalize()} gerado com sucesso!", title="Relatório")
            else:
                sg.popup_error(f"{tipo.capitalize()} não encontrado no sistema!")

    window.close()

# Conexão com o banco de dados
conn = banco.connect("C:/Backup/Desktop/Moises/clientes.db")
c = conn.cursor()

# Definição dos menus
menu_def = [
    ["Cadastrar", ["Clientes", "Fornecedores", "Transportadoras"]],
    ["Consulta", ["Clientes", "Fornecedores", "Transportadoras"]],
    ["Relatório", ["Clientes", "Fornecedores", "Transportadoras"]]
]

sg.theme("DarkTeal0")

layout = [
    [sg.Menu(menu_def, tearoff=False)],
    [sg.Text("", size=(40, 1), key="-OUTPUT-")],
]

window = sg.Window("Sistema de Cadastro Vs.1.0", layout, size=(300, 200))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ["Clientes", "Fornecedores", "Transportadoras"]:
        sub_event, _ = window.read()
        if sub_event in ["Cadastrar", "Consulta", "Relatório"]:
            if event == "Clientes":
                if sub_event == "Cadastrar":
                    cadastrar_registro("clientes")
                elif sub_event == "Consulta":
                    consultar_registro("clientes")
                elif sub_event == "Relatório":
                    gerar_relatorio("clientes")
            elif event == "Fornecedores":
                if sub_event == "Cadastrar":
                    cadastrar_registro("fornecedor")
                elif sub_event == "Consulta":
                    consultar_registro("fornecedor")
                elif sub_event == "Relatório":
                    gerar_relatorio("fornecedor")
            elif event == "Transportadoras":
                if sub_event == "Cadastrar":
                    cadastrar_registro("transport")
                elif sub_event == "Consulta":
                    consultar_registro("transport")
                elif sub_event == "Relatório":
                    gerar_relatorio("transport")

window.close()
conn.close()
