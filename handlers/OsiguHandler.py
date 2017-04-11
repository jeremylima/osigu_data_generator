import requests
from config.Config import Config
from config import ConfigurationManager
from mapping.diagnoses_map import get_diagnosis_id

config = Config
config_manager = ConfigurationManager


class OsiguHandler:
    @staticmethod
    def associate_provider_product(osigu_product, provider_products):
        for provider_product, slug in provider_products.items():
            url = config_manager.get_base_url() + '/products/{osigu_product_id}/references/providers/{provider_slug}/products/{' \
                                                  'provider_product}'.format(osigu_product_id=osigu_product,
                                                                             provider_slug=slug,
                                                                             provider_product=provider_product)

            headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

            resp = requests.post(url, headers=headers)

            assert resp.status_code == 204, "An error occurs when associated a provider product. Osigu id: " \
                                            + str(osigu_product) + ". " + resp.text

    @staticmethod
    def associate_insurer_product(osigu_product, insurer_products):
        for insurer_product, slug in insurer_products.items():
            url = config_manager.get_base_url() + '/products/{osigu_product_id}/references/insurers/{insurer_slug}/products/{' \
                                                  'insurer_product}'.format(osigu_product_id=osigu_product,
                                                                            insurer_slug=slug,
                                                                            insurer_product=insurer_product)

            headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

            resp = requests.post(url, headers=headers)

            assert resp.status_code == 204, "An error occurs when associated an insurer product. Osigu id: " \
                                            + str(osigu_product) + ". " + resp.text

    @staticmethod
    def create_product_diagnosis_association(osigu_product, diagnoses):

        for diagnosis in diagnoses:
            url = config_manager.get_base_url() + '/products/{osigu_product_id}/diagnoses/{diagnosis_id}' \
                .format(osigu_product_id=osigu_product, diagnosis_id=get_diagnosis_id(diagnosis))

            headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

            resp = requests.post(url, headers=headers)

            assert resp.status_code == 201, "An error occurs when create product diagnosis association. Osigu id: " \
                                            + str(osigu_product) + ". " + resp.text
