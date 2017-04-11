import requests
from config.Config import Config
from config import ConfigurationManager
from mapping.manufacturers_map import get_manufacturer_name
from mapping.product_types_map import get_product_type_name
from mapping.insurers_map import get_insurer_id
from mapping.diagnoses_map import get_diagnosis_id

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

            manufacturer = None if 'manufacturer_id' not in osigu_product else \
                get_manufacturer_name(osigu_product['manufacturer_id'])

            body = {
                "id": insurer_code,
                "name": osigu_product['full_name'],
                "full_name": osigu_product['full_name'],
                "manufacturer": manufacturer,
                "type": get_product_type_name(osigu_product['type_id'])
            }

            resp = requests.post(url, json=body, headers=headers)
            assert resp.status_code == 204, "An error occurs when creating an insurer product"
            products_slug[insurer_code] = slug

        return products_slug

    @staticmethod
    def create_insurer_product_diagnoses(insurer_products, diagnoses):
        for insurer_product, slug in insurer_products.items():
            insurer_id = get_insurer_id(slug)
            for diagnosis in diagnoses:
                diagnosis_id = get_diagnosis_id(diagnosis)
                url = config_manager.get_base_url() + '/insurers/{insurer_id}/products/{insurer_product}/diagnoses/' \
                                                      '{diagnosis_id}'\
                    .format(insurer_id=insurer_id,insurer_product=insurer_product, diagnosis_id=diagnosis_id)

                headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

                resp = requests.post(url, headers=headers)

                assert resp.status_code == 201, "An error occurs when creating insurer_product_diagnoses. " + resp.text
