import os
import json
from collections import defaultdict

INGREDIENTS = [
    "Apple",
    "Banana",
    "Cucumber",
    "Orange",
    "Tomato",
    "apple",
    "asparagus",
    "avocado",
    "banana",
    "beef",
    "bell_pepper",
    "bento",
    "blueberries",
    "bread",
    "broccoli",
    "butter",
    "carrot",
    "cauliflower",
    "cheese",
    "chicken",
    "chicken_breast",
    "chocolate",
    "coffee",
    "corn",
    "cucumber",
    "egg",
    "eggs",
    "energy_drink",
    "fish",
    "flour",
    "garlic",
    "goat_cheese",
    "grated_cheese",
    "green_beans",
    "ground_beef",
    "guacamole",
    "ham",
    "heavy_cream",
    "humus",
    "ketchup",
    "leek",
    "lemon",
    "lettuce",
    "lime",
    "mango",
    "marmelade",
    "mayonaise",
    "milk",
    "mushrooms",
    "mustard",
    "nuts",
    "onion",
    "pak_choi",
    "pear",
    "pineapple",
    "potato",
    "potatoes",
    "pudding",
    "rice_ball",
    "salad",
    "sandwich",
    "sausage",
    "shrimp",
    "smoothie",
    "spinach",
    "spring onion",
    "strawberries",
    "sugar",
    "sweet_potato",
    "tomato",
    "tomato_sauce",
    "tortillas",
    "turkey",
    "yogurt",
]


def process_recipes(json_path):
    ingredient_to_recipes = defaultdict(list)
    with open(json_path, "r") as file:
        data = json.load(file)

    for id, recipe in data.items():
        for string in recipe["ingredients"]:
            print("string: ", string)
            for ingredient in INGREDIENTS:
                print("ingredient: ", ingredient)
                if ingredient in string:
                    ingredient_to_recipes[ingredient.lower()].append(recipe["title"])
                    break

    with open("ingredient_to_recipes.json", "w") as f:
        json.dump(ingredient_to_recipes, f, indent=4)


json_arrays = []

paths = [
    "recipes_raw_nosource_ar.json",
    "recipes_raw_nosource_epi.json",
    "recipes_raw_nosource_fn.json",
]

#process_recipes(paths[0])


# {
#   "rmK12Uau.ntP510KeImX506H6Mr6jTu": {
#     "title": "Slow Cooker Chicken and Dumplings",
#     "ingredients": [
#       "4 skinless, boneless chicken breast halves ADVERTISEMENT",
#       "2 tablespoons butter ADVERTISEMENT",
#       "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
#       "1 onion, finely diced ADVERTISEMENT",
#       "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
#       "ADVERTISEMENT"
#     ],
#     "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
#     "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
#   },


#  {
#   "05zEpbSqcs9E0rcnCJWyZ9OgdH0MLby": {
#     "ingredients": [
#       "12 egg whites",
#       "12 egg yolks",
#       "1 1/2 cups sugar",
#       "3/4 cup rye whiskey",
#       "12 egg whites",
#       "3/4 cup brandy",
#       "1/2 cup rum",
#       "1 to 2 cups heavy cream, lightly whipped",
#       "Garnish: ground nutmeg"
#     ],
#     "picture_link": null,
#     "instructions": "Beat the egg whites until stiff, gradually adding in 3/4 cup sugar. Set aside. Beat the egg yolks until they are thick and pale and add the other 3/4 cup sugar and stir in rye whiskey. Blend well. Fold the egg white mixture into the yolk mixture and add the brandy and the rum. Beat the mixture well. To serve, fold the lightly whipped heavy cream into the eggnog. (If a thinner mixture is desired, add the heavy cream unwhipped.) Sprinkle the top of the eggnog with the nutmeg to taste.\nBeat the egg whites until stiff, gradually adding in 3/4 cup sugar. Set aside. Beat the egg yolks until they are thick and pale and add the other 3/4 cup sugar and stir in rye whiskey. Blend well. Fold the egg white mixture into the yolk mixture and add the brandy and the rum. Beat the mixture well. To serve, fold the lightly whipped heavy cream into the eggnog. (If a thinner mixture is desired, add the heavy cream unwhipped.) Sprinkle the top of the eggnog with the nutmeg to taste.",
#     "title": "Christmas Eggnog "
#   },


# {
#   "p3pKOD6jIHEcjf20CCXohP8uqkG5dGi": {
#     "instructions": "Toss ingredients lightly and spoon into a buttered baking dish. Top with additional crushed cracker crumbs, and brush with melted butter. Bake in a preheated at 350 degrees oven for 25 to 30 minutes or until delicately browned.",
#     "ingredients": [
#       "1/2 cup celery, finely chopped",
#       "1 small green pepper finely chopped",
#       "1/2 cup finely sliced green onions",
#       "1/4 cup chopped parsley",
#       "1 pound crabmeat",
#       "1 1/4 cups coarsely crushed cracker crumbs",
#       "1/2 teaspoon salt",
#       "3/4 teaspoons dry mustard",
#       "Dash hot sauce",
#       "1/4 cup heavy cream",
#       "1/2 cup melted butter"
#     ],
#     "title": "Grammie Hamblet's Deviled Crab",
#     "picture_link": null
#   },


def clean_recipe(json_file):
    """Generate json file with recipe title as key"""
    with open(json_file, "r") as file:
        datas = json.load(file)
    result = {}
    for key, value in datas.items():
        title = value.pop('title')
        result[title] = value
    with open("./recipe_to_ingredients.json", "w") as json_file:
        json.dump(result, json_file)
    


 # clean_recipe('./recipes_raw_nosource_ar.json')
