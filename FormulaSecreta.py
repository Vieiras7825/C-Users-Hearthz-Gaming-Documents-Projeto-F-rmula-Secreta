from datetime import datetime, timedelta

# Definindo as classes principais
class Participante:
    def __init__(self, nome, idade, equipe):
        self.nome = nome
        self.idade = idade
        self.equipe = equipe

class Equipe:
    def __init__(self, cor):
        self.cor = cor
        self.participantes = []
        self.pontuacao = 0

    def atualizar_pontuacao(self, pontos):
        self.pontuacao += pontos

class ProjetoFormulaSecreta:
    def __init__(self):
        self.equipes = {
            "verde": Equipe("verde"),
            "laranja": Equipe("laranja"),
            "amarela": Equipe("amarela"),
            "vermelha": Equipe("vermelha")
        }
        self.atividades = []
        self.data_inicio = datetime(2024, 7, 22)
        self.data_fim = datetime(2024, 7, 27)  # Corrigido: adicionei o fechamento do parêntese

# Exemplo de uso
projeto = ProjetoFormulaSecreta()
projeto.equipes["verde"].atualizar_pontuacao(10)

print(projeto.equipes["verde"].pontuacao)  # Saída: 10
