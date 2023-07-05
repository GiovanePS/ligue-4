class Tabuleiro:
    def __init__(self):
        self.__tabuleiro = []
        self.montar_tabuleiro()

    def montar_tabuleiro(self):
        self.__tabuleiro = [[0 for _ in range(7)] for __ in range(6)]

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

    def verificar_vitoria():
        ...

class Ligue4:
    def __init__(self):
        self.tabuleiro = Tabuleiro()

    def iniciar_jogo(self):
        jogador = 0
        while True:
            self.tabuleiro.mostrar_tabuleiro()
            self.tabuleiro.adicionar_peca(jogador%2+1)
            jogador += 1
            if jogador == 6 * 7 - 1:
                print("Empate")
                return
            
    def verificar_empate(self):
        ...

    def verificar_vitoria(self):
        ...

if __name__ == "__main__":
    Ligue4.iniciar_jogo()