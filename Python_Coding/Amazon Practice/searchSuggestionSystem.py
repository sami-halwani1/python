import string
from typing import List

""" 
You are given an array of strings "products" and a string "searchWord"

Design a system that suggest at most three product names from "products" after each character of "searchWord" us typed.
Suggested products should have a common prefix with "searchWord". If there are more than three products with a commohn prefix return
three lexicographically minimum products.

Return a list of lists of the suggested products after each character of "searchWord" is typed.

"""



class Solution:
    def suggestedProducts(self, products: List[str], searchword: str) -> List[List[str]]:
        products.sort() #Sort Product List
        # l,r = 0, len(products)-1
        result = []
        prefix = ''

        for char in searchWord: # Iterates through the length of the searchWord
            prefix += char #appends char to prefix for search

            suggestion = []
            for product in products: #searches through products
                if product.startswith(prefix): # looks for matching products based on prefix
                    suggestion.append(product)
            result.append(suggestion[:3]) #return upto only the first 3 results


        # for i in range(len(searchword)):
        #     search = searchWord[i]

        #     while l<=r and (len(products[l]) <= i) or products[l][i] != search:
        #         l += 1

        #     while l<=r and (len(products[l]) <= i) or products[r][i] != search:
        #         r -= 1

        #     word_left = r-l +1
        #     if word_left >=3:
        #         result.append([products[l], products[l+1], products[l+2]])
        #     elif word_left == 2:
        #        result.append([products[l], products[l+1]])
        #     elif word_left == 1:
        #        result.append([products[l]])
        #     else:
        #         result.append([])
            
        return result
    

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mousepad"

solution = Solution()
result = solution.suggestedProducts(products, searchWord)
print(result)
