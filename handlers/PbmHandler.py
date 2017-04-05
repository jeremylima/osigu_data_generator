from config.Sequences import Sequences
from config.GlobalVariables import GlobalVariables
from mapping.pbm_category_map import get_category_id
from handlers.DatabaseHandler import DatabaseHandler

databaseHandler = DatabaseHandler
sequences = Sequences
global_v = GlobalVariables


class PbmHandler:
    def __init__(self):
        self.product_categories_id = sequences.PBM_PRODUCT_CATEGORIES
        self.substitute_products_id = sequences.PBM_SUBSTITUTE_PRODUCTS
        self.product_categories_statement = ""
        self.substitute_products_statement = ""
        self.priority = {}

    def get_priority(self, substitute_osigu_product_id):
        if substitute_osigu_product_id in self.priority:
            self.priority[substitute_osigu_product_id] += 1
        else:
            self.priority[substitute_osigu_product_id] = 1

        return self.priority[substitute_osigu_product_id]

    def build_product_categories_statement(self, product):
        osigu_product = product['osigu']
        pbm = product['pbm']
        category_id = get_category_id(pbm['category'])
        product_id = osigu_product['id']

        statement = "insert into pbm.product_categories (id, category_id, product_id, enabled, created_by, " \
                    "updated_by) " \
                    "values ({id}, {category_id}, {product_id}, true, 'test', 'test');" \
            .format(id=self.product_categories_id, category_id=category_id, product_id=product_id)

        self.product_categories_statement += statement

        self.product_categories_id += 1

    def build_substitute_products_statement(self, product):
        osigu_product = product['osigu']
        pbm = product['pbm']

        insurer_id = 1 if 'insurer_id' not in product else product['insurer_id']

        statement = "insert into pbm.substitute_products (id, insurer_id, osigu_product_id, substitute_osigu_product_id," \
                    " substitute_equivalent_units, priority, enabled, created_by, updated_by) values ({id}, " \
                    "{insurer_id}, {osigu_product_id}, {substitute_osigu_product_id}, {substitute_equivalent_units}, " \
                    "{priority}, true, 'test', 'test');" \
            .format(id=self.substitute_products_id, insurer_id=insurer_id,
                    osigu_product_id=pbm['substitute_osigu_product_id'],
                    substitute_osigu_product_id=osigu_product['id'],
                    substitute_equivalent_units=pbm['substitute_equivalent_units'],
                    priority=self.get_priority(pbm['substitute_osigu_product_id']))

        self.substitute_products_statement += statement

        self.substitute_products_id += 1

    def populate(self):
        databaseHandler.execute_non_query(self.product_categories_statement)
        databaseHandler.execute_non_query(self.substitute_products_statement)
