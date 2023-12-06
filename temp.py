def get_recipe(f, cook_book, name):
    cook_book[name] = []
    ingredients_amount = int(f.readline().strip())
    for i in range(ingredients_amount):
        ingredient = f.readline().strip().split(' | ')
        cook_book[name].append({'ingredient_name': ingredient[0], 
                                'quantity': ingredient[1], 
                                'measure': ingredient[2]})
    gap = f.readline()

def get_recipes():
    cook_book = {}
    with open('1/recipes.txt', 'r', encoding='UTF-8') as f:
        while True:
            name = f.readline().strip()
            if name == '':
                return cook_book
            get_recipe(f, cook_book, name)

def get_shop_list_by_dishes(dishes, person_count):