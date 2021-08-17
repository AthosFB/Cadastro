def verificacao(email, nome, senha):
    import enviar
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    from random import randint
    codigo = list()
    for i in range(0, 6):
        codigo.append(randint(0, 9))
    codigo = str(codigo)
    codigo = codigo.replace("[", "")
    codigo = codigo.replace("]", "")
    codigo = codigo.replace(",", "")
    codigo = codigo.replace(" ", "")
    mcursor.execute("use login;")
    mcursor.execute(f"insert into conf value (default, '{email}', '{nome}', '{senha}', '{codigo}');")
    enviar.enviarconfirm(email, codigo)


def validador(email, codigo):
    codigo = str(codigo).strip().replace(" ", "")
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use login;")
    mcursor.execute(f"select * from conf where email = '{email}';")
    rows = mcursor.fetchall()
    if len(rows) == 0:
        print("Erro!!!")
    else:
        if rows[0][4] == codigo:
            mcursor.execute("use login;")
            mcursor.execute(f"insert into logi value (default, '{rows[0][1]}', '{rows[0][2]}', '{rows[0][3]}');")
            mcursor.execute(f"delete from conf where email = '{rows[0][1]}'")
            print("CONTA ADICIONADA!")
        else:
            print("Código inválido!")
