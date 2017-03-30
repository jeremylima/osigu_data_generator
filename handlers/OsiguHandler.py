import requests
from config.Config import Config


config = Config


class OsiguHandler:
    @staticmethod
    def associate_provider_product(osigu_product, provider_products):
        for provider_product, slug in provider_products.items():
            url = config.BASE_URL + '/products/{osigu_product_id}/references/providers/{provider_slug}/products/{' \
                                    'provider_product}'.format(osigu_product_id=osigu_product, provider_slug=slug,
                                                               provider_product=provider_product)

            headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

            resp = requests.post(url, headers=headers)

            assert resp.status_code == 204, "An error occurs when associated a provider product"

    @staticmethod
    def associate_insurer_product(osigu_product, insurer_products):
        for insurer_product, slug in insurer_products.items():
            url = config.BASE_URL + '/products/{osigu_product_id}/references/insurers/{insurer_slug}/products/{' \
                                    'insurer_product}'.format(osigu_product_id=osigu_product, insurer_slug=slug,
                                                              insurer_product=insurer_product)

            headers = {'Authorization': 'Bearer ' + config.DASHBOARD_TOKEN, 'Content-Type': 'application/json'}

            resp = requests.post(url, headers=headers)

            assert resp.status_code == 204, "An error occurs when associated an insurer product"
