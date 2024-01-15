import os, time, mysql.connector
from mysql.connector import Error

"""
host = "localhost"
usuario = "root"
senha = "admin"
DB = "eclipsepi"
"""

def criarBD(host, usuario, senha, DB):
    try:
        connection=mysql.connector.connect( 
            host = host,
            user = usuario,
            password = senha, 
            database = DB
        )
        print("Banco de dados já existe!")
        return True
    except Error as err:
        print("Banco de dados não existe, criando banco de dados...")
        pass
    connection=connection=mysql.connector.connect(
            host = host, 
            user = usuario, 
            password = senha 
        )
    cursor = connection.cursor() 
    cursor.execute("CREATE DATABASE "+ DB) 
    cursor.close() 
    connection.close() 
    print("Banco de dados criado com sucesso!")
    return False

def criarTabelas(host, usuario, senha, DB):
    connection=conectarBD (host, usuario, senha, DB)
    cursor = connection.cursor() #Cursor para comunicação com o banco
    cursor.execute('''CREATE TABLE clientes (id int not null auto_increment primary key, nome varchar(45), email varchar(90), telefone varchar(45), cnpj varchar(18));
CREATE TABLE projetos (id int not null auto_increment primary key, nome varchar(45), descricao varchar(180), data_inicio date, data_fim date, clientes_id int not null, FOREIGN KEY (clientes_id) REFERENCES clientes (id));
CREATE TABLE funcionarios (id int not null auto_increment primary key, nome_razao_social varchar(45), cpf_cnpj varchar(18), salario float, setor varchar(15), maquina_id int, maquina_config int, projetos_id int, FOREIGN KEY (projetos_id) REFERENCES projetos (id));
CREATE TABLE faturas (id int not null auto_increment primary key, pago_status int, valor float, data_criacao date, data_quitacao date)
                   ''')
    #Executa o comando SQL
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão
    print("Tabelas criadas com sucesso!")

def conectarBD (host, usuario, senha, DB): 
    connection=mysql.connector.connect( 
        host = host, 
        user = usuario, 
        password = senha, 
        database = DB
    )
    return connection
    
#Inserir cliente
def insert_cliente(nome, email, telefone, cnpj, conn):
    connection = conn
    cursor = connection.cursor()
    sql = "INSERT INTO CLIENTES (nome, email, telefone, cnpj) VALUES (%s, %s, %s, %s)"
    data = (
        nome,
        email,
        telefone,
        cnpj
        )
    cursor.execute(sql, data)
    connection.commit()
    idcliente = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Cliente cadastrado com ID ", idcliente)

#Exibir clientes
def read_clientes(conn):
    connection = conn
    cursor = connection.cursor()
    sql = "SELECT * FROM CLIENTES"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for result in results:
        print(result)

#Atualizar clientes
def update_clientes(nome, email, telefone, cnpj, id, conn): 
    connection = conn 
    cursor = connection.cursor() 
    sql = "UPDATE CLIENTES SET NOME=%s, EMAIL=%s, TELEFONE=%s, CNPJ=%s WHERE ID=%s"
    data = ( 
        nome,
        email,
        telefone,
        cnpj,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados") 

#Excluir cliente
def delete_clientes(id, conn): 
    connection = conn
    cursor = connection.cursor()
    sql = "DELETE FROM CLIENTES WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")



#Inserir projeto
def insert_projetos(nome, descricao, data_inicio, data_fim, clientes_id, conn):
    connection = conn
    cursor = connection.cursor()
    sql = "INSERT INTO PROJETOS (nome, descricao, data_inicio, data_fim, clientes_id) VALUES (%s, %s, %s, %s, %s)"
    data = (nome,
            descricao,
            data_inicio,
            data_fim,
            clientes_id
            )
    cursor.execute(sql, data)
    connection.commit()
    idprojeto = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Projeto cadastrado com ID ", idprojeto)

#Exibir projetos
def read_projetos(conn):
    connection = conn
    cursor = connection.cursor()
    sql = "SELECT * FROM PROJETOS"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for result in results:
        print(result)

#Atualizar projeto
def update_projetos(nome, descricao, data_inicio, data_fim, clientes_id, id, conn): 
    connection = conn 
    cursor = connection.cursor() 
    sql = "UPDATE PROJETOS SET NOME=%s, DESCRICAO=%s, DATA_INICIO=%s, DATA_FIM=%s, CLIENTES_ID=%s WHERE ID=%s"
    data = ( 
        nome,
        descricao,
        data_inicio,
        data_fim,
        clientes_id,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados") 

#Excluir projeto
def delete_projetos(id, conn): 
    connection = conn
    cursor = connection.cursor()
    sql = "DELETE FROM PROJETOS WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos") 



#Inserir funcionário
def insert_funcionarios(nome_razao_social, cpf_cnpj, salario, setor, maquina_id, maquina_config, projetos_id, conn):
    connection = conn
    cursor = connection.cursor()
    sql = "INSERT INTO FUNCIONARIOS (nome_razao_social, cpf_cnpj, salario, setor, maquina_id, maquina_config, projetos_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (nome_razao_social,
            cpf_cnpj,
            salario,
            setor,
            maquina_id,
            maquina_config,
            projetos_id)
    cursor.execute(sql, data)
    connection.commit()
    funcionario_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Funcionário cadastrado com ID ", funcionario_id)

#Exibir funcionários
def read_funcionarios(conn):
    connection = conn
    cursor = connection.cursor()
    sql = "SELECT * FROM FUNCIONARIOS"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for result in results:
        print(result)

#Atualizar funcionário
def update_funcionarios(nome_razao_social, cpf_cnpj, salario, setor, maquina_id, maquina_config, projetos_id, id, conn): 
    connection = conn 
    cursor = connection.cursor() 
    sql = "UPDATE FUNCIONARIOS SET NOME_RAZAO_SOCIAL=%s, CPF_CNPJ=%s, SALARIO=%s, SETOR=%s, MAQUINA_ID=%s, MAQUINA_CONFIG=%s, PROJETOS_ID=%s WHERE ID=%s"
    data = ( 
        nome_razao_social,
        cpf_cnpj,
        salario,
        setor,
        maquina_id,
        maquina_config,
        projetos_id,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados") 

#Excluir funcionário
def delete_funcionarios(id, conn): 
    connection = conn
    cursor = connection.cursor()
    sql = "DELETE FROM FUNCIONARIOS WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")



#Inserir fatura
def insert_faturas(pago_status, valor, data_criacao, data_quitacao, conn):
    connection = conn
    cursor = connection.cursor()
    sql = "INSERT INTO FATURAS (pago_status, valor, data_criacao, data_quitacao) VALUES (%s, %s, %s, %s)"
    data = (pago_status, valor, data_criacao, data_quitacao)
    cursor.execute(sql, data)
    connection.commit()
    fatura_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Fatura cadastrada com ID ", fatura_id)

#Exibir faturas
def read_faturas(conn):
    connection = conn
    cursor = connection.cursor()
    sql = "SELECT * FROM FATURAS"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for result in results:
        print(result)

#Atualizar faturas
def update_faturas(pago_status, valor, data_criacao, data_quitacao, id, conn): 
    connection = conn 
    cursor = connection.cursor() 
    sql = "UPDATE FATURAS SET pago_status=%s, VALOR=%s, DATA_CRIACAO=%s, DATA_QUITACAO=%s WHERE ID=%s"
    data = ( 
        pago_status,
        valor,
        data_criacao,
        data_quitacao,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados") 

#Excluir faturas
def delete_faturas(id, conn): 
    connection = conn
    cursor = connection.cursor()
    sql = "DELETE FROM FATURAS WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")    

def main():
    if not criarBD("localhost", "root", "admin", "eclipsepi"):
        criarTabelas("localhost","root", "admin", "eclipsepi")
    time.sleep(2)

    while True:
        os.system("cls") 
        print(''':::::: GERENCIADOR DE CADASTROS ::::::
              
1 - Clientes
2 - Projetos 
3 - Funcionários
4 - Faturas
5 - Sair
              ''')

        opcao = input("Digite a opção desejada: ") 

        if opcao == "1":
            while True: 
                print('''
1 - Cadastrar Cliente
2 - Exibir Clientes
3 - Atualizar Cliente 
4 - Excluir Cliente
5 - Sair
                      ''') 
                opcao_cliente = input("Digite a opção desejada: ")
        
                if opcao_cliente == "1":
                    nome = input("Digite o nome completo do cliente: ")
                    email = input("Digite o email do cliente: ") 
                    telefone = input("Digite o telefone do cliente: ") 
                    cnpj = input("Digite o CNPJ do cliente: ")

                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    insert_cliente(nome, email, telefone, cnpj, connection) 
                    pass

                elif opcao_cliente == "2": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    read_clientes(connection)
                    pass

                elif opcao_cliente == "3": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    clientes_id = input("Informe o ID do cliente: ")
                    nome = input("Informe o nome atualizado: ") 
                    email = input("Informe o endereço de email atualizado: ")
                    telefone = input("Informe o número de telefone atualizado: ") 
                    cnpj = input("Informe o CNPJ atualizado: ") 
                    update_clientes(nome, email, telefone, cnpj, clientes_id, connection) 
                    pass

                elif opcao_cliente == "4": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    id_cliente = input("Informe o ID do cliente: ") 
                    delete_clientes(id_cliente, connection)
                    pass

                elif opcao_cliente == "5":
                    break   
         
        
        elif opcao == "2":
            while True: 
                print('''
1 - Cadastrar Projeto
2 - Exibir Projetos
3 - Atualizar Projeto
4 - Excluir Projeto
5 - Sair
                      ''') 
                opcao_projeto = input("Digite a opção desejada: ")

                if opcao_projeto == "1":
                    nome = input("Digite o nome do projeto: ")
                    descricao = input("Digite a descrição do projeto: ") 
                    data_inicio = input("Digite a data de início do projeto (AAAA-MM-DD): ") 
                    data_fim = input("Digite a data final do projeto (AAAA-MM-DD): ")
                    clientes_id = input("Digite o ID do cliente atrelado ao projeto: ") 

                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    insert_projetos(nome, descricao, data_inicio, data_fim, clientes_id, connection)
                    pass 

                elif opcao_projeto == "2": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    read_projetos(connection)
                    pass

                elif opcao_projeto == "3": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    id_projeto = input("Informe o ID do projeto: ")
                    nome = input("Informe o nome atualizado: ") 
                    descricao = input("Informe a descrição atualizada: ")
                    data_inicio = input("Informe a data de início atualizada (AAAA-MM-DD): ") 
                    data_fim = input("Informe a data final atualizada (AAAA-MM-DD): ") 
                    clientes_id = input("Informe o ID atualizado do cliente: ") 
                    update_projetos(nome, descricao, data_inicio, data_fim, clientes_id, id_projeto, connection) 
                    pass

                elif opcao_projeto == "4": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    id_projeto = input("Informe o ID do projeto: ") 
                    delete_projetos(id_projeto, connection)
                    pass

                elif opcao_projeto == "5":
                    break   

    
        elif opcao == "3":
            while True: 
                print('''
1 - Cadastrar Funcionário
2 - Exibir Funcionários
3 - Atualizar Funcionário
4 - Excluir Funcionário
5 - Sair
                      ''') 
                opcao_funcionario = input("Digite a opção desejada: ")

                if opcao_funcionario == "1":
                    nome_razao_social = input("Digite o nome ou razão social do funcionário: ")
                    cpf_cnpj = input("Digite o CPF/CNPJ do funcionário: ") 
                    salario = input("Digite o salário do funcionário: ") 
                    setor = input("Digite o setor em que o funcionário trabalha: ")
                    maquina_id = input("Digite o ID da máquina a ser utilizada: ")
                    maquina_config = input("Digite o ID da configuração da máquina: ")
                    projetos_id = input("Digite o ID do projeto relacionado ao funcionário: ") 

                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    insert_funcionarios(nome_razao_social, cpf_cnpj, salario, setor, maquina_id, maquina_config, projetos_id, connection)
                    pass 
        
                elif opcao_funcionario == "2": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    read_funcionarios(connection)
                    pass
        
                elif opcao_funcionario == "3": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    id_funcionario = input("Informe o ID do funcionário: ")
                    nome_razao_social = input("Informe o nome/razão social atualizado: ") 
                    cpf_cnpj = input("Informe o CPF/CNPJ atualizado: ")
                    salario = input("Informe o salário atualizado: ")
                    setor = input("Informe o setor atualizado: ") 
                    maquina_id = input("Informe o ID atualizado da máquina: ") 
                    maquina_config = input("Informe a configuração atualizada da máquina: ")
                    projetos_id = input("Informe o ID atualizado do projeto relacionado ao funcionário: ") 
                    update_funcionarios(nome_razao_social, cpf_cnpj, salario, setor, maquina_id, maquina_config, projetos_id, id_funcionario, connection) 
                    pass
        
                elif opcao_funcionario == "4": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    id_funcionario = input("Informe o ID do funcionário: ") 
                    delete_funcionarios(id_funcionario, connection)
                    pass

                elif opcao_funcionario == "5":
                    break

        elif opcao == "4": 
            while True:
                print('''
1 - Cadastrar Fatura
2 - Exibir Faturas
3 - Atualizar Fatura
4 - Excluir Fatura
5 - Sair
                      ''') 
                opcao_fatura = input("Digite a opção desejada: ")

                if opcao_fatura == "1":
                    pago_status = input("Digite o status de pagamento (0, 1): ")
                    valor = input("Digite o valor da fatura: ") 
                    data_criacao = input("Digite a data de criação da fatura (AAAA-MM-DD): ") 
                    data_quitacao = input("Digite a data de quitação da fatura (AAAA-MM-DD): ")
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    insert_faturas(pago_status, valor, data_criacao, data_quitacao, connection)
                    pass

                elif opcao_fatura == "2": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    read_faturas(connection)
                    pass
        
                elif opcao_fatura == "3": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi") 
                    id_fatura = input("Informe o ID da fatura: ")
                    pago_status = input("Informe o status de pagamento atualizado: ") 
                    valor = input("Informe o valor atualizado da fatura: ")
                    data_criacao = input("Informe a data de criação atualizada (AAAA-MM-DD): ") 
                    data_quitacao = input("Informe a data de quitação atualizada (AAAA-MM-DD): ")
                    update_faturas(pago_status, valor, data_criacao, data_quitacao, id_fatura, connection) 
                    pass
        
                elif opcao_fatura == "4": 
                    connection = conectarBD("localhost", "root", "admin", "eclipsepi")
                    id_fatura = input("Informe o ID da fatura: ") 
                    delete_faturas(id_fatura, connection)
                    pass

                elif opcao_fatura == "5": 
                    break

        elif opcao == "5":
            exit()

if __name__ == "__main__":
    main()