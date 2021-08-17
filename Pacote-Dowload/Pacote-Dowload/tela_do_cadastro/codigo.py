def esqueceuasenha(oeme):
    """
    :param oeme: o eme.get()
    :return:
    """
    server = 0
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use login;")
    mcursor.execute("select * from recup;")
    rows = mcursor.fetchall()
    for row in rows:
        if row[1] == 0:
            server = row[0]
            print("Achei!!!")
            break
        else:
            print("Cheio...")
    try:
        mcursor.execute(f"select id from logi where email = '{oeme}';")
        rows = mcursor.fetchall()
    except:
        print("Email inválido")
    else:
        if len(rows) == 0:
            return 0
        elif server == 0:
            print("Servidores Cheios!!!")
        else:
            for row in rows:
                for i in row:
                    mcursor.execute(f"update recup set conta = '{i}' where servidor = '{server}'")
                    print("Código enviado!!!")
            return 1
