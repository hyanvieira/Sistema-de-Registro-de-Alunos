import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       telefone TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       curso TEXT NOT NULL,
                       picture TEXT NO NULL)''')
        
    def Registrar_estudante(self, estudantes):    
        self.c.execute("INSERT INTO estudantes(nome, email, telefone, sexo, data_nascimento, endereco, curso, picture) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                        (estudantes))
        self.conn.commit()



        #Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')


    def ver_estudantes(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()
        return dados
    def buscar_estudante(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados
        
    def atualizar_estudante(self, nova_valores):
        query = "UPDATE estudantes SET nome=?, email=?, telefone=?,sexo=? , data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, nova_valores)
        self.conn.commit()

        #Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Estudante com ID:{nova_valores[8]} foi atualizado!')


    def deletar_estudante(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id, ))
        self.conn.commit()

        #Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Estudante com ID:{id} foi Deletado!')


#Criando uma instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# informações
#estudante = ('Elena', 'elena@gmail.com', '(11) 40028922', 'F', '06/05/2005', 'Portugal, Lisboa', 'Medicina', 'imagem2.png')

#sistema_de_registro.Registrar_estudante(estudante)


# Ver os estudantes
# #sistema_de_registro.ver_estudantes()

# # Procurar alunos

# #aluno = sistema_de_registro.buscar_estudante(3)

# # Atualizar aluno

# #aluno = sistema_de_registro.atualizar_estudante(estudante)

# # Deletar estudante

# #sistema_de_registro.deletar_estudante(2)
# sistema_de_registro.ver_estudantes()










