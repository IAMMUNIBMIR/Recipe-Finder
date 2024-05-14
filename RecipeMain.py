import requests

APP_ID = "cd4948ce" 
APP_KEY = "cf08bb7dbee0ac81a74259ec55644b21" 
BASE_URL = 'https://api.edamam.com/search'

def get_recipes(query, number=5):
    params = {
        'q': query,
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'to': number
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('hits', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def print_recipes(recipes):
    for idx, recipe in enumerate(recipes):
        recipe_info = recipe['recipe']
        print(f"{idx + 1}. {recipe_info['label']}")
        print(f"   Recipe URL: {recipe_info['url']}")
        print(f"   Ingredients: {', '.join([ingredient['text'] for ingredient in recipe_info['ingredients']])}")
        print()

def main():
    query = input("Enter the recipe name or ingredients you are looking for: ")
    recipes = get_recipes(query)
    if recipes:
        print(f"\nFound {len(recipes)} recipes:")
        print_recipes(recipes)
    else:
        print("No recipes found. Try a different query.")

if __name__ == "__main__":
    main()
