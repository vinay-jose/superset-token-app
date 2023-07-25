import logging
from flask import request, make_response
# from resources import read_config
import requests
# from addons.authentication import authentication

logger = logging.getLogger()


class GuestToken:

    @classmethod
    def guest_token(cls):

        # # verify keycloak token
        # if "Authorization" in request.headers and "Bearer" in request.headers["Authorization"]:
        #     token = request.headers['Authorization'].replace("Bearer", "").strip(" ")
        #     verified = authentication.verify_keycloak_token(token)
        #     logger.info(verified)

        #     if verified is True:
        #         pass
        #     elif verified is False:
        #         return make_response("Token Expired", 401, {'WWW-Authentication': 'Token Expired'})
        #     else:
        #         return make_response("Internal Server Error", 500, {'WWW-Authentication': 'Internal Server Error'})
        # else:
        #     return make_response("Authorization Missing", 400, {'WWW-Authentication': 'Need Authorization'})

        id = str(request.args['id'])
        # message = str(request.args['message'])
        access_token, refresh_token = cls.get_access_token()
        token = cls.fetch_guest_token(id, access_token)
        return token
    
    @classmethod
    def get_access_token(cls):
        url = 'http://172.174.122.184:8088/api/v1/security/login'
        body = {
            "password": "admin",
            "provider": "db",
            "refresh": True,
            "username": "admin"
        }
        response = requests.post(url=url, json=body)
        tokens = response.json()
        return tokens["access_token"], tokens["refresh_token"]
    
    @classmethod
    def fetch_guest_token(cls, id, access_token):
        url = 'http://172.174.122.184:8088/api/v1/security/guest_token/'
        headers = {"Authorization": f'Bearer {access_token}'}
        body = {
            "resources": [
                {
                    "id": id,
                    "type": "dashboard"
                }
            ],
            "rls": [
            ],
            "user": {
                "first_name": "Superset",
                "last_name": "Admin",
                "username": "admin"
            }
        }
        response = requests.post(url=url, json=body, headers=headers)
        token = response.json()
        # print(token)
        return token
    

guestToken = GuestToken()

