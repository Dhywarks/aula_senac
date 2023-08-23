import PySimpleGUI as sg
import sqlite3 as bbb

# Cria a conexão e interage com o banco
conn = bbb.connect("cliente.db")  # Conecta ao banco
c = conn.cursor()

layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro clientes', 'Cadastro fornecedores', 'Cadastro transportadoras']],
        ['Consulta', ['Consulta clientes', 'Consulta fornecedores', 'Consulta transportadoras']],
        ['Relatorio', ['Relatorio clientes', 'Relatorio fornecedores', 'Relatorio transportadoras']]
    ], tearoff=False)]
]

# NOME QUE APARECE NO SISTEMA E DEFINIÇÂO DO TAMANHO DA TELA
window = sg.Window("Sistema de Cadastro Vs.1.0", layout, size=(600, 400))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # CADASTRO DE CLIENTES
    if event == 'Cadastro clientes':
        cadastro_layout_clientes = [
            [sg.Text("Nome:")],
            [sg.InputText(key="nome")],
            [sg.Text("Cpf:")],
            [sg.InputText(key="cpf")],
            [sg.Text("Endereço:")],
            [sg.InputText(key="endereço")],
            [sg.Text("Email:")],
            [sg.InputText(key="email")],
            [sg.Text("Cidade:")],
            [sg.InputText(key="cidade")],
            [sg.Text("Telefone:")],
            [sg.InputText(key="telefone")],
            [sg.Text("Estado:")],
            [sg.InputText(key="estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        cadastro_clientes = sg.Window("Cadastro de clientes", cadastro_layout_clientes, size=(400,600))

        while True:
            event, values = cadastro_clientes.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                cadastro_clientes.close()
                break

            # Operações no Banco de dados
            c.execute("INSERT INTO clientes (nome, cpf, endereço, email, telefone, cidade, estado, ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      values["nome"],values["cpf"],values["endereço"],values["email"], values["telefone"], values["estado"], values["cidade"])
            conn.commit()

            # Limpa os campos após efetuar o cadastro
            cadastro_clientes["nome"].update("")
            cadastro_clientes["cpf"].update("")
            cadastro_clientes["endereço"].update("")
            cadastro_clientes["email"].update("")
            cadastro_clientes["telefone"].update("")
            cadastro_clientes["cidade"].update("")
            cadastro_clientes["estado"].update("")
            

            # Mostrar pop-up após o cadastro
            sg.popup("Cadastro do cliente realizado com sucesso!")

        cadastro_clientes.close()

    # CADASTRO DE CLIENTES
    elif event == "cadastrar":
        cadastro_layout = [
            [sg.Text("Nome")],
            [sg.InputText(key="nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="cpf")],
            [sg.Text("Endereço")],
            [sg.InputText(key="endereco")],
            [sg.Text("E-mail")],
            [sg.InputText(key="email")],
            [sg.Text("Telefone")],
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        cadastro_window = sg.Window("Cadastro de clientes", cadastro_layout, size=(400, 500))

        while True:
            event, values = cadastro_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break

            # interagindo com o banco
            c.execute("INSERT INTO clientes (nome, cpf, endereco, telefone, cidade, estado) VALUES (?, ?, ?, )",
                      (values["nome"], values["cpf"], values["endereco"], values["telefone"],
                       values["cidade"], values["estado"]))
            conn.commit()

            # Limpar inputs após o cadastro
            cadastro_window["nome"].update("")
            cadastro_window["cpf"].update("")
            cadastro_window["endereco"].update("")
            cadastro_window["telefone"].update("")
            cadastro_window["cidade"].update("")
            cadastro_window["estado"].update("")

            # Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()

    # CADASTRO DE FORNECEDORES
    elif event == "Cadastro fornecedores":
        fornecedor_layout = [
            [sg.Text("Nome")],
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],
            [sg.InputText(key="cnpj")],
            [sg.Text("Endereço")],
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        fornecedor_window = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400, 500))

        while True:
            event, values = fornecedor_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                fornecedor_window.close()
                break

            # interagindo com o banco e salvando os dados
            c.execute("INSERT INTO fornecedor (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, )",
                      (values["nome"], values["cnpj"], values["endereco"], values["telefone"],
                       values["cidade"], values["estado"]))
            conn.commit()

            # Limpar inputs após o cadastro
            fornecedor_window["nome"].update("")
            fornecedor_window["cnpj"].update("")
            fornecedor_window["endereco"].update("")
            fornecedor_window["telefone"].update("")
            fornecedor_window["cidade"].update("")
            fornecedor_window["estado"].update("")

            # Confirmar o cadastro
            sg.popup("Fornecedor Cadastrado com sucesso!", title="Cadastro")

        fornecedor_window.close()

    elif event == "Cadastro transportadoras":
        transp_layout = [
            [sg.Text("Nome")],
            [sg.InputText(key="nome")],
            [sg.Text("CNPJ")],
            [sg.InputText(key="cnpj")],
            [sg.Text("Endereço")],
            [sg.InputText(key="endereco")],
            [sg.Text("Telefone")],
            [sg.InputText(key="telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="estado")],
            [sg.Button("Cadastrar")],
            [sg.Button("Cancelar")]
        ]

        transp_window = sg.Window("Cadastro de Transportadoras", transp_layout, size=(400, 500))

        while True:
            event, values = transp_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                transp_window.close()
                break

            # interagindo com o banco e salvando os dados
            c.execute("INSERT INTO transport (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)",
                      (values["nome"], values["cnpj"], values["endereco"], values["telefone"],
                       values["cidade"], values["estado"]))
            conn.commit()

            # Limpar inputs após o cadastro
            transp_window["nome"].update("")
            transp_window["cnpj"].update("")
            transp_window["endereco"].update("")
            transp_window["telefone"].update("")
            transp_window["cidade"].update("")
            transp_window["estado"].update("")

            # Confirmar o cadastro
            sg.popup("Transportadora Cadastrada com sucesso!", title="Cadastro")

        transp_window.close()


    if event == "Consulta clientes":

             consulta_layout =[
                 [sg.Text("clientes")],
                 [sg.InputText(key="clientes")],
                 [sg.Button("Consultar")],
                 [sg.Button("Cancelar")],
                 [sg.Table(values=[], headings=["Nome","Cpf","Endereço","Telefone","Cidade","Estado"], display_row_numbers=False, auto_size_columns=False,num_rows=10, key="Tabela")]

             ]
             consulta_window = sg.Window("Consulta de clientes", consulta_layout, resizable=True)


             while True:
                 event, values = consulta_window.read()

                 if event == sg.WIN_CLOSED or event == "Cancelar":
                     consulta_window.close
                     break
                 
                 produto_busca = values["Clientes"].upper()
                 c.execute( "SELECT nome, cpf, endereco, telefone, cidade, estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca))
                 registros = c.fetchall()

                 tabela = consulta_window["tabela"]
                 tabela.update(values=registros)

             consulta_window.close()
    

    elif event == "Consulta fornecedores":

        consulta_layout =[
                 [sg.Text("Consultar Fornecedor")],
                 [sg.InputText(key="fornecedor")],
                 [sg.Button("Consultar")],
                 [sg.Button("Cancelar")],
                 [sg.Table(values=[], headings=["Nome","Cnpj","endereço","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False,num_rows=10, key="Tabela")]

             ]
        consulta_window = sg.Window("Consulta de fornecedores", consulta_layout, resizable=True)

        
        while True:
                 event, values = consulta_window.read()

                 if event == sg.WIN_CLOSED or event == "Cancelar":
                     consulta_window.close
                     break
                 
                 produto_busca = values["Fornecedor"].upper()
                 c.execute( "SELECT nome, cnpj, cpf, endereco, telefone, cidade, estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca))
                 registros = c.fetchall()

                 tabela = consulta_window["tabela"]
                 tabela.update(values=registros)

        consulta_window.close()
    

    elif event == "Consulta transportadoras":

        consulta_layout =[
                 [sg.Text("Consultar Transportadoras")],
                 [sg.InputText(key="trasnportadoras")],
                 [sg.Button("Consultar")],
                 [sg.Button("Cancelar")],
                 [sg.Table(values=[], headings=["Nome","Cnpj","endereço","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False,num_rows=10, key="Tabela")]

             ]
        consulta_window = sg.Window("Consulta de transportadoras", consulta_layout, resizable=True)

        
        while True:
                 event, values = consulta_window.read()

                 if event == sg.WIN_CLOSED or event == "Cancelar":
                     consulta_window.close
                     break
                 
                 produto_busca = values["Trasnportadoras"].upper()
                 c.execute( "SELECT nome, cnpj, cpf, endereco, telefone, cidade, estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca))
                 registros = c.fetchall()

                 tabela = consulta_window["tabela"]
                 tabela.update(values=registros)


    elif event == "Relatorio transportadoras":

        consulta_layout =[
                 [sg.Text("Relatorio transportadoras")],
                 [sg.InputText(key="transportadoras")],
                 [sg.Button("Consultar")],
                 [sg.Button("Cancelar")],
                 [sg.Table(values=[], headings=["Nome","Cnpj","endereço","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False,num_rows=10, key="Tabela")]

             ]
        consulta_window = sg.Window("Consulta de transportadoras", consulta_layout, resizable=True)

        
        while True:
                 event, values = consulta_window.read()

                 if event == sg.WIN_CLOSED or event == "Cancelar":
                     consulta_window.close
                     break
                 
                 produto_busca = values["transportadoras"].upper()
                 c.execute( "SELECT nome, cnpj, cpf, endereco, telefone, cidade, estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca))
                 registros = c.fetchall()

                 tabela = consulta_window["tabela"]
                 tabela.update(values=registros)

    
                 if registro:
                    with open("relatorio.html", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write("<h1>Relatório</h1><table border='1'><tr><th>Produto</th><th>Valor</th></tr>")
       
                        for row in registro:
                            f.write(f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>")
                        f.write("</table></body></html>")


                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
           
    else:
        sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

        produto_busca_r = values["produto"].upper()
        c.execute("SELECT * FROM vendas WHERE UPPER(produto) = ?", (produto_busca_r,))
        registro = c.fetchall()


            #Limpar inputs
        relatorio_window["produto"].update("")

        relatorio_window.close()

        consulta_window.close()

             
conn.close()