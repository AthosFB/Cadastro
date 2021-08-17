from tkinter import *
import codigo
import verificação_de_conta
import mysql.connector
import os
os.system(r"start D:\Git-e-GitHub\Cadastro\Pacote-Dowload\wamp64\wampmanager")
cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
mcursor = cnx.cursor()
a = 0


def cadastrar():

    def fim():
        cdg = conf.get()
        verificação_de_conta.validador(email, cdg)
        janela.geometry("400x400")
        cancel = Label(janela, text="Conta Criada com Sucesso!                                                        ")
        cancel.place(x=150, y=350)
    email = eme.get()
    nome = nom.get()
    senha = sen.get()
    if nome.strip() == "" or senha.strip() == "" or email.strip() == "":
        erro = Label(janela, text="(Login/Senha/Eamil) inválidos!")
        erro.place(x=150, y=330)
    else:
        try:
            verificação_de_conta.verificacao(email, nome, senha)
        except:
            erro = Label(janela, text="Login ou Email de usuário ja em uso!")
            erro.place(x=150, y=330)
        else:
            janela.title("Email de Verificação!")
            janela.geometry("500x500")
            txt = Label(janela, text="Um Email foi enviado por favor digite o código aqui!")
            txt.place(x=150, y=350)
            conf = Entry(janela)
            conf.place(x=150, y=400)
            bot = Button(janela, width=16, text="Ok", command=fim)
            bot.place(x=150, y=450)


def entrar():
    mcursor.execute("use login;")
    mcursor.execute("select email, nome, senha from logi;")
    rows = mcursor.fetchall()
    cont = 0
    for row in rows:
        if row[0] == eme.get() and row[1] == nom.get() and row[2] == sen.get():
            cont += 1
    if cont == 1:
        janela.destroy()
        teste = Tk()
        teste.geometry("1920x1080")
        fazendo = Label(teste, text="Em Construção Aguarde!")
        fazendo.place(x=920, y=500)
        teste.mainloop()
    else:
        fazendo = Label(janela, text="Aconteceu algo de Errado!")
        fazendo.place(x=150, y=330)


def excluir():
    mcursor.execute("use login;")
    mcursor.execute("select email, nome, senha from logi;")
    rows = mcursor.fetchall()
    cont = 0
    for row in rows:
        if row[0] == eme.get() and row[1] == nom.get() and row[2] == sen.get():
            cont += 1
    if cont == 1:
        mcursor.execute(f"delete from logi where nome = '{nom.get()}'")
        fazendo = Label(janela, text="Conta Deletada Com Sucesso!")
        fazendo.place(x=150, y=330)
    else:
        fazendo = Label(janela, text="Senha, Login, ou email inválido!")
        fazendo.place(x=150, y=330)


def esqueceuasenha():

    def teste():

        def destruir():
            enviar.destroy()

        if codigo.esqueceuasenha(email.get()) == 1:
            resp = Label(enviar, text="Um email foi enviado!                                           ")
            resp.place(x=330, y=100)
            resp = Label(enviar, text="Verifique a caixa de spam!                                      ")
            resp.place(x=330, y=150)
            resp = Label(enviar, text="Caso ele não seja enviado em 5 minutos,                         ")
            resp.place(x=330, y=200)
            resp = Label(enviar, text="clique novamente em Esquecia a senha                            ")
            resp.place(x=330, y=250)
            bot = Button(enviar, text="Entendi!", command=destruir)
            bot.place(x=330, y=300)
        else:
            erro = Tk()
            text = Label(erro, text="Email Não cadastrado!!!                  ")
            text.place(x=30, y=60)
            erro.mainloop()
    enviar = Tk()
    enviar.title("Senha")
    enviar.geometry("960x540")
    email = Entry(enviar)
    email.place(x=150, y=100)
    text = Label(enviar, text="Email da Conta: ")
    text.place(x=50, y=100)
    bot = Button(enviar, text="Enviar Código", command=teste)
    bot.place(x=150, y=140)
    enviar.mainloop()


# Programa Principal
janela = Tk()
janela.title("Cadastrar")
janela.geometry("400x400")
princi = Label(janela, text="Coloque seus dados para entrar ou se cadastrar!")
princi.place(x=90, y=30)
info0 = Label(janela, text="email: ")
info0.place(x=100, y=70)
info1 = Label(janela, text="Login: ")
info1.place(x=100, y=120)
info2 = Label(janela, text="Senha: ")
info2.place(x=100, y=170)
eme = Entry(janela)
eme.place(x=150, y=70)
nom = Entry(janela)
nom.place(x=150, y=120)
sen = Entry(janela)
sen.place(x=150, y=170)
but = Button(janela, width=16, text="Cadastrar", command=cadastrar)
but.place(x=220, y=220)
but = Button(janela, width=16, text="Entrar", command=entrar)
but.place(x=90, y=220)
but = Button(janela, width=16, text="Excluir Conta", command=excluir)
but.place(x=160, y=260)
but = Button(janela, width=16, text="Esquecia a senha", command=esqueceuasenha)
but.place(x=160, y=300)
janela.mainloop()
