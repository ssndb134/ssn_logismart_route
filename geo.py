import requests


def get_toll_geo(s, d):
    url = "https://rajmargyatra.nhai.gov.in/nhai/api/v2.0/getMMIMultipleRoutePlannerDev"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://rajmargyatra.nhai.gov.in",
        "referer": "https://rajmargyatra.nhai.gov.in/"
    }

    payload = {
        "startAddress": s,
        "endAddress": d,
        "vehicletype": "31",
        "source": "web"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )
    print(response)
    dat = response.json()
    return dat["payload"]["routes"][0]["data"]["total_cost"], dat["payload"]["routes"][0]["data"]["distance"], dat["payload"]["routes"][0]["data"]["total_tolls"], dat["payload"]["routes"][0]["geometry"]



def get_toll_mappls(s, d):
    API_KEY = "xoivqadrfigbfjeainuunbubhnfcnzfxkeqo"

    url = (
        f"https://apis.mappls.com/advancedmaps/v1/"
        f"{API_KEY}/route_adv/trucking/"
        f"{s};{d}"
    )

    params = {
        "alternatives": "true",
        "overview": "full"
    }

    response = requests.get(url, params=params)

    dat = response.json()
    return dat
