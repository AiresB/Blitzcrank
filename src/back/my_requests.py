import requests

def safe_requests(url, params={}, req_type=requests.get):
    """[safe request return a tuple with the status code and the response as dict]

    Args:
        url ([str]): [url to request]
        params ([str], optional): [params]
        req_type ([request.], optional): [request type]. Defaults to requests.get.
    """
    res = req_type(url, params=params)
    return res.status_code, res.json()
