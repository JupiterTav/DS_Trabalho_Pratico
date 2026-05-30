# TODO: Integrar com a UI

class CampoTexto:
    def __init__(self):
        self.linhas: list[str] = []
        print("Insira  o texto: ")

    def le_texto(self):
        lendo = True
        while lendo:
            linha = input()
            if linha == "":
                lendo = False
            else:
                self.linhas.append(linha)

    @property
    def Linhas(self):
        return self.linhas
