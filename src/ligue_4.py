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
        self.jogador_atual = 1

    def jogo(self):
        contador = 0
        
        while True:
            self.tabuleiro.mostrar_tabuleiro()
            self.tabuleiro.adicionar_peca(self.jogador_atual)
            if self.verificar_vitoria():
                print(f'jogador {self.jogador_atual} venceu!')
                return
            if self.verificar_empate(contador):
                print('Empate!')
                return 
            if self.jogador_atual == 2:
                self.jogador_atual = 1
            else:
                self.jogador_atual = 2
            contador += 1    
            
    def verificar_empate(self, quantidade_jogadas):
        if quantidade_jogadas == 41:
            return True 

    def verificar_vitoria(self):
        tabuleiro = self.tabuleiro.tabuleiro
        for linha in range(6):
            for coluna in range(4):
                if (tabuleiro[linha][coluna] == self.jogador_atual and 
                    tabuleiro[linha][coluna+1] == self.jogador_atual and 
                    tabuleiro[linha][coluna+2] == self.jogador_atual and 
                    tabuleiro[linha][coluna+3] == self.jogador_atual):
                        return True

        for linha in range(3):
            for coluna in range(7):
                if (tabuleiro[linha][coluna] == self.jogador_atual and 
                    tabuleiro[linha+1][coluna] == self.jogador_atual and 
                    tabuleiro[linha+2][coluna] == self.jogador_atual and 
                    tabuleiro[linha+3][coluna] == self.jogador_atual):
                        return True
                    
        for linha in range(3):
            for coluna in range(4):
                if (tabuleiro[linha][coluna] == self.jogador_atual and 
                    tabuleiro[linha+1][coluna+1] == self.jogador_atual and 
                    tabuleiro[linha+2][coluna+2] == self.jogador_atual and 
                    tabuleiro[linha+3][coluna+3] == self.jogador_atual):
                        return True
                    
        for linha in range(3,6):
            for coluna in range(4):
                if (tabuleiro[linha][coluna] == self.jogador_atual and 
                    tabuleiro[linha-1][coluna+1] == self.jogador_atual and 
                    tabuleiro[linha-2][coluna+2] == self.jogador_atual and 
                    tabuleiro[linha-3][coluna+3] == self.jogador_atual):
                        return True

if __name__ == "__main__":
    Ligue4().jogo()