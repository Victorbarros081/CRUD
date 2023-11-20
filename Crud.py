import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1905',
    database='academiaturmab',
)

meucursor = conexao.cursor()
while True:
    cont = 0
    reposta1 = "S"
    print(" ====================MENU====================="
          "\n1.VISUALIZAR TABELAS\n"
          "2.ADICIONAR INFORMAÇÕES NAS TABELAS\n"
          "3.ATUALIZAR INFORMAÇÕES NAS TABELAS\n"
          "4.DELETAR INFORMAÇÕES DAS TABELAS\n"
          "5.ENCERRAR SISTEMA")
    usuario = input("DIGITE A OPÇÃO: ")

    if usuario == '1':
        meucursor.execute("SHOW TABLES")
        meuresultado = meucursor.fetchall()
        for x in meuresultado:
            print(f'{cont+1}-{x[0]}')
            cont +=1

        reposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ")
        while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
            reposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ")
    elif usuario == '2':
        while reposta1 == "S":
            nome_tabela= input("DIGITE O NOME DA TABELA: ").upper()
            if nome_tabela == 'alunos'.upper():
                Nome = input("DIGITE O NOME: ")
                cpf = input("DIGITE O CPF: ")
                endereco = input("DIGITE O ENDEREÇO: ")
                telefone = input("DIGITE O TELEFONE: ")
                comando = f'INSERT INTO alunos (Nome, cpf, endereco, telefone) VALUES ("{Nome}", "{cpf}", "{endereco}","{telefone}")'
                meucursor.execute(comando)
                conexao.commit()
                print ("DADO INSERIDO COM SUCESSO NA TABELA ALUNOS")
                reposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ")
                while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
                    reposta1 = input("Opção inválida, escolha novamente [S/N]: ")
            if nome_tabela == 'funcionarios'.upper():
                nome = input("DIGITE O NOME: ")
                cpf = input("DIGITE O CPF: ")
                departamento = input("DIGITE O DEPARTAMENTO: ")
                cpf_supervisor = input("DIGITE O CPF DO SUPERVISOR: ")
                salario = input("DIGITE O SALARIO: ")

                comando = f"""INSERT INTO funcionarios (nome, cpf,departamento, cpf_supervisor,salario) VALUES ("{nome}", "{cpf}","{departamento}","{cpf_supervisor}","{salario}")"""

                meucursor.execute(comando)
                conexao.commit()
                print("DADO INSERIDO COM SUCESSO NA TABELA FUNCIONARIOS")
                reposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ")
                while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
                    reposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ")

            if nome_tabela == 'modalidade':
                professor = input("DIGITE O NOME DO PROFESSOR: ")
                Nome_da_modalidade = input("DIGITE O NOME DA MODALIDADE: ")
                duracao = input("DIGITE A DURAÇÃO: ")
                horario = input("DIGITE O HORARIO DA MODALIDADE [00:00]: ")

                comando = f"""INSERT INTO modalidade (professor, Nome_da_modalidade,duracao,horario) VALUES ("{professor}","{Nome_da_modalidade}","{duracao}","{horario}")"""
                meucursor.execute(comando)
                conexao.commit()
                print("DADO INSERIDO COM SUCESSO NA TABELA MODALIDADE")
                reposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ")
                while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
                    reposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ")
            if nome_tabela == "personal".upper():
                nome = input("DIGITE O NOME DO PERSONAL: ")
                cpf = input("DIGITE O CPF DO PERSONAL: ")
                comando = f'INSERT INTO personal (Nome, cpf) VALUES ("{nome}", "{cpf}")'

                meucursor.execute(comando)
                conexao.commit()
                print("DADO INSERIDO COM SUCESSO NA TABELA PERSONAL")
                reposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ")
                while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
                    reposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ")
    elif usuario == '3':
        minhatabela = input("INFORME A TABELA: ")
        print(f"******tabela {minhatabela} selecionada****** ")
        coluna1 = input("INFORME O NOME DA COLUNA: ")
        valor_coluna = input("INSIRA O NOVO CONTEUDO: ")
        coluna2 = input("INFORME A COLUNA QUE SERÁ ALTERADA: ")
        condicao = input("INFORME O CONTEUDO DA COLUNA: ")
        comando = f"""UPDATE {minhatabela} SET {coluna1} = '{valor_coluna}' WHERE {coluna2} = '{condicao}'"""
        meucursor.execute(comando)
        conexao.commit()
        meucursor.close()
        conexao.close()
        reposta1 = input("DESEJA ALTERAR DADOS NOVAMENTE: ")
        while (reposta1 != "S") and (reposta1 != "N" and reposta1 != "n"):
            reposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ")
    elif usuario == '4':
        escolha = input("[1]DELETAR DADOS ESPECIFICOS DE UMA TABELA\n[2]DELETAR TODOS OS DADOS DA TABELA\n[3]DELETAR TABELA\nESCOLHA UMA OPÇÃO: ")
        if escolha == '1':
            minhatabela = input("INFORME A TABELA: ")
            print(f"******tabela {minhatabela} selecionada******")
            coluna1 = input("INFORME O NOME DA COLUNA: ")
            condicao = input("INFORME O CONTEUDO DA COLUNA: ")
            comando = f"""DELETE FROM {minhatabela} WHERE {coluna1} = '{condicao}'"""
            meucursor.execute(comando)
            conexao.commit()
            resposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ").upper()
            while resposta1 != "S" and resposta1 != "N".upper():
                resposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ").upper()

        if escolha == '2':
            minhatabela = input("INFORME A TABELA: ")
            print(f"******tabela {minhatabela} selecionada******")
            comando = f"""DELETE FROM {minhatabela}"""
            meucursor.execute(comando)
            conexao.commit()
            print("DADOS DA TABELA DELETADA COM SUCESSO!")
            resposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ").upper()
            while resposta1 != "S" and resposta1 != "N".upper():
                resposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ").upper()

        if escolha == '3':
            escolha2 = input("MUITO CUIDADO,VOCE ESTÁ DELETANDO TODA UMA TABELA\nQUER CONTINUAR ?").upper()
            if escolha2 == 'S':
                minhatabela = input("INFORME A TABELA: ")
                comando = f"DROP TABLE {minhatabela}"
                meucursor.execute(comando)
                print ("TABELA EXCLUIDA COM SUCESSO!")
            if escolha2 == "N":
                resposta1 = input("DESEJA VISUALIZAR AS TABELAS NOVAMENTE: ").upper()
                while resposta1 != "S" and resposta1 != "N".upper():
                    resposta1 = input("OPÇÃO INVALIDA, ESCOLHA NOVAMENTE [S/N]: ").upper()


    elif usuario == "5":
        print("*=*=*=*=*=*=*=*=*=*=*=*=**=*=*=*=*=*=*=*=*=*\n"
              "*=*=*=*=*=*=* SISTEMA ENCERRADO *=*=*=*=*=*=*\n"
              "*=*=*=*=*=*=*=*=*=*=*=*=**=*=*=*=*=*=*=*=*=*")
        meucursor.close()
        conexao.close()
        break
    else:
        print("Opção inválida, tente novamente!")

