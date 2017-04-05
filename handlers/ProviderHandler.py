import requests
from config.Config import Config
from config import ConfigurationManager
from mapping.manufacturers_map import get_manufacturer_name
from mapping.product_types_map import get_product_type_name

config = Config
config_manager = ConfigurationManager


class ProviderHandler:
    @staticmethod
    def create_product(osigu_product):
        products_slug = {}
        for slug, token in config.PROVIDER_SLUGS.items():
            url = config_manager.get_base_url() + '/providers/' + slug + '/products'
            headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

            provider_code = '{provider_prefix}_{osigu_product_id}_{provider_slug}'.format(
                provider_prefix=config.PREFIX_PROVIDER_CODE, osigu_product_id=osigu_product['id'],
                provider_slug=slug[:2]).upper()

            body = {
                "id": provider_code,
                "name": osigu_product['full_name'],
                "full_name": osigu_product['full_name'] + ' - QA TESTING',
                "manufacturer": get_manufacturer_name(osigu_product['manufacturer_id']),
                "type": get_product_type_name(osigu_product['type_id'])
            }

            resp = requests.post(url, json=body, headers=headers)
            assert resp.status_code == 204, "An error occurs when creating a provider product"
            products_slug[provider_code] = slug

        return products_slug

