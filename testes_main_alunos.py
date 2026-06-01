import unittest
from datetime import datetime
from app import obter_resposta


class TestObterResposta(unittest.TestCase):
    def teste_saudacoes(self):
        """Teste de respostas a saudações - 3 testes"""
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")

    def teste_perguntas_simples(self):
        """Teste de respostas a perguntas simples - 4 testes"""
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("como te chamas"), "O meu nome é: Bot :)")
        self.assertEqual(obter_resposta("tempo"), "Está um dia de sol fantástico!")
        self.assertEqual(obter_resposta("ajuda"), "Podes perguntar-me pelas horas, tempo, o meu nome ou dizer adeus.")

    def teste_despedidas(self):
        """Teste de respostas a despedidas - 3 testes"""
        self.assertEqual(obter_resposta("bye"), "Gostei de falar contigo! Até breve...")

    def teste_historia_portugal(self):
        """Teste de respostas sobre história de Portugal - 1 teste"""

    def teste_cozinhar(self):
        """Teste de respostas sobre cozinhar - 1 teste"""

    def teste_programar(self):
        """Teste de respostas sobre programar - 2 testes"""

    def teste_desenvolvimento(self):
        """Teste de respostas sobre desenvolvimento - 4 testes"""
        self.assertEqual(obter_resposta("desenvolvimento web"), "O desenvolvimento web envolve a criação de sites e aplicações web...")

    def teste_ia(self):
        """Teste de respostas sobre inteligência artificial - 3 testes"""
        self.assertEqual(obter_resposta("ia"), "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana.")

    def teste_saude(self):
        """Teste de respostas sobre saúde - 3 testes"""
        self.assertEqual(obter_resposta("saúde"), "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades.")

    def teste_indisposicao(self):
        """Teste de respostas sobre indisposição - 3 testes"""
        self.assertEqual(obter_resposta("indisposição"), "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem.")

    def teste_horas_e_data(self):
        """Teste de respostas a perguntas sobre horas e data"""
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%d-%m-%Y")

        self.assertEqual(obter_resposta("que horas são"), f"São: {hora_atual} horas")
        self.assertEqual(obter_resposta("qual é a data"), f"Hoje é dia: {data_atual}")

    def teste_resposta_padrao(self):
        """Teste de resposta padrão"""
        texto_aleatorio = "xyz123"
        self.assertEqual(obter_resposta(texto_aleatorio), f"Desculpa, não entendi a questão! {texto_aleatorio}")
        texto_aleatorio2 = "teste123" # fazer outro teste de texto aleatório
        texto_aleatorio3 = "indisposição" # fazer outro teste de texto aleatório
        texto_aleatorio4 = "sintomas de indisposição" # fazer outro teste de texto aleatório


if __name__ == '__main__':
    unittest.main()


# para correr os testes: python -m unittest -v testes_main_alunos.py