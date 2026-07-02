import pandas as pd

class RecipeRetriever:

    def __init__(self):
        self.data = pd.read_csv(
            "data/recipe_dataset.csv"
        )

    def search(self, ingredients):

        best_match = None
        best_score = 0

        for _, row in self.data.iterrows():

            recipe_items = [
                x.strip().lower()
                for x in row["ingredients"].split(",")
            ]

            score = len(
                set(ingredients).intersection(
                    recipe_items
                )
            )

            if score > best_score:
                best_score = score
                best_match = row

        return best_match