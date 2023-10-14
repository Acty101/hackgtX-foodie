import json
from collections import defaultdict


class RecipeFinder:
    def __init__(
        self,
        class_names,
        
        json_ingredients_filepath="./ingredient_to_recipes.json",
        json_recipe_filepath="./recipe_to_ingredients.json",
    ) -> None:
        self.class_names = [name.lower() for name in class_names]
        with open(json_ingredients_filepath, "r") as json_file:
            self.in_to_rec_data = json.load(json_file)

        with open(json_recipe_filepath, "r") as json_file:
            self.rec_to_in_data = json.load(json_file)
        # remove ingredients not found
        self.in_to_rec_data = {
            key: self.in_to_rec_data[key]
            for key in self.in_to_rec_data
            if key in self.class_names
        }
        # get a defaultDict of recipes and how many ingredients encountered
        self.mapping = defaultdict()
        for key, values in self.in_to_rec_data.items():
            for value in values:
                self.mapping[value] = 0
        self.recipes = []

    def get_recipes(self):
        self._find_recipes()
        return self.recipes

    def _find_recipes(self, threshold=0.15):
        for ingredients, recipes in self.in_to_rec_data.items():
            for recipe in recipes:
                self.mapping[recipe] += 1
        for key, value in self.mapping.items():
            try:
                if value >= threshold * len(
                    self.rec_to_in_data[key]["ingredients"]
                ):
                    self.recipes.append(key)
            except KeyError:
                continue
