import psycopg
print (psycopg)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe (usuario):
#Abre a conexão
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20252_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="pLub3n4TTi@#$"
    ) as conexao:
        #obtém um cursor
        with conexao.cursor() as cursor:
                #executa o comando
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', (f'{usuario.login}',
            f'{usuario.senha}'))
            #obtém o resultado
            result = cursor.fetchone()
            #verifica se o resultado é diferente de None, o
            #que indica que o usuário existe na base
    return result != None

            
