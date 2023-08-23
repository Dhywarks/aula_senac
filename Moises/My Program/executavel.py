import PySimpleGUI as sg
import sqlite3 as banco
# INICIANDO A CONEXÂO COM O BANCO DE DADOS
conn = banco.connect("C:/Backup/Desktop/Moises/clientes.db")
c = conn.cursor()




# BOTÂO DO MENU PRINCIPAL COM A OPÇÂO DE CADASTRAR


# Definir tema e layout do menu principal
# MENU COM BOTOÔES 
sg.theme("DarkTeal0")
layout = [
    [sg.Menu([
    ["Cadastrar", ('Cadastro Clientes', 'Cadastro Fornecedores', 'Cadastro Transportadoras')],
    ["Consulta", ('Consulta Clientes', 'Consulta Fornecedores', 'Consulta Transportadoras')],
    ["Relatório", ('Relatório Clientes', 'Relatório Fornecedores', 'Relatório Transportadoras')]
    ],
    tearoff=False)]
]





# NOME QUE APARECE NO SISTEMA E DEFINIÇÂO DO TAMANHO DA TELA  
window = sg.Window("Sistema de Cadastro Vs.1.0",layout,size=(300,200) )

while True:
    event, values = window.read()

    #SE a janela for fechada Encerra o Processo de cadastro
    if event == sg.WINDOW_CLOSED:
        break







    #CADASTRO DE CLIENTES

    if event == "Cadastro Clientes":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
        cadastro_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="nome")],
            [sg.Text("CPF")],      
            [sg.InputText(key="cpf")],
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


        cadastro_window = sg.Window("Cadastro de Clientes", cadastro_layout, size=(400,500))

         #While da janela de  cadastro de clientes
        while True:
            event, values = cadastro_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break


            #interagindo com o banco
            c.execute("INSERT INTO clientes (nome, cpf, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cpf"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            cadastro_window["nome"].update("")
            cadastro_window["cpf"].update("")
            cadastro_window["endereco"].update("")
            cadastro_window["telefone"].update("")
            cadastro_window["cidade"].update("")
            cadastro_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()





#CADASTRO DE FORNECEDORES

    elif event == "Cadastro Fornecedores":

        #criar layout da seguna tela que aparece quando clica em cadastrar cliente
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


        fornecedor_window = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = fornecedor_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                fornecedor_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO fornecedor (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            fornecedor_window["nome"].update("")
            fornecedor_window["cnpj"].update("")
            fornecedor_window["endereco"].update("")
            fornecedor_window["telefone"].update("")
            fornecedor_window["cidade"].update("")
            fornecedor_window["estado"].update("")

            #Confirmar o cadastro
            sg.popup("Fornecedor Cadastrado com sucesso!", title="Cadastro")

        fornecedor_window.close()





    elif event == "Cadastro Transportadoras":

        #criar layout da seguna tela que aparece quando clica em cadastrar Transportadora
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


        transp_window = sg.Window("Cadastro de Transportadoras", transp_layout, size=(400,500))

         #While da janela de  cadastro de fornecedores
        while True:
            event, values = transp_window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                transp_window.close()
                break


            #interagindo com o banco esalvando os dados
            c.execute("INSERT INTO transport (nome, cnpj, endereco, telefone, cidade, estado) VALUES (?, ?, ?, ?, ?, ?)", (values["nome"], values["cnpj"],values["endereco"],values["telefone"],values["cidade"],values["estado"]))
            conn.commit()

            #Limpar iputs após o cadastro
            transp_window["nome"].update("")
            transp_window["cnpj"].update("")
            transp_window["endereco"].update("")
            transp_window["telefone"].update("")
            transp_window["cidade"].update("")
            transp_window["estado"].update("")




        transp_window.close() 


    if event == "Consulta Clientes":

            consulta_layout =[
                [sg.Text("Clientes")],
                [sg.InputText(key="clientes")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cpf","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Clientes", consulta_layout, resizable=True)

        #loop eventos

            while True:
                event, values = consulta_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["clientes"].upper()
                c.execute( "SELECT nome, cpf, endereco,telefone,cidade,estado FROM clientes WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros) # ATUALIZA A TELA COM OS DADOS QUE ESTAVA ARMAZENADO NA VARIÁVEL "registros"    

            consulta_window.close()  


    elif event == "Consulta Fornecedores":

            consulta_layout =[
                [sg.Text("Consultar_Fornecedor")],
                [sg.InputText(key="fornecedor")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cnpj","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Fornecedores", consulta_layout, resizable=True)

        #loop eventos

            while True:
                event, values = consulta_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["fornecedor"].upper()
                c.execute( "SELECT nome, cnpj, endereco,telefone,cidade,estado FROM fornecedor WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     

            consulta_window.close()  


    # AQUI ENTRAMOS NO MENU DE CONSULTA DAS TRANSPORTADORAS CADASTRADAS        
    elif event == "Consulta Transportadoras":

            consulta_layout =[
                [sg.Text("Consultar Transportadora")],
                [sg.InputText(key="transportadora")],
                [sg.Button("Consultar")],
                [sg.Button("Cancelar")],
                [sg.Table(values=[], headings=["nome","cnpj","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
            ]    
            consulta_window = sg.Window("Consulta de Transportadora", consulta_layout, resizable=True)

        #loop eventos

            while True:
                event, values = consulta_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    consulta_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["transportadora"].upper()
                c.execute( "SELECT nome, cnpj, endereco,telefone,cidade,estado FROM transport WHERE UPPER(nome) = ?",(produto_busca,))
                registros = c.fetchall()

                # ATUALIZAR
                tabela = consulta_window["tabela"]
                tabela.update(values=registros)     

            consulta_window.close()









                                # -----------RELATÓRIOS------------ #       
    elif event == "Relatório Fornecedores": 

            relatorio_layout =[
                [sg.Text("Relatório Fornecedores")],
                [sg.InputText(key="fornecedor")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]

            ]    
            relatorio_window = sg.Window("Relatório de Fornecedores", relatorio_layout, resizable=True)

        #loop eventos

            while True:
                event, values = relatorio_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["fornecedor"].upper()
                c.execute( "SELECT * FROM fornecedor WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()

                if registro:
                    with open("C:/Backup/Desktop/Moises/clientes.db","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>Cnpj</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")

                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO

                else :
                    sg.popup("Fornecedor não Encontrado no Sistema!!", title="Relatório")


                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["fornecedor"].update ("")
                    relatorio_window.update (values="registro")     

                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP


          # RELATÓRIO DE TRANPORTADORAS  
    elif event == "Relatório Transportadoras": 

            relatorio_layout =[
                [sg.Text("Relatório Transportadoras")],
                [sg.InputText(key="transport")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]

            ]    
            relatorio_window = sg.Window("Relatório de Transportadoras", relatorio_layout, resizable=True)

        #loop eventos

            while True:
                event, values = relatorio_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["transport"].upper() # upper DEIXA A PESQUISA PADRÂO NO BANCO DE DADOS PARA NÂO HAVER ERRO NA QUERY
                c.execute( "SELECT * FROM transport WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()

                if registro:
                    with open("C:/Backup/Desktop/Moises/clientes.db","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>Cnpj</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")

                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO

                else :
                    sg.popup("Transportadora não Encontrado no Sistema!!", title="Relatório")


                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["transport"].update ("")
                    relatorio_window.update (values="registro")     

                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP        



   # RELATÓRIO DE CLIENTES         
    elif event == "Relatório Clientes": 

            relatorio_layout =[
                [sg.Text("Relatório Clientes")],
                [sg.InputText(key="clientes")],
                [sg.Button("Gerar Relatório")],
                [sg.Button("Cancelar")]

            ]    
            relatorio_window = sg.Window("Relatório de Clientes", relatorio_layout, resizable=True)

        #loop eventos

            while True:
                event, values = relatorio_window.read()

                if event == sg.WIN_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # operações no banco de dados
                produto_busca = values["clientes"].upper() # upper DEIXA A PESQUISA PADRÂO NO BANCO DE DADOS PARA NÂO HAVER ERRO NA QUERY
                c.execute( "SELECT * FROM clientes WHERE UPPER(nome) = ?",(produto_busca,))
                registro = c.fetchone()

                if registro:
                    with open("clientes.db","w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório<h1><table border='1'><tr><th>Nome</th><th>cpf</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th><th>{registro[2]}</th><th>{registro[3]}</th><th>{registro[4]}</th><th>{registro[5]}</th></tr>")
                        f.write("</body></html>")

                        sg.popup("Relatório Gerado com Sucesso!!", title="Relatório") # MENSAGEM QUE APARECE APÓS GERAR O RELATÓRIO

                else :
                    sg.popup("Cliente não Encontrado no Sistema!!", title="Relatório")


                    # ATUALIZAR OS DADOS DA PESQUISA APÓS REAKIZADA COM SUCESSO
                    relatorio_window["clientes"].update ("")
                    relatorio_window.update (values="registro")     

                relatorio_window.close()    # DEVE FICAR NA LINHA DO BREAK PARA FECHAR A TELA APÓS O POPUP         




# Define a função para editar um registro no banco de dados
def edit_record(new_product, new_value, old_product):
    c.execute("UPDATE clientes SET nome = ? WHERE UPPER(nome) = ?", (new_value, old_product))
    conn.commit()

# Define a estrutura da interface gráfica usando a biblioteca PySimpleGUI
layout = [
    [sg.Text("Produto")],
    [sg.InputText(key="produto")],
    [sg.Button("Consultar")],
    [sg.Table(values=[], headings=["nome","cpf","endereco","telefone","cidade","estado"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")],
    [sg.Button("Editar"), sg.Button("Excluir"), sg.Button("Cancelar")]
]

window = sg.Window("Consulta", layout, resizable=True)  # Cria a janela da interface gráfica

# Loop principal da aplicação
while True:
    event, values = window.read()  # Lê os eventos e valores da interface

    if event == sg.WIN_CLOSED or event == "Cancelar":  # Fecha a janela se clicado no "X" ou no botão "Cancelar"
        break

    if event == "Consultar":
        produto_pesquisa = values["produto"].upper()  # Obtém o valor do campo de pesquisa e converte para maiúsculas
        c.execute("SELECT nome,cpf,endereco,telefone,cidade,estado FROM clientes WHERE UPPER(nome) = ?", (produto_pesquisa,))
        registros = c.fetchall()  # Executa a consulta SQL e obtém os registros correspondentes

        window["tabela"].update(values=registros)  # Atualiza a tabela na interface com os registros encontrados

    elif event == "Editar":
        selected_row = values["tabela"]  # Obtém a linha selecionada na tabela
        if selected_row:
            selected_row_index = selected_row[0]  # Obtém o índice da linha selecionada
            row_data = registros[selected_row_index]  # Obtém os dados da linha selecionada
            edited_product = sg.popup_get_text("Editar produto", default_text=row_data[0])  # Abre um popup para editar o produto
            if edited_product is not None:
                old_product = row_data[0]
                # Chama a função para editar o registro no banco de dados e atualiza os registros na interface
                edit_record(edited_product, row_data[1], old_product)
                registros[selected_row_index] = (edited_product, row_data[1], row_data[2], row_data[3], row_data[4], row_data[5])
                window["tabela"].update(values=registros)

    elif event == "Excluir":
        selected_row = values["tabela"]
        if selected_row:
            selected_row_index = selected_row[0]
            row_data = registros[selected_row_index]
            if sg.popup_yes_no("Tem certeza que deseja excluir esse registro?", title="Confirmação") == "Yes":
                product_to_delete = row_data[0]
                # Executa o comando SQL para excluir o registro do banco de dados
                c.execute("DELETE FROM clientes WHERE nome = ?", (product_to_delete,))
                conn.commit()  # Confirma a alteração no banco de dados
                registros.pop(selected_row_index)  # Remove o registro da lista de registros
                window["tabela"].update(values=registros)  # Atualiza a tabela na interface


window.close()
conn.close()
