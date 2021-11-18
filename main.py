import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import abil_azul
import requests

from tkinter import PhotoImage
from model import Model
from ttkbootstrap import Style
style = Style(theme='flatly')



class App:
    def __init__(self, root):
        
        self.janela = root.get_object("login")
        

        self.botao=root.get_object("login_entrar_botao")
        self.botao.configure(style='primary.Outline.TButton')

        self.botao2=root.get_object("login_cancelar_botao")
        self.botao2.configure(style='primary.TButton')
        
        self.logo=root.get_object("logo")
        self.logo_img = PhotoImage(name='logo',file='img/logo.png')
       
        self.logo['image']=self.logo_img
        

        

    def logar(self):
        ui = pygubu.Builder()
        ui.add_from_file("window_main.ui")

        
        win =ui.get_object("principal2")
        
        self.janela_quit()
        ui.connect_callbacks(abil_azul.abil(ui))
        

    def janela_quit(self):

        self.janela.destroy()
        pass
    def janela_destroy(self):

        self.janela.quit()

        
    def buscar_infracao_lateral(self):
    	print('asdf')


ui2 = pygubu.Builder()
ui2.add_from_file("window_login.ui")
ui2.connect_callbacks(App(ui2))
win =ui2.get_object("login")
win.master.title("OAM - Termo Notificação Penalidade | Alex Odisseus - SECME")
win.mainloop()
