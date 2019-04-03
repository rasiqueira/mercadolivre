# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:47:57 2019

@author: Rodrigo
"""

import time
import requests
import schedule
pool =[]
def scrap():  
    
    response = requests.get("https://api.mercadolibre.com/sites/MLB/search?q=master system")

    for product in response.json().get('results'):
        if len(pool) == 50:
            break
        elif product['id'] in pool:
            pass
        else:
            string = 'id :' + product['id'] + ' produto: ' + product['title'] + ' preço: R$' + str(product['price']) + ' link: ' + product['permalink']
            print('id :' + product['id'])
            print('produto: ' + product['title'])
            print('preço: R$' + str(product['price']))
            print('link: ' + product['permalink'])
            print(string)
            pool.append(product['id'])
            requests.get(
                    "https://api.telegram.org/bot735882624:AAFXauZDdFgHPCdoYnoum-hKif8nd6FbO_U/sendMessage?chat_id=60302325&text"
                    "='novo produto no ML \n {}'"
            .format(string))
            requests.get(
                    "https://api.telegram.org/bot735882624:AAFXauZDdFgHPCdoYnoum-hKif8nd6FbO_U/sendMessage?chat_id=696291164&text"
                    "='novo produto no ML \n {}'"
                    .format(string))
        
    return pool

    
            
schedule.every(10).minutes.do(scrap)
while True:
    schedule.run_pending()
    time.sleep(1)
