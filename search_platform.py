import requests
import json

def plataformas(filme_id = int, auth = ''):
    url = f"https://api.themoviedb.org/3/movie/{filme_id}/watch/providers"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {auth}"
    }

    response_platform = json.loads(requests.get(url, headers=headers).text)
    
    try:
        dados = response_platform["results"]["BR"]
        streams = dados["flatrate"]
    except:
        response = {
            "link": f"https://www.themoviedb.org/movie/{filme_id}/watch?locale=BR",
            "streams": [{"Indisponível": ""}]
        }
    else:
        providers = []
        for i in range(len(streams)):
            providers.append({streams[i]["provider_name"]: streams[i]["logo_path"]})

        response = {
            "link": dados["link"],
            "streams": providers
        }
    
    return response
