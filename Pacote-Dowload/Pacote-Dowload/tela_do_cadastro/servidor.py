import mysql.connector
import enviar
from time import sleep
from sys import stdout
cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
mcursor = cnx.cursor()
mcursor.execute("use login;")
aemail = anome = asenha = ""
sec = minu = hor = 0
try:
    while True:
        mcursor.execute("select * from recup;")
        rows = mcursor.fetchall()
        for row in rows:
            if row[1] != 0:
                mcursor.execute(f"select email, nome, senha from logi where id = '{row[1]}'")
                server = row[0]
                rows = mcursor.fetchall()
                for row in rows:
                    aemail = row[0]
                    anome = row[1]
                    asenha = row[2]
                    enviar.enviaremail(aemail, anome, asenha)
                    mcursor.execute(f"update recup set conta = '0' where servidor = '{server}'")
            else:
                if sec == 60:
                    minu += 1
                    sec = 0
                if minu == 60:
                    hor += 1
                    minu = 0
                stdout.write(f"\r{hor}:{minu}:{sec}")
                sleep(1)
                sec += 1
except KeyboardInterrupt:
    print("\nPrograma Finalizado")
