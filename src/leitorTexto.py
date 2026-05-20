class LeitorTexto:
    linhas = []

    def __init__(self):
        self.linhas = []
        print("Insira o texto: ")

    def get_texto(self):
        lendo_paragrafo = True
        while lendo_paragrafo:
            linha = input()
            if linha == "":
                lendo_paragrafo = False
            else:
                self.linhas.append(linha)
