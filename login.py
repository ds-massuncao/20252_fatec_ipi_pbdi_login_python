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
        password="Lub3n4TTi@#$"
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

def registar(usuario):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20252_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="Lub3n4TTi@#$"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)',
                (usuario.login, usuario.senha)
            )
        conexao.commit()
        conexao.close()
    return True
            
            
def menu():
    
    texto = '0 - Fechar Sistema\n1 - Login\n2 - Logoff\n3 - Inserir Usuario\n'
    
    usuario = None
    
    op = int(input(texto))
    
    while op != 0:
        
        if op == 1:
            login = input('Login: ')
            senha = input('Senha: ')
            usuario = Usuario(login, senha)
            print("Usuario OK!" if existe(usuario) else "Usuario Invalido!")
        
        if op == 2:
            usuario = None
            print("Logoff efetuado com sucesso!!!")
        
        
        if op == 3:
            login = input('Login: ')
            senha = input('Senha: ')
            usuario = Usuario(login, senha)
            print("Usuario Inserido" if registar(usuario) else "Erro ao inserir usuario")
            
        op = int(input(texto))
        
    else:
        print("Até mais!!!")      
        
          
menu()  
             