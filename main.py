import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import abil_azul

from tkinter import PhotoImage
from model import Model
from ttkbootstrap import Style
style = Style(theme='litera')



class App:
    def __init__(self, root):
        self.madruga = Model()
        self.janela = root.get_object("login")
        

        self.botao=root.get_object("login_entrar_botao")

        self.botao.configure(style='primary.Outline.TButton')

        self.botao2=root.get_object("login_cancelar_botao")
        self.botao2.configure(style='primary.TButton')
        
        self.logo=root.get_object("logo")
        self.logo_img = PhotoImage(name='logo',file='img/logo.png')
       
        self.logo['image']=self.logo_img
       

        self.login_matricula_entry=root.get_object("login_matricula_entry")
        self.login_senha_entry=root.get_object("login_senha_entry")
        self.cvar="asd"

        

    def logar(self):
        matricola = self.login_matricula_entry.get()
        senha = self.login_senha_entry.get()


        self.usuario = self.madruga.buscar_usuario(matricola,senha)
        usuario = self.usuario
        
        if self.usuario !=[]:
            self.carregar_sistema()
        
    def carregar_sistema(self):
        ui = pygubu.Builder()
        ui.add_from_file("window_main.ui")

        
        win =ui.get_object("principal2")
        
        self.janela_quit()
        ui.connect_callbacks(abil_azul.abil(ui,self.usuario))


    def janela_quit(self):

        self.janela.destroy()
        pass
    def janela_destroy(self):

        self.janela.quit()

        
    def buscar_infracao_lateral(self):
    	print('asdf')


ui2 = pygubu.Builder()
ui2.add_from_file("window_login.ui")

labil = App(ui2)
ui2.connect_callbacks(labil)



win =ui2.get_object("login")
win.master.title("OAM - Termo Notificação Penalidade | Alex Odisseus - SECME")
win.mainloop()