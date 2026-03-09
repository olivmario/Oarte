from Models.Bd import get_db_connection 

class Arte:
    def __init__(self, nome, data_criacao, data_publicacao, link_img ):
        self.nome = nome
        self.data_criacao = data_criacao
        self.data_publicacao = data_publicacao
        self.link_img = link_img

    def inserir_arte(self):
        con = get_db_connection
        cursor = con.cursor()
        insert = """Insert into artes(nome, data_criacao, data_publi, imagem) values (%s, %s, %s, %s))"""
        values = (self.nome, self.data_criacao, self.data_publicacao, self.link_img)
        cursor.execute(insert, values)

        con.commit()
        cursor.close()
        con.close()

    