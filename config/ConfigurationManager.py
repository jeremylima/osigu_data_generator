from config.Config import Config
from config.Profiles import PROFILES

config = Config


def get_elastic_search_host():
    return PROFILES[config.CURRENT_PROFILE]['ELASTIC_SEARCH']


def get_base_url():
    return PROFILES[config.CURRENT_PROFILE]['BASE_URL']


def get_database():
    return PROFILES[config.CURRENT_PROFILE]['DATABASE']
