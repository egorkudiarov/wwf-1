def get_recipe(f, cook_book, name):
    cook_book[name] = []
    ingredients_amount = int(f.readline().strip())
    for i in range(ingredients_amount):
        ingredient = f.readline().strip().split(' | ')
        cook_book[name].append({'ingredient_name': ingredient[0], 
                                'quantity': int(ingredient[1]), 
                                'measure': ingredient[2]})
    gap = f.readline()

def get_recipes(path):
    cook_book = {}
    with open(path, 'r', encoding='UTF-8') as f:
        while True:
            name = f.readline().strip()
            if name == '':
                return cook_book
            get_recipe(f, cook_book, name)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_recipes('1, 2/recipes.txt')
    shoping_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if shoping_list.get(ingredient['ingredient_name']):
                shoping_list['ingredient']['quantity'] += ingredient['quantity'] * person_count
            else:
                shoping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 
                                                               'quantity': ingredient['quantity'] * person_count}
    return shoping_list