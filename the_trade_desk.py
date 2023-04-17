# -*- coding: utf-8 -*-
"""
This is the coding problem requested during the internship application process of The Trade Desk - Shanghai.
30 minutes are allowed.

"products"  is a list of all products on sale.
"productPrices" is the list of the correct prices of the produts, where at index i there is the price of the ith product on sale.
"productSold" is a list of product sold right now
"soldPrice" is the list of prices at which the products are sold right now

There can be errors in the price of products sold right now, so the task is to count how many products are being sold at a wrong price.
"""

def solution(products, productPrices, productSold, soldPrice):
    price_hashtable = {products[i]: productPrices[i] for i in range(len(productPrices))}
    err_count = 0
    for i in range(0, len(productSold)):
        if soldPrice[i] != price_hashtable[productSold[i]]:
            err_count += 1
    return err_count

