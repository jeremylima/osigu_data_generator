import logging
from handlers.ProductsHandler import ProductsHandler
from handlers.TokensHandler import TokensHandler
from config.Config import Config

logging.basicConfig(filename='data_generator.log', filemode='w', level=logging.DEBUG)
config = Config

tokensHandler = TokensHandler
productHandler = ProductsHandler

tokensHandler.generate()
productHandler.populate()

print('Finished')


