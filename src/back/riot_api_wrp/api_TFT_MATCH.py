from src.back.my_requests import safe_requests
from src.back.riot_api_wrp.api_LOL_STATUS import Wrp_LOL_STATUS

ERROR_TOKEN = 401, {'status': {'message': 'Error Token', 'status_code': 401}}

class Wrp_TFT_MATCH:
    """
    Wrapper for riot games api: TFT-MATCH-V1
    roots wrapped:

    /tft/match/v1/matches/by-puuid/{puuid}/ids
    /tft/match/v1/matches/{matchId}
    """
    def get_tft_match_history(self, puuid, token, nb="20"):
        """[Get a list of match ids by PUUID]

        Args:
            puuid (str): [puuid of the player]
            token (str): [riot api]
            nb (str): [number of games in the history, default="20"]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(token):
            return ERROR_TOKEN

        p = {"api_key": token}
        return safe_requests(f"https://euw1.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={nb}", params=p)

    def get_tft_match(self, id, token):
        """[Get a match by match id]

        Args:
            id (str): [id of the game]
            token (str): [riot api]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(token):
            return ERROR_TOKEN

        p = {"api_key": token}
        return safe_requests(f"https://euw1.api.riotgames.com/tft/match/v1/matches/{id}", params=p)