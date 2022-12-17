import tkinter as tk
import psycopg2 as psycopg2
import psycopg2 as OperationalError

#Trabalho Feito com 5 participantes sendo eles:
#André mateus Nogueira farias, Matricula:202001289861
#Diego Gomes Magalhes, matricula: 202002027398
#Lucas de Sousa Carreiro, matricula:202008481155
# Mateus Antonio Pontes Rocha, Matricula:202003229938#
#janela menu principal
def Menu_Principal():
    janela = tk.Tk()
    janela.title("Menu Principal")
    janela.minsize(600, 500)

    
    tk.Button(janela, text="Excluir endereco",command=excluir_edereco).grid(row=6, column=8, sticky=tk.W, pady=8)

    tk.Button(janela, text="Excluri conta",command=excluir_conta).grid(row=7, column=8, sticky=tk.W,pady=8)

    tk.Button(janela, text="Gerar novo usuario", command=Janela_cadastro).grid(row=2, column=8, sticky=tk.W, pady=4)

    tk.Button(janela, text="Cadastrar conta",command=cadastro_conta).grid(row=3, column=8, sticky=tk.W, pady=4)

    tk.Button(janela, text="Cadastrar Endereço", command=cadastra_endereco).grid(row=4,column=8, sticky=tk.W, pady=4)

    tk.Button(janela, text="Excluir usuario", command=Excluir_Cadastro).grid(row=5, column=8, sticky=tk.W, pady=8)

    tk.Button(janela, text="Pesquisa e Alteração", command=Pesquisar_Pessoa).grid(row= 9, column= 8, sticky=tk.W, pady= 10)

    tk.Button(janela, text= "Sair", command=janela.destroy).grid(row=10,column= 8, sticky=tk.W, pady= 11)


#janela de pesquisar e alterar
def Pesquisar_Pessoa():
    pesquisar = tk.Toplevel()
    pesquisar.minsize(600, 500)
    pesquisar.title("Janela de Pesquisa e Alteração")

    tk.Label(pesquisar, text="Aba de Pesquisa").grid(row=0)
    tk.Label(pesquisar, text="Pesquise a pessoa cujo quer Alterar Cadastro").grid(row=1)

    e1 = tk.Entry(pesquisar)
    e2 = tk.Entry(pesquisar)

    e1.grid(row=1, column=1)

    def search():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()
    tk.Button(pesquisar, text="Menu Principal", command=Menu_Principal).grid(row= 3, column=3, sticky=tk.W,pady=4)
    tk.Button(pesquisar, text="Pesquisar", command=search).grid(row=14, column=6,sticky=tk.W,pady=4)


#janela de excluir pessoa
def Excluir_Cadastro():
    excluir = tk.Toplevel()
    excluir.minsize(600, 500)
    excluir.title("janela de excluir")

    tk.Label(excluir, text="Excluir").grid(row=0)
    tk.Label(excluir, text="Pesquisar cliente").grid(row=1)


    e1 = tk.Entry(excluir)
    e1 = tk.Entry(excluir)

    e1.grid(row=1, column=1)

    def dell_pessoa():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''DELETE FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()

    def search():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()



    tk.Button(excluir,text="Menu principal", command=Menu_Principal).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(excluir, text="Pesquisar",command=search).grid(row=13, column=6,sticky=tk.W, pady=4)
    tk.Button(excluir, text="Excluir Pessoa", command=dell_pessoa).grid(row=14, column=6,sticky=tk.W,pady=4)
    

#janela de excluir endereço
def excluir_edereco():

    excluirendereco = tk.Toplevel()
    excluirendereco.minsize(500,500)
    excluirendereco.title("Excluir Endereco")

    tk.Label(excluirendereco, text="Aba de Pesquisa").grid(row=1)
    tk.Label(excluirendereco, text="Pesquise a pessoa cujo excluir endereço").grid(row=2)

    e1 = tk.Entry(excluirendereco)
    e2 = tk.Entry(excluirendereco)

    e1.grid(row=2, column=1)

    def dell_endereco():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''DELETE FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()

    def search():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()


    tk.Button(excluirendereco,text="Menu principal", command=Menu_Principal).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(excluirendereco, text="Pesquisar",command=search).grid(row=13, column=6,sticky=tk.W, pady=4)
    tk.Button(excluirendereco, text="Excluir Endereço", command=dell_endereco).grid(row=14, column=6,sticky=tk.W,pady=4)


#janela de excluir conta
def excluir_conta():
    excluirconta = tk.Toplevel()
    excluirconta.minsize(500,500)
    excluirconta.title("Excluir Conta")

    tk.Label(excluirconta, text="Aba de Pesquisa").grid(row=0)
    tk.Label(excluirconta, text="Pesquisar a conta que deve ser excluida").grid(row=1)

    e1 = tk.Entry(excluirconta)
    e2 = tk.Entry(excluirconta)

    e1.grid(row=1, column=1)



    
    def search():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()


    def dell_conta():
        id=e1.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''DELETE FROM pessoa where id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()
        print(row)


        conn.commit()
        conn.close()

    tk.Button(excluirconta,text="Menu principal", command=Menu_Principal()).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(excluirconta, text="Pesquisar",command=search).grid(row=13, column=6,sticky=tk.W, pady=4)
    tk.Button(excluirconta, text="Excluir conta", command=dell_conta).grid(row=14, column=6,sticky=tk.W,pady=4)

def Janela_cadastro():
    cadastro = tk.Toplevel()
    cadastro.minsize(600, 500)
    cadastro.title("Cadastro de Pessoa e Conta")

    tk.Label(cadastro, text="CPF").grid(row=0)
    tk.Label(cadastro, text="PrimeirNome").grid(row=1)
    tk.Label(cadastro, text="Sobrenome").grid(row=2)
    tk.Label(cadastro, text="Meionome").grid(row=3)
    tk.Label(cadastro, text="Idade").grid(row=4)
    tk.Label(cadastro, text="Peso").grid(row=5)


    e1 = tk.Entry(cadastro)
    e2 = tk.Entry(cadastro)
    e3 = tk.Entry(cadastro)
    e4 = tk.Entry(cadastro)
    e5 = tk.Entry(cadastro)
    e6 = tk.Entry(cadastro)
   

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    
    def save_new_pessoa():
        cpf=e1.get()
        primeironome=e2.get()
        sobrenome=e3.get()
        meionome=e4.get()
        idade=int(e5.get())
        peso=float(e6.get())
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = f'''INSERT INTO Pessoa(cpf, primeironome, meionome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (cpf, primeironome, meionome, sobrenome, idade, peso))
        print("succesfully data inserted")
        conn.commit()
        conn.close()

    tk.Button(cadastro,text="Menu principal", command=Menu_Principal).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(cadastro, text="Salvar", command=save_new_pessoa).grid(row=11,column=6,sticky=tk.W,pady=4)

    #agora é a parte de cadastro da conta

def cadastro_conta():
    conta = tk.Toplevel()
    conta.minsize(600, 500)
    conta.title("Janela de cadastro de conta")

    tk.Label(conta, text="Numero da Conta").grid(row=5)
    tk.Label(conta, text="Agencia").grid(row=6)
    tk.Label(conta, text="Saldo").grid(row=7)
    tk.Label(conta, text="Gerente").grid(row=8)
    tk.Label(conta, text="Titular").grid(row=9)
    tk.Label(conta, text="estado").grid(row=10)


    e6 = tk.Entry(conta)
    e7 = tk.Entry(conta)
    e8 = tk.Entry(conta)
    e9 = tk.Entry(conta)
    e10 = tk.Entry(conta)
    e11 = tk.Entry(conta)

    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    e9.grid(row=8, column=1)
    e10.grid(row=9, column=1)
    e11.grid(row=10, column=1)

    def save_new_conta():
        numero=e6.get()
        agencia=e7.get()
        saldo=e8.get()
        gerente=e9.get()
        titular=e10.get()
        estado=e11.get()
        conn = psycopg2.connect(dbname="banco", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = f'''INSERT INTO Conta(numero, agencia, saldo ,gerente, titular, estado) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (numero, agencia, saldo, gerente,titular, estado))
        print("succesfully data inserted")
        conn.commit()
        conn.close()

    tk.Button(conta,text="Menu principal", command=Menu_Principal).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(conta, text="Salvar", command=save_new_conta).grid(row=11,column=6,sticky=tk.W,pady=4)


def cadastra_endereco():
    endereco = tk.Toplevel()
    endereco.minsize(600,500)
    endereco.title("Cadastro de Endereço")

    tk.Label(endereco, text="Rua").grid(row=0)
    tk.Label(endereco, text="Numero").grid(row=1)
    tk.Label(endereco, text="Bairro").grid(row=2)
    tk.Label(endereco, text="CEP").grid(row=3)
    tk.Label(endereco, text="Cidade/Estado").grid(row=4)

    a1 = tk.Entry(endereco)
    a2 = tk.Entry(endereco)
    a3 = tk.Entry(endereco)
    a4 = tk.Entry(endereco)
    a5 = tk.Entry(endereco)

    a1.grid(row=0, column=1)
    a2.grid(row=1, column=1)
    a3.grid(row=2, column=1)
    a4.grid(row=3, column=1)
    a5.grid(row=4, column=1)

    def save_new_endereco():
        rua=a1.get()
        numero=a2.get()
        bairro=a3.get()
        cep=a4.get()
        cidade=a5.get()
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password="admin157", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        query = '''INSERT INTO Endereco(rua, numero, bairro, cep, cidade) VALUES (%s, %s, %s, %s, %s)'''
        cursor.execute(query, (rua, numero, bairro, cep, cidade))
        print("succesfully data inserted")
        conn.commit()
        conn.close()

    tk.Button(endereco,text="Menu principal", command=Menu_Principal).grid(row=12, column=6, sticky=tk.W, pady=4)
    tk.Button(endereco,text="Salvar",command=save_new_endereco).grid(row=13,column=6, sticky=tk.W,pady=5)





janela = tk.Tk()
janela.title("Menu Principal")
janela.minsize(600, 500)



tk.Button(janela, text="Excluir endereco",command=excluir_edereco).grid(row=6, column=8, sticky=tk.W, pady=8)

tk.Button(janela, text="Excluir conta",command=excluir_conta).grid(row=7, column=8, sticky=tk.W,pady=8)

tk.Button(janela, text="Gerar novo usuario", command=Janela_cadastro).grid(row=2, column=8, sticky=tk.W, pady=4)

tk.Button(janela, text="Cadastrar conta",command=cadastro_conta).grid(row=3, column=8, sticky=tk.W, pady=4)

tk.Button(janela, text="Cadastrar Endereço", command=cadastra_endereco).grid(row=4,column=8, sticky=tk.W, pady=4)

tk.Button(janela, text="Excluir usuario", command=Excluir_Cadastro).grid(row=5, column=8, sticky=tk.W, pady=8)

tk.Button(janela, text="Pesquisa e Alteração", command=Pesquisar_Pessoa).grid(row= 9, column= 8, sticky=tk.W, pady= 10)

tk.Button(janela, text= "Sair", command=janela.destroy).grid(row=10,column= 8, sticky=tk.W, pady= 11)

janela.mainloop()