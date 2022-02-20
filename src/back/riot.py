from src.back.my_requests import safe_requests
from src.back.riot_api import RiotAPI

global ERROR_TOKEN
global ERROR_UNKNOWN_PLAYER
global ERROR_UNRANKED_PLAYER

ERROR_TOKEN = -1
ERROR_UNKNOWN_PLAYER = -2
ERROR_UNRANKED_PLAYER = -3

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


def get_rank_by_player(player, token, queue_type="RANKED_TFT"):

    if not RiotAPI().token_work(token):
        return "Error Token, please reload the token with !token [token]", ERROR_TOKEN

    status, res = RiotAPI().get_tft_player_infos_by_summ_id(player.id, token)

    if status == 403:
        print("wrong id")
        player.update(RiotAPI().get_tft_player_by_pseudo(player.pseudo, token))
        status, res = RiotAPI().get_tft_player_infos_by_summ_id(player.id, token)

        if status != 200:
            return f"{player.pseudo}: Unrecognize player", ERROR_UNKNOWN_PLAYER

    for l in res:
        if l["queueType"] == queue_type:
            return get_print(l), get_lp(l)

    return f"{player.pseudo}: Unranked player", ERROR_UNRANKED_PLAYER


def get_ranking(players, token, queue_type="RANKED_TFT"):
    """[get the list of the players and return the ranking]

    Args:
        players ([Players]): [Class players]
        token ([str]): [riot api token]
        queue_type (str, optional): [queue type]. Defaults to "RANKED_TFT".

    Returns:
        [list]: [list of the players sorted by rank]
    """
    tp = []
    st = []
    for p in players:
        tp.append(get_rank_by_player(p, token, queue_type))
    st = sorted(tp, key = lambda x: x[1], reverse=True)
    return st