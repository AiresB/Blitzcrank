from src.back.my_requests import safe_requests

class Wrp_LOL_STATUS():
    """
    Wrapper for riot games api: LOL-STATUS-V4
    roots wrapped:

    /lol/status/v4/platform-data

    """
    def get_lol_status(self, token):
        """[Check the validity of the token]

        Args:
            token (str): [riot api]

        Returns:
            [Bool]: [True: token works, False: token doesn't work]
        """
        p = {"api_key": token}
        return safe_requests("https://euw1.api.riotgames.com/lol/status/v4/platform-data", params=p)

    def token_work(self, token):
        """[Check the validity of the token]

        Args:
            token (str): [riot api]

        Returns:
            [Bool]: [True: token works, False: token doesn't work]
        """
        p = {"api_key": token}
        status, _ = safe_requests("https://euw1.api.riotgames.com/lol/status/v4/platform-data", params=p)
        if status != 200:
            print("Error Token, please reload the token with !token [token]")
            return False
        else:
            return True