import requests
import json
from config.Config import Config
from config import ConfigurationManager
from mapping.entity_map import get_entity_id
from handlers.DatabaseHandler import DatabaseHandler


config = Config
config_manager = ConfigurationManager
databaseHandler = DatabaseHandler


def get_custom_token():
    query = "select * from oauth_access_tokens where entity_id =1 and entity_type = 'USER' " \
            "order by created_at desc limit 1;"

    return databaseHandler.execute(query)[0][0]


def set_provider_tokens(custom_token):
    for key in config.PROVIDER_SLUGS:
        url = config_manager.get_base_url() + '/oauth/custom/token'
        headers = {'Authorization': 'Bearer' + custom_token, 'Content-Type': 'application/json'}

        body = {
            "entity_id": get_entity_id(key),
            "entity_type": "PROVIDER_BRANCH",
            "slug": key
        }

        resp = requests.post(url, json=body, headers=headers)
        assert resp.status_code == 201, "Must be restarted the config_server for generate a new token"
        config.PROVIDER_SLUGS[key] = json.loads(resp.text)['access_token']


def set_insurer_tokens(custom_token):
    for key in config.INSURER_SLUGS:
        url = config_manager.get_base_url() + '/oauth/custom/token'
        headers = {'Authorization': 'Bearer' + custom_token, 'Content-Type': 'application/json'}

        body = {
            "entity_id": get_entity_id(key),
            "entity_type": "INSURER",
            "slug": key
        }

        resp = requests.post(url, json=body, headers=headers)
        assert resp.status_code == 201, "Must be restarted the config_server for generate a new token"
        config.INSURER_SLUGS[key] = json.loads(resp.text)['access_token']


def set_dashboard_token():
    url = config_manager.get_base_url() + '/oauth/token?grant_type=password&username={user_name}&password={password}'.format(
        user_name=config.TOKEN_DASHBOARD_USER, password=config.TOKEN_DASHBOARD_PASSWORD)
    headers = {'Authorization': 'Basic ' + config.TOKEN_BASIC, 'Content-Type': 'application/json'}

    resp = requests.post(url, headers=headers)
    assert resp.status_code == 200, "Dashboard token can not be generated. Check it out"
    config.DASHBOARD_TOKEN = json.loads(resp.text)['access_token']


class TokensHandler:
    @staticmethod
    def generate():
        custom_token = get_custom_token()
        set_provider_tokens(custom_token)
        set_insurer_tokens(custom_token)
        set_dashboard_token()
        print('Tokens generated successfully')
