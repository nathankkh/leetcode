from collections import defaultdict
from typing import List

class Solution:
    # DFS
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
        recipes: string array
        ingredients: 2d string array
        ith recipe => lookup ingredients[i] 

        supplies: string array of all ingredients. Note that recipes will not be included in supplies

        return a list of all reciptes that can be created

        Create a graph where a node = a recipe.
        Find out which recipe depends on other recipes 
        '''
        d = {recipes[n]:set(ingredients[n]) for n in range(len(recipes))}
        can_be_made = {i: True for i in supplies}
        visited = set()
        def check_recipe(recipe: str):
            
            if recipe in can_be_made and can_be_made[recipe] == True:
                return True
            
            # DNE or cycle
            if recipe not in d or recipe in visited:
                return False
            
            visited.add(recipe)

            ingredients = d[recipe]
            temp = True
            for i in ingredients:
                out = check_recipe(i)
                if out == False:
                    temp = False
                    break
                else:
                    can_be_made[i] = True
            can_be_made[recipe] = temp
            return temp
        return [r for r in recipes if check_recipe(r)]
    
