
class Tabuleiro:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura
        self.__tabuleiro = []
        self.montar_tabuleiro()

    def montar_tabuleiro(self):
        self.__tabuleiro = [[0 for _ in range(self.largura)] for __ in range(self.altura)]

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura
    
    @property
    def tabuleiro(self):
        return self.__tabuleiro

    def mostrar_tabuleiro(self):
        for linha in self.__tabuleiro:
            print(linha)
        print()

    def adicionar_peca(self, jogador):
        while True:
            print(f"Jogador {jogador}.")
            coluna = int(input("Selecione uma coluna para jogar: ")) - 1
            for linha in range(len(self.__tabuleiro)-1, -1, -1):
                if self.__tabuleiro[linha][coluna] == 0:
                    self.__tabuleiro[linha][coluna] = jogador
                    return
                
            print("Coluna cheia. Jogue em outro coluna!")

    def verificar_vitoria

def iniciar_jogo():
    largura = 7
    altura = 6
    tabuleiro = Tabuleiro(largura, altura)
    jogador = 0
    while True:
        tabuleiro.mostrar_tabuleiro()
        tabuleiro.adicionar_peca(jogador%2+1)
        jogador += 1
        if jogador == largura * altura - 1:
            print("Empate")
            return

if __name__ == "__main__":
    iniciar_jogo()