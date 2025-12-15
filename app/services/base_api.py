import requests
from app.config.settings import settings

class BaseAPI:
    @staticmethod
    def _get(endpoint: str, params: dict = None):
        if params is None:
            params = {}
        
        url = f"{settings.BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = settings.get_headers()
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Request Failed at {endpoint}: {e}")
            return None
