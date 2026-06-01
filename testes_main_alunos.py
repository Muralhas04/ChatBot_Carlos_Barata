import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from app import obter_resposta, chat


class TestChatBot(unittest.TestCase):


    def test_obter_resposta_saudacoes(self):
        """Testa se o bot responde corretamente a saudações individuais e tuplos."""
        self.assertEqual(obter_resposta("Olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("BOM DIA"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")
        

    def test_obter_resposta_perguntas_exatas(self):
        """Testa correspondências de texto exatas ou parciais de chaves simples."""
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("Como te chamas"), "O meu nome é: Bot :)")

    def test_obter_resposta_substring(self):
        """Testa se o bot reconhece palavras-chave dentro de uma frase."""
        self.assertEqual(obter_resposta("podes dar-me uma ajuda?"), "Podes perguntar-me pelas horas, tempo, o meu nome ou dizer adeus.")
        self.assertEqual(obter_resposta("Como está o tempo hoje?"), "Está um dia de sol fantástico!")

    def test_obter_resposta_horas(self):
        """Testa a resposta das horas dinâmica."""
        resposta_esperada = f"São: {datetime.now():%H:%M} horas"  
        self.assertEqual(obter_resposta("que horas são?"), resposta_esperada)
    def test_obter_resposta_desconhecida(self):
        """Testa a resposta padrão quando o bot não entende."""
        entrada = "Qual é o sentido da vida?"
        resposta_esperada = f"Desculpa, não entendi a questão! {entrada}"
        self.assertEqual(obter_resposta(entrada), resposta_esperada)


    @patch('builtins.print')
    @patch('builtins.input')
    def test_fluxo_chat_completo(self, mock_input, mock_print):
        """Simula uma conversa inteira no terminal para garantir que o loop funciona e termina."""
        
        mock_input.side_effect = ['Carlos', 'tempo', 'adeus']

        chat()

        self.assertEqual(mock_input.call_count, 3)

        mock_print.assert_any_call('Chat acabou')


if __name__ == '__main__':
    unittest.main()
    