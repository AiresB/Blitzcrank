from src.back.my_requests import safe_requests
from src.back.riot_api_wrp.api_LOL_STATUS import Wrp_LOL_STATUS

ERROR_TOKEN = 401, {'status': {'message': 'Error Token', 'status_code': 401}}

class Wrp_TFT_LEAGUE:
    """
    Wrapper for riot games api: TFT-LEAGUE-V1
    roots wrapped:

    /tft/league/v1/challenger
    /tft/league/v1/grandmaster
    /tft/league/v1/master
    /tft/league/v1/entries/by-summoner/{summ_id}
    /tft/league/v1/entries/{tier}/{div}?page={page}
    /tft/league/v1/leagues/{id}
    /tft/league/v1/rated-ladders/{queue}/top
    """

    def get_tft_challengers(self, key):
        """[get all players challenger]

        Args:
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/challenger', params=param)

    def get_tft_grandmaster(self, key):
        """[get all players grandmaster]

        Args:
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/grandmaster', params=param)

    def get_tft_master(self, key):
        """[get all players master]

        Args:
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/master', params=param)

    def get_tft_player_infos_by_summ_id(self, summ_id, key):
        """[Get league entries for a given summoner ID]

        Args:
            summ_id ([str]): [summoner id]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summ_id}', params=param)

    def get_tft_league(self, tier, div, page, key):
        """[Get all the league entries]

        Args:
            tier ([str]): [tier [IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND]]
            div ([str]): [division [I, II, III, IV]]
            page ([str]): [page number as str]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/entries/{tier}/{div}?page={page}', params=param)

    def get_tft_league_from_id(self, id, key):
        """[Get league with given ID, including inactive entries]

        Args:
            id ([str]): [The UUID of the league.]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/leagues/{id}', params=param)

    def get_tft_ladder_from_queue(self, key, queue="RANKED_TFT_TURBO"):
        """[Get the top rated ladder for given queue]

        Args:
            queue ([str]): [default: "RANKED_TFT_TURBO"]
            key ([str]): [api key]

        Returns:
            [status code]: []
            [response]: [response json as dict]
        """
        if not Wrp_LOL_STATUS().token_work(key):
            return ERROR_TOKEN

        param = {"api_key": key}
        return safe_requests(f'https://euw1.api.riotgames.com/tft/league/v1/rated-ladders/{queue}/top', params=param)