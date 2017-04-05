import logging
from handlers.ProductsHandler import ProductsHandler
from handlers.TokensHandler import TokensHandler
from config.Config import Config
from config.GlobalVariables import GlobalVariables


logging.basicConfig(filename='data_generator.log', filemode='w', level=logging.DEBUG)
config = Config
global_v = GlobalVariables

tokensHandler = TokensHandler
productHandler = ProductsHandler


tokensHandler.generate()
productHandler.populate()

print('Finished')


