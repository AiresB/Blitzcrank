from src.back.my_requests import safe_requests

def token_work(token):
    """[Check the validity of the token]

    Args:
        token (str): [riot api]

    Returns:
        [Bool]: [True: token works, False: token doesn't work]
    """
    p = {"api_key": token}
    status, _ = safe_requests("https://euw1.api.riotgames.com/lol/status/v3/shard-data", params=p)
    if status != 200:
        print("Error Token, please reload the token with !token [token]")
        return False
    else:
        return True


def get_print(dic):
    """[get the ranked string from the dic]

    Args:
        dic (dictionary): [player dictionnary]

    Returns:
        [str]: [the rank as string]
    """
    return f'{dic["summonerName"]}:\t {dic["tier"]}\t {dic["rank"]}\t {dic["leaguePoints"]} LP\t'


def get_lp(dic):
    """[get the rank as lp from 0 to ~3000]

    Args:
        dic (dictionary): [player dictionnary]

    Returns:
        [int]: [the rank as lp]
    """
    tier = {"IRON": 0, "BRONZE": 400, "SILVER": 800, "GOLD": 1200, "PLATINUM": 1600, "DIAMOND": 2000, "MASTER": 2400, "GRANDMASTER": 2400 ,"CHALLENGER": 2400}
    rank = {"IV": 0, "III": 100, "II": 200, "I": 300}
    lp = tier[dic["tier"]] + rank[dic["rank"]] + int(dic["leaguePoints"])
    return lp


def get_player_id(pseudo, param):
    """[get informations on the player by his pseudo]

    Args:
        pseudo ([str]): [pseudo of the player searched]
        param ([dict]): [param from the requests, containing token]

    Returns:
        [dict]: [dict of the player informations]
    """
    status, res = safe_requests(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{pseudo}', params=param)
    if status == 200:
        return res["id"]
    else:
        return 0


def get_rank(pseudo, token, queue_type="RANKED_TFT"):
    """[get the rank of a player given his pseudo and the queue type]

    Args:
        pseudo ([str]): [pseudo of the player]
        token ([str]): [riot api token]
        queue_type (str): [queue type]. Defaults to "RANKED_TFT".

    Returns:
        [str]: [rank as str]
        [int]: [rank as int]
    """
    if not token_work(token):
        return "Error Token, please reload the token with !token [token]", 0
    param = {"api_key": token}
    id = get_player_id(pseudo, param)
    if id == 0:
        return f"{pseudo}: Unrecognize player", 0
    status, res = safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{id}', params=param)
    if status != 200:
        return f"{pseudo}: Unranked player", 0

    if type(res) != list:
        if res["queueType"] == queue_type:
            return get_print(res), get_lp(res)
        else:
            return f"{pseudo}: Unranked player", 0
    else:
        for l in res:
            if l["queueType"] == queue_type:
                return get_print(l), get_lp(l)
    return f"{pseudo}: Unranked player", 0

def get_list(pseudos, token, queue_type="RANKED_TFT"):
    """[get the list of the players and return the ranking]

    Args:
        pseudos ([str]): [pseudos]
        token ([str]): [riot api token]
        queue_type (str, optional): [queue type]. Defaults to "RANKED_TFT".

    Returns:
        [list]: [list of the players sorted by rank]
    """
    tp = []
    st = []
    for p in pseudos:
        tp.append(get_rank(p, token, queue_type))
    st = sorted(tp, key = lambda x: x[1], reverse=True)
    return st