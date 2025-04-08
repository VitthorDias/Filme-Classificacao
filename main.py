import configparser
import search
import testes_tela

def pesquisa_tmdb(text = ""):
    response = search.busca(text, autorizacao)

    return response


url = "https://api.themoviedb.org/3/authentication"

# Pega os dados necessários no arquivo 'config.ini'
config = configparser.ConfigParser()
config.read("config.ini")

chave = config.get('api', 'chave')
autorizacao = config.get('api', 'autorizacao')
