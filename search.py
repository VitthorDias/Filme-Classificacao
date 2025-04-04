import requests
import json

def busca(search = '', auth = ''):
    url = f"https://api.themoviedb.org/3/search/movie?query={search}&language=pt-br&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {auth}"
    }

    response = json.loads(requests.get(url, headers=headers).text)

    results = []
    for item in response["results"]:
        result = {
            "Filme": {
                "id": item["id"],
                "titulo": item["title"],
                "imagem": item["poster_path"],
                "avaliacao": f"{item["vote_average"]*10:.2f}%",
                "sinopse": item["overview"]
            }
        }
        results.append(result)

    return results