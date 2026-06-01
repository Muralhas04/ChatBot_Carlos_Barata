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
        self.assertEqual(obter_resposta("adeus"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("tchau"), "Gostei de falar contigo! Até breve...")

    def teste_historia_portugal(self):
        """Teste de respostas sobre história de Portugal - 1 teste"""
        self.assertEqual(obter_resposta("história de portugal"), "Portugal foi fundado em 1143 por D. Afonso Henriques.")

    def teste_cozinhar(self):
        """Teste de respostas sobre cozinhar - 1 teste"""
        self.assertEqual(obter_resposta("cozinhar"), "Cozinhar envolve arte, técnica e bons ingredientes!")

    def teste_programar(self):
        """Teste de respostas sobre programar - 2 testes"""
        self.assertEqual(obter_resposta("programar python"), "Python é uma excelente linguagem para programar!")
        self.assertEqual(obter_resposta("aprender a programar"), "Programar exige muita prática e lógica.")

    def teste_desenvolvimento(self):
        """Teste de respostas sobre desenvolvimento - 4 testes"""
        self.assertEqual(obter_resposta("desenvolvimento web"), "O desenvolvimento web envolve a criação de sites e aplicações web...")
        self.assertEqual(obter_resposta("desenvolvimento de software"), "O desenvolvimento de software segue um ciclo de vida planeado.")
        self.assertEqual(obter_resposta("desenvolvimento mobile"), "Criar apps para telemóveis faz parte do desenvolvimento mobile.")
        self.assertEqual(obter_resposta("equipa de desenvolvimento"), "O trabalho em equipa é essencial no desenvolvimento.")

    def teste_ia(self):
        """Teste de respostas sobre inteligência artificial - 3 testes"""
        self.assertEqual(obter_resposta("ia"), "A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana.")
        self.assertEqual(obter_resposta("inteligência artificial"), "A inteligência artificial está a mudar o mundo tecnológico.")
        self.assertEqual(obter_resposta("futuro da ia"), "O futuro da inteligência artificial trará muita automação.")

    def teste_saude(self):
        """Teste de respostas sobre saúde - 3 testes"""
        self.assertEqual(obter_resposta("saúde"), "A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades.")
        self.assertEqual(obter_resposta("cuidar da saúde"), "Cuidar da saúde implica comer bem e fazer exercício.")
        self.assertEqual(obter_resposta("saúde mental"), "A saúde mental é tão importante quanto a física.")

    def teste_indisposicao(self):
        """Teste de respostas sobre indisposição - 3 testes"""
        self.assertEqual(obter_resposta("indisposição"), "Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem.")
        self.assertEqual(obter_resposta("estou indisposto"), "Se sentes indisposição, o ideal é descansar um pouco.")
        self.assertEqual(obter_resposta("muita indisposição"), "Indisposição persistente deve ser avaliada por um médico.")

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
        
        texto_aleatorio2 = "teste123"
        self.assertEqual(obter_resposta(texto_aleatorio2), f"Desculpa, não entendi a questão! {texto_aleatorio2}")
        
        # Nota: "indisposição" não deve ser testada aqui como falha, pois o bot conhece essa palavra!
        texto_aleatorio3 = "pergunta desconhecida" 
        self.assertEqual(obter_resposta(texto_aleatorio3), f"Desculpa, não entendi a questão! {texto_aleatorio3}")


if __name__ == '__main__':
    unittest.main()
    