# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#Importando a main
from main import *


#cores
cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # Branca   
cor2 = "#e5e5e5"  # grey
cor3 = "#00a095"  # Verde
cor4 = "#403d3d"   # letra
cor6 = "#003452"   # azul
cor7 = "#ef5350"   # vermelha

cor6 = "#146C94"   # azul
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # + verde


#janela

janela = Tk()
janela.title()
janela.geometry('810x535')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)


style = Style(janela)
style.theme_use("clam")

#Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=cor6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky= NSEW, columnspan=5)


frame_botoes = Frame(janela,width=100, height=200, bg=cor1, relief=RAISED )
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes= Frame(janela,width=800, height=100, bg=cor1, relief=SOLID )
frame_detalhes.grid(row=1, column=1, pady=1,padx=10, sticky=NSEW)


frame_tabela= Frame(janela,width=800, height=100, bg=cor1, relief=SOLID )
frame_tabela.grid(row=3, column=0, pady=0,padx=10, sticky=NSEW, columnspan=5)



# Trabalhando no frame logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('icones/logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)

app_logo = Label(frame_logo, image=app_lg, text=' Sistema de Registro de Alunos', width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=cor6, fg=cor1)
app_logo.place(x=5, y=0)

#Abrir Imagem

imagem = Image.open('icones/logo.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
l_imagem.place(x=390, y=10)


# -------------------------------------
# Função Adicionar
# -------------------------------------
def adicionar():
    global imagem, imagem_string, l_imagem

    try:
        # Obtendo os valores
        nome = e_nome.get().strip()
        email = e_email.get().strip()
        tel = e_telefone.get().strip()
        sexo = c_sexo.get().strip()
        data = data_nascimento.get().strip()
        endereco = e_endereco.get().strip()
        curso = c_curso.get().strip()
        img = imagem_string

        lista = [nome, email, tel, sexo, data, endereco, curso, img]

        # Verifica campos vazios
        if any(i == '' for i in lista):
            messagebox.showerror('Erro', 'Preencha todos os campos antes de adicionar.')
            return

        # Registra o aluno
        sistema_de_registro.Registrar_estudante(lista)
        messagebox.showinfo('Sucesso', f'Aluno "{nome}" adicionado com sucesso!')

        # Limpa os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        mostrar_aluno()

    except Exception as e:
        messagebox.showerror('Erro ao adicionar', f'Ocorreu um erro: {e}')


# -------------------------------------
# Função Procurar
# -------------------------------------
def procurar():
    global imagem, imagem_string, l_imagem

    try:
        id_texto = e_procurar.get().strip()
        if not id_texto.isdigit():
            messagebox.showerror("Erro", "Digite um ID numérico válido.")
            return

        id_aluno = int(id_texto)
        dados = sistema_de_registro.buscar_estudante(id_aluno)

        if not dados:
            messagebox.showwarning("Aviso", f"Nenhum aluno encontrado com o ID {id_aluno}.")
            return

        # Limpa os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        # Insere os dados retornados
        e_nome.insert(END, dados[1])
        e_email.insert(END, dados[2])
        e_telefone.insert(END, dados[3])
        c_sexo.insert(END, dados[4])
        data_nascimento.insert(END, dados[5])
        e_endereco.insert(END, dados[6])
        c_curso.insert(END, dados[7])

        imagem = dados[8]
        imagem_string = imagem

        try:
            img = Image.open(imagem)
            img = img.resize((130, 130))
            img = ImageTk.PhotoImage(img)
            l_imagem = Label(frame_detalhes, image=img, bg=cor1)
            l_imagem.image = img
            l_imagem.place(x=390, y=10)
        except Exception:
            messagebox.showwarning("Aviso", "Imagem não encontrada ou inválida.")

    except Exception as e:
        messagebox.showerror("Erro ao procurar aluno", f"Ocorreu um erro: {e}")


# -------------------------------------
# Função Atualizar
# -------------------------------------
def atualizar():
    global imagem, imagem_string, l_imagem

    try:
        id_texto = e_procurar.get().strip()
        if not id_texto.isdigit():
            messagebox.showerror("Erro", "Digite um ID numérico válido.")
            return

        id_aluno = int(id_texto)

        nome = e_nome.get().strip()
        email = e_email.get().strip()
        tel = e_telefone.get().strip()
        sexo = c_sexo.get().strip()
        data = data_nascimento.get().strip()
        endereco = e_endereco.get().strip()
        curso = c_curso.get().strip()
        img = imagem_string

        lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

        if any(i == '' for i in lista[:-1]):  # ignora o id na checagem
            messagebox.showerror('Erro', 'Preencha todos os campos antes de atualizar.')
            return

        sistema_de_registro.atualizar_estudante(lista)
        messagebox.showinfo('Sucesso', f'Aluno "{nome}" atualizado com sucesso!')

        # Limpa os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        imagem_string = imagem
        img = Image.open('icones/logo.png')
        img = img.resize((130, 130))
        img = ImageTk.PhotoImage(img)

        l_imagem = Label(frame_detalhes, image=img, bg=cor1)
        l_imagem.image = img
        l_imagem.place(x=390, y=10)

        mostrar_aluno()

    except Exception as e:
        messagebox.showerror('Erro ao atualizar', f'Ocorreu um erro: {e}')


# -------------------------------------
# Função Deletar
# -------------------------------------
def Deletar():
    global imagem, imagem_string, l_imagem

    try:
        id_texto = e_procurar.get().strip()
        if not id_texto.isdigit():
            messagebox.showerror("Erro", "Digite um ID numérico válido.")
            return

        id_aluno = int(id_texto)

        confirmar = messagebox.askyesno("Confirmar", f"Tem certeza que deseja deletar o aluno ID {id_aluno}?")
        if not confirmar:
            return

        sistema_de_registro.deletar_estudante(id_aluno)
        messagebox.showinfo("Sucesso", f"Aluno com ID {id_aluno} deletado com sucesso.")

        # Limpa os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        c_sexo.delete(0, END)
        data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)
        e_procurar.delete(0, END)

        imagem_string = imagem
        img = Image.open('icones/logo.png')
        img = img.resize((130, 130))
        img = ImageTk.PhotoImage(img)

        l_imagem = Label(frame_detalhes, image=img, bg=cor1)
        l_imagem.image = img
        l_imagem.place(x=390, y=10)

        mostrar_aluno()

    except Exception as e:
        messagebox.showerror('Erro ao deletar', f'Ocorreu um erro: {e}')







#Criando os campos de entrada
l_nome = Label(frame_detalhes, text='Nome *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_nome.place(x=4, y=10)

e_nome = Entry(frame_detalhes, width=30, justify=LEFT, relief=SOLID)
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text='Email *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_email.place(x=4, y=70)

e_email = Entry(frame_detalhes, width=30, justify=LEFT, relief=SOLID)
e_email.place(x=7, y=100)

l_telefone = Label(frame_detalhes, text='Telefone *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_telefone.place(x=4, y=130)

e_telefone = Entry(frame_detalhes, width='15', justify=LEFT, relief=SOLID)
e_telefone.place(x=7, y=160)


# Label Box

l_sexo = Label(frame_detalhes, text='Sexo *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify=CENTER)
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)


l_data_nascimento = Label(frame_detalhes, text='Data de nascimento *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_detalhes, width=18, justify='center', bg= 'darkblue', foreground='white', borderwidth=2, year=2025 )
data_nascimento.place(x=224, y=40)


l_endereco = Label(frame_detalhes, text='Endereço *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_endereco.place(x=220, y=70)

e_endereco = Entry(frame_detalhes, width='15', justify=LEFT, relief=SOLID)
e_endereco.place(x=224, y=100) 


cursos = [
    'Administração',
    'Agronomia',
    'Análise e Desenvolvimento de Sistemas',
    'Arquitetura e Urbanismo',
    'Biomedicina',
    'Ciência da Computação',
    'Ciência de Dados',
    'Ciências Biológicas',
    'Ciências Contábeis',
    'Contabilidade',
    'Design de Interiores',
    'Design Gráfico',
    'Direito',
    'Economia',
    'Educação Física',
    'Enfermagem',
    'Engenharia Aeroespacial',
    'Engenharia Ambiental',
    'Engenharia Civil',
    'Engenharia de Materiais',
    'Engenharia de Produção',
    'Engenharia de Software',
    'Engenharia Elétrica',
    'Engenharia Florestal',
    'Engenharia Mecânica',
    'Engenharia Naval',
    'Engenharia Química',
    'Farmácia',
    'Física',
    'Fisioterapia',
    'Gastronomia',
    'Geografia',
    'Geologia',
    'Gestão de Recursos Humanos',
    'História',
    'Hotelaria',
    'Jornalismo',
    'Letras',
    'Licenciatura em Matemática',
    'Logística',
    'Marketing',
    'Matemática',
    'Medicina',
    'Moda',
    'Nutrição',
    'Oceanografia',
    'Odontologia',
    'Pedagogia',
    'Psicologia',
    'Publicidade e Propaganda',
    'Química',
    'Relações Internacionais',
    'Relações Públicas',
    'Segurança da Informação',
    'Serviço Social',
    'Sistemas de Informação',
    'Teologia',
    'Tecnologia da Informação',
    'Turismo',
    'Veterinária',
    'Zootecnia'
]


l_curso = Label(frame_detalhes, text='Cursos *',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'), justify=CENTER)
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)


# função para escolher imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar de foto'




botao_carregar = Button(frame_detalhes, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor1, fg=cor0)
botao_carregar.place(x=390, y=160)



# Tabela Alunos
def mostrar_aluno():

    cabecalho = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    df_list = sistema_de_registro.ver_estudantes()
    
    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=cabecalho, show='headings')
 
    # Barra Vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)
    # Barra horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)


    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd = ['nw','nw','nw','center','center','center','center','center','center']
    h =[40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0


    for col in cabecalho:
        tree_aluno.heading(col, text=col.title(), anchor=NW)

        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1


    for item in df_list:
        tree_aluno.insert('', 'end', values=item)




# Procurar aluno ------

frame_procurar = Frame(frame_botoes, width=40, height=55, bg=cor1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky= NSEW)

l_nome = Label(frame_procurar, text='Procurar aluno [Entrar ID]',anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4 )
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky= NSEW)

e_procurar  = Entry(frame_procurar, width='5', justify='center', relief='solid',font=('Ivy 10') )
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky= NSEW)


botao_procurar = Button(frame_procurar, command=procurar, text='Procurar'.upper(), width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor1, fg=cor0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky= NSEW)

#Botoes -------

#Botão Adicionar
app_img_adicionar = Image.open('icones/adicionar.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)

botao_adicionar = Button(frame_botoes,command=adicionar, image=app_img_adicionar, text='Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0, relief=GROOVE)
botao_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky= NSEW)
#Botão Atualizar
app_img_atualizar = Image.open('icones/atualizar.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)

botao_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, text='Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0, relief=GROOVE)
botao_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky= NSEW)
#Botão Deletar
app_img_deletar = Image.open('icones/deletar.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)

botao_deletar = Button(frame_botoes, command=Deletar, image=app_img_deletar, text='Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0, relief=GROOVE)
botao_deletar.grid(row=3, column=0, pady=5, padx=10, sticky= NSEW)


#Linha vertical de separação

l_linha = Label(frame_botoes, image=app_img_deletar, width=1, height=223, font=('Ivy 1'), bg=cor1, fg=cor1, relief=GROOVE, anchor=NW)
l_linha.place(x=235, y=15)









mostrar_aluno()

janela.mainloop()