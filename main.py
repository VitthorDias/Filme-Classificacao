import configparser
import search
import testes_tela


url = "https://api.themoviedb.org/3/authentication"

# Pega os dados necessários no arquivo 'config.ini'
config = configparser.ConfigParser()
config.read("config.ini")

chave = config.get('api', 'chave')
autorizacao = config.get('api', 'autorizacao')

response = search.busca("Annabele", autorizacao)

testes_tela.tela(response)
