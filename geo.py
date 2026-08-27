import requests


def get_toll_geo(s, d):
    url = "https://rajmargyatra.nhai.gov.in/nhai/api/v2.0/getMMIMultipleRoutePlannerDev"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://rajmargyatra.nhai.gov.in",
        "Referer": "https://rajmargyatra.nhai.gov.in/",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/139.0.0.0 Safari/537.36"
        )
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
    print("STATUS:", response.status_code, flush=True)
    print("CONTENT TYPE:", response.headers.get("content-type"), flush=True)
    print("RESPONSE:", response.text[:5000], flush=True)
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
