from src.back.my_requests import safe_requests
from src.back.riot_api.api_LOL_STATUS import Wrp_LOL_STATUS


class Wrp_TFT_SUMMONER():
    """
    Wrapper for riot games api: TFT-SUMMONER-V1
    roots wrapped:

    /tft/summoner/v1/summoners/by-name/{pseudo}
    /tft/summoner/v1/summoners/{summ_id}
    /tft/summoner/v1/summoners/by-puuid/{puuid}
    /tft/summoner/v1/summoners/by-account/{acc_id}

    """

    def get_tft_player_by_pseudo(self, pseudo, key):
        """[get player info from pseudo]

        Args:
            pseudo ([str]): [pseudo of the player to search]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS.token_work(key):
            return 401, {"message": "Error Token"}

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{pseudo}', params=param)

    def get_tft_player_by_summ_id(self, summ_id, key):
        """[get player info from SummonerId]

        Args:
            summ_id ([str]): [SummonerId]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS.token_work(key):
            return 401, {"message": "Error Token"}

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/{summ_id}', params=param)

    def get_tft_player_by_puuid(self, puuid, key):
        """[get player info from puuid]

        Args:
            puuid ([str]): [puuid]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS.token_work(key):
            return 401, {"message": "Error Token"}

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{puuid}', params=param)

    def get_tft_player_by_acc_id(self, acc_id, key):
        """[get player info from account id]

        Args:
            acc_id ([str]): [account id]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS.token_work(key):
            return 401, {"message": "Error Token"}

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-account/{acc_id}', params=param)