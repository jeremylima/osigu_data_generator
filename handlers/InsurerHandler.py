import requests
from config.Config import Config
from config import ConfigurationManager
from mapping.manufacturers_map import get_manufacturer_name
from mapping.product_types_map import get_product_type_name

config = Config
config_manager = ConfigurationManager


class InsurerHandler:
    @staticmethod
    def create_product(osigu_product):
        products_slug = {}
        for slug, token in config.INSURER_SLUGS.items():
            url = config_manager.get_base_url() + '/insurers/' + slug + '/products'
            headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

            insurer_code = '{insurer_prefix}_{osigu_product_id}_{insurer_slug}'.format(
                insurer_prefix=config.PREFIX_INSURER_CODE, osigu_product_id=osigu_product['id'],
                insurer_slug=slug[:2]).upper()

            body = {
                "id": insurer_code,
                "name": osigu_product['full_name'],
                "full_name": osigu_product['full_name'] + ' - QA TESTING',
                "manufacturer": get_manufacturer_name(osigu_product['manufacturer_id']),
                "type": get_product_type_name(osigu_product['type_id'])
            }

            resp = requests.post(url, json=body, headers=headers)
            assert resp.status_code == 204, "An error occurs when creating an insurer product"
            products_slug[insurer_code] = slug

        return products_slug
