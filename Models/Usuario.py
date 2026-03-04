from app import get_db_connection


class Usuario:

    def __init__(self, nome, email, senha, idade):
        
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade


    def cadastrar_usuario(self):
        con = get_db_connection()
        cursor = con.cursor()
        insert  = """Insert into usuarios (nome, idade, email, senha) values (%s, %s, %s, %s)"""
        values = (self.nome, self.idade, self.email, self.senha)
        cursor.execute(insert, values)
        con.commit()
        cursor.close()
        con.close()


    def buscar_idade(self):

        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("Select nome, idade from usuarios order by idade desc")
        lista_idade = cursor.fetchall()

        cursor.close()
        con.close()

        return lista_idade
