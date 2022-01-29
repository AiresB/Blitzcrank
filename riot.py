import requests

def token_work(token):
    p = {"api_key": token}
    res = requests.get("https://euw1.api.riotgames.com/lol/status/v3/shard-data", params=p)
    if res.status_code != 200:
        print("Error Token, please reload the token with !token [token]")
        return False
    else:
        return True


def get_print(dic):
    return f'{dic["summonerName"]}:\t {dic["tier"]}\t {dic["rank"]}\t {dic["leaguePoints"]} LP\t'


def get_lp(dic):
    tier = {"IRON": 0, "BRONZE": 400, "SILVER": 800, "GOLD": 1200, "PLATINUM": 1600, "DIAMOND": 2000, "MASTER": 2400, "GRANDMASTER": 2400 ,"CHALLENGER": 2400}
    rank = {"IV": 0, "III": 100, "II": 200, "I": 300}
    lp = tier[dic["tier"]] + rank[dic["rank"]] + int(dic["leaguePoints"])
    return lp


def get_player(pseudo, param):
    return requests.get(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{pseudo}', params=param).json()


def get_rank(pseudo, token, queue_type="RANKED_TFT"):
    if not token_work(token):
        return "Error Token, please reload the token with !token [token]", 0
    param = {"api_key": token}
    player = get_player(pseudo, param)
    id = player["id"]
    rank = requests.get(f'https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{id}', params=param).json()
    if type(rank) != list:
        if rank["queueType"] == queue_type:
            return get_print(rank), get_lp(rank)
        else:
            return f"{pseudo}: Unranked player", 0
    else:
        for l in rank:
            if l["queueType"] == queue_type:
                return get_print(l), get_lp(l)
    return f"{pseudo}: Unranked player", 0

def get_list(pseudos, token, queue_type="RANKED_TFT"):
    tp = []
    for p in pseudos:
        tp.append(get_rank(p, token, queue_type))
    st = sorted(tp, key = lambda x: x[1], reverse=True)
    return st