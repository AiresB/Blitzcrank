from src.back.riot_api_wrp.api_LOL_STATUS import Wrp_LOL_STATUS
from src.back.riot_api_wrp.api_TFT_LEAGUE import Wrp_TFT_LEAGUE
from src.back.riot_api_wrp.api_TFT_MATCH import Wrp_TFT_MATCH
from src.back.riot_api_wrp.api_TFT_SUMMONER import Wrp_TFT_SUMMONER

class Riot_API(Wrp_LOL_STATUS, Wrp_TFT_LEAGUE, Wrp_TFT_MATCH, Wrp_TFT_SUMMONER):
    def __init__(self):
        pass