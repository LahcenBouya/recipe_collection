import time


class Recipe:
    def __init__(self, name, ingredients, time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def display_recipe(self):
        print("Displaying recipe.....")
        time.sleep(3)
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooking Time: {self.time}")
        print(f"Instructions: {self.instructions}")
        print("-" * 30)


def create_recipe():
    name_of_recipe = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma separeted): ")
    cooking_time = input("Enter cooking time: ")
    cooking_instructions = input("Enter cooking instructions: ")
    return Recipe(name_of_recipe, ingredients, cooking_time, cooking_instructions)
print("Welcome to recipe collection:\n")
recipe = create_recipe()

print("Recipe added successfully!\n")
print("displaying recipe.......")
time.sleep(3)
recipe.display_recipe()

