import requests
import json

def busca(search = '', auth = ''):
    url_infos = f"https://api.themoviedb.org/3/search/movie?query={search}&language=pt-br&page=1"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {auth}"
    }

    response_infos = json.loads(requests.get(url_infos, headers=headers).text)
    
    results = []
    classificacao = 0
    for item in response_infos["results"]:
        url_cert = f"https://api.themoviedb.org/3/movie/{item.get("id", 0)}/release_dates"
        url_detalhes = f"https://api.themoviedb.org/3/movie/{item.get("id", 0)}?language=pt-BR"
        response_cert = json.loads(requests.get(url_cert, headers=headers).text)
        response_detal = json.loads(requests.get(url_detalhes, headers=headers).text)

        # Verifica os idiomas para verificação da classificação de idades
        temp_cert = []
        try:
            for item_cert in response_cert["results"]:
                temp_cert.append(item_cert["iso_3166_1"])
        except:
            temp_cert = []
                
        if "BR" in temp_cert:
            for item_cert in response_cert["results"]:
                if item_cert["iso_3166_1"] == "BR":
                    for cert_get in item_cert["release_dates"]:
                        classificacao = cert_get["certification"]
        else:
            classificacao = 0

        generos = []
        try:
            for gen in response_detal["genres"]:
                generos.append(gen["name"])
        except:
            generos = []
        
        result = {
            "Filme": {
                "id": item.get("id", int),
                "titulo": item.get("title", ""),
                "poster": item.get("poster_path", ""),
                "capa_fundo": item.get("backdrop_path", ""),
                "classificacao": classificacao,
                "generos": generos,
                "lancamento": item.get("release_date", ""),
                "avaliacao": item.get("vote_average", 0)*10,
                "sinopse": item.get("overview", ""),
                "assistido": "não"
            }
        }
        results.append(result)

    return results
