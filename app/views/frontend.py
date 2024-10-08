import customtkinter
from app.models.backend import *

# Classe construtora da interface
class Calculadora(customtkinter.CTk):
    # Inicializador da classe
    def __init__(self):
        super().__init__()

        # Define um título da janela
        self.title("Calculadora")

        # Configuração do display da calculadora
        self.display = customtkinter.CTkEntry(self, justify='right', font=("Arial", 20), width=300, height=50)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=(5, 10))

        # Lista dos botões com seus respectivos textos e posições
        botoes = [
            ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
            ('1/x', 2, 0), ('x²', 2, 1), ('√x', 2, 2), ('÷', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('×', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('±', 6, 0), ('0', 6, 1), (',', 6, 2), ('=', 6, 3)
        ]

        # Loop para adicionar todos os botões à interface
        for texto, linha, coluna in botoes:
            botao = customtkinter.CTkButton(self,text=texto,command=lambda t=texto: self.acao_botao(t),width=70,height=60,fg_color="#4b4b4b",hover_color="#5e5e5e",text_color="white",font=("Arial", 18))
            botao.grid(row=linha, column=coluna, padx=3, pady=3)

        # Ajustar a janela para caber exatamente no tamanho dos widgets
        self.update_idletasks()  # Atualiza o layout para obter o tamanho correto
        largura_janela = self.display.winfo_width() + 12  # Margem adicional
        altura_janela = self.display.winfo_height() + (5.67 * 70) + 20  # Ajusta a altura para incluir os botões
        self.geometry(f"{largura_janela}x{altura_janela}")  # Ajusta a janela ao tamanho dos widgets
        self.resizable(False, False)  # Desabilita redimensionamento

    # Método responsável por capturar a ação dos botões
    def acao_botao(self,valor):
        # Limpa o display se o botão "C" for pressionado
        if valor == 'C':
            self.display.delete(0, 'end')
        # Deleta o último caractere se o botão "⌫" for pressionado
        elif valor == '⌫':
            self.display.delete(len(self.display.get()) - 1, 'end')
        # Calcula o resultado se o botão "=" for pressionado
        elif valor == '=':
            try:
                expressao = self.display.get().replace('×', '*').replace('÷', '/')
                resultado = str(eval(expressao))  # Avalia a expressão usando eval
                self.display.delete(0, 'end')
                self.display.insert('end', resultado)
            except Exception as e:
                self.display.delete(0, 'end')
                self.display.insert('end', 'Erro')
        # Caso contrário, insere o valor pressionado no display
        else:
            self.display.insert('end', valor)