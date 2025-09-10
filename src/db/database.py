import mysql.connector
from mysql.connector import Error

def testar_conexao():
    """Testa a conexão com o servidor MySQL e a existência do banco de dados 'agendai'."""
    try:
        # Tenta se conectar apenas ao servidor, sem especificar o banco de dados
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        # Se a conexão com o servidor for bem-sucedida
        if conn.is_connected():
            print("Conexão com o servidor MySQL bem-sucedida!")

            # Verifica se o banco de dados 'agendai' existe
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES LIKE 'agendai'")
            database_exists = cursor.fetchone()

            if database_exists:
                print("O banco de dados 'agendai' já existe.")
                return True
            else:
                print("O banco de dados 'agendai' não foi encontrado. Por favor, crie-o.")
                return False

    except Error as e:
        # Se ocorrer um erro, ele será capturado aqui
        print(f"Erro ao conectar com o MySQL: {e}")
        return False

    finally:
        # Garante que a conexão seja fechada, mesmo se houver um erro
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexão com o MySQL fechada.")

# @app.route('/')
# def index():
#     conn = get_mysql_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     results = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return str(results)

# Chamada da função para testar
if __name__ == '__main__':
    if testar_conexao():
        print("Você pode prosseguir com seu projeto!")
    else:
        print("A conexão falhou. Verifique as credenciais ou a existência do banco de dados.")