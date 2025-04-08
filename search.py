import requests
import json

def busca(search = '', auth = ''):
    url = f"https://api.themoviedb.org/3/search/movie?query={search}&language=pt-br&page=1"
    url2 = f"https://api.themoviedb.org/3/movie/{search}/release_dates"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {auth}"
    }

    response = json.loads(requests.get(url, headers=headers).text)
    response2 = json.loads(requests.get(url2, headers=headers).text)

    results = []
    for item in response["results"]:
        result = {
            "Filme": {
                "id": item["id"],
                "titulo": item["title"],
                "poster": item["poster_path"],
                "capa_fundo": item["backdrop_path"],
                "generos": item["genre_ids"],
                "lançamento": item["release_date"],
                "avaliacao": f"{item["vote_average"]*10:.2f}%",
                "sinopse": item["overview"]
            }
        }
        results.append(result)

    return results