spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods ]
    return names

def get_spiciest_foods(spicy_foods):
    spicy = [food for food in spicy_foods if food["heat_level"] > 5]
    return spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)
        
        heat_emojie = "🌶" * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojie}")
        
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        target_cuisine = food.get("cuisine", "Unknown")
        if target_cuisine == cuisine:
            return food
    return None 
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)
        
        heat_emojie = "🌶" * heat_level
        
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojie}")
            

        
        

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    
    return average


def create_spicy_food(spicy_foods, spicy_food):
     updated_spicy_foods = spicy_foods + [spicy_food]
     return updated_spicy_foods