import customtkinter
from app.models.backend import *

# Classe construtora da interface
class Calculadora(customtkinter.CTk):
    # Inicializador da classe
    def __init__(self):
        super().__init__()

        # Define um titulo da janela
        self.title("Calculadora")
        # Define a altura e a largura da janela
        self.geometry("320x450")

        # Define um botão na tela, e com o parametro "command" seleciona um metodo para executar uma ação ao pressionar o botão
        self.button = customtkinter.CTkButton(self, text="Pressione", command=self.pressione)
        # Faz a estilização do botão
        self.button.grid(row=0, column=0, padx=20, pady=20)

    # Metodo responsavel por exibir no terminal "Pressionado" ao clicar no botão
    def pressione(self):
        print("Pressionado")