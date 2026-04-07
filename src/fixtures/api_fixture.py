import pytest
import requests
from src.config.settings import BASE_URL_API
from src.utils.utils_logger import get_logger

logger = get_logger(__name__)


class APIClient:
    """
    Reusable API client for all API tests
    Handles base URL, headers, auth token
    """
    def __init__(self, base_url:str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.clear()        # clear all default headers
        self.session.cookies.clear()        # <-- IMPORTANT
        self.session.auth = None    
        self.token = None 
   

    # default heders

    def set_auth_token(self, token: str):
            """
            set JWT token in headers
            """
            if "reqres.in" in self.base_url:
                return  # skip for ReqRes
            ''' self.token = token
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })
            logger.info("Auth token set !")'''

    def get(self, endpoint: str, params= None):
            """GET Request """
            url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            logger.info(f"GET {url}")
            response = self.session.get(url, params=params)
            logger.info(f"Response: {response.status_code}")
            return response
            
    
    def post(self, endpoint: str, json= None, **kwargs):
            """POST Request """
            url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            logger.info(f" POST {url}")
            logger.info(f" Payload: {json}")
            response = self.session.post(url,json= json, **kwargs)
            logger.info(f" Response: {response.status_code}")
            return response 

    def put(self, endpoint: str, json = None, **kwargs):
            """PUT Request"""
            url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            logger.info(f"PUT {url}")
            logger.info(f"payload: {json}")
            response = self.session.put(url,json=json, **kwargs)
            logger.info(f" Response: {response.status_code}")
            return response

    def delete(self, endpoint: str):
            """DELETE Request"""
            url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
            logger.info(f"DELETE {url}")
            response = self.session.delete(url)
            logger.info(f" Response: {response.status_code}")
            return response    

    def close(self):
            """ Close Session """
            self.session.close()
            logger.info("API session closed!")

 
@pytest.fixture(scope = "session")
def api_client():
    """
    Session scoped API client
    Created once - reused for ALL API tests
    """
    logger.info(" Creating API Client...")
    client = APIClient("https://jsonplaceholder.typicode.com")
    yield client
    client.close()
    logger.info("API client closed !")

       
    




        




