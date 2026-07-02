class RecipeAgent:

    def recommend(self, recipe):

        return {
            "name": recipe["recipe_name"],
            "ingredients": recipe["ingredients"],
            "instructions": recipe["instructions"]
        }