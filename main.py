class CookBook:
    def __init__(self):
        self.cook_book = {}

    def __str__(self):
        """
        Dictionary's formatted return.
        """
        res = '{\n'
        for dish, recipe in self.cook_book.items():
            res += f'\'{dish}\' :[\n'
            for ingr in recipe:
                res += f'    {str(ingr)}\n'
            res += f'    ],\n'
        return res[:-2] + '\n}'

    def read_recipes(self, filename):
        """
        Function reads file (as parameter) and fill cook book dictionary.
        :param filename:
        :return:
        """
        with open(filename, 'r', encoding='UTF-8') as recipeFile:
            cur_recipe = recipeFile.readline().strip()
            for line in recipeFile:
                s = line.strip()
                if '|' in line:
                    ingredient, quantity, measure = s.split(' | ')
                    if cur_recipe in self.cook_book.keys():
                        self.cook_book[cur_recipe].append({'ingredient_name': ingredient,
                                                           'quantity': int(quantity),
                                                           'measure': measure})
                    else:
                        self.cook_book[cur_recipe] = [{'ingredient_name': ingredient,
                                                       'quantity': int(quantity),
                                                       'measure': measure}]
                elif not s.isdigit() and s != '':
                    cur_recipe = s

    def get_shop_list_by_dishes(self, dishes, person_count):
        """
        Function returns total quantity of all dishes in the list.

        :param dishes:
        :param person_count:
        :return:
        """
        product_dict = {}
        for dish in dishes:
            for elem in self.cook_book[dish]:
                ingredient, quantity, measure = elem.values()
                if ingredient in product_dict.keys():
                    product_dict[ingredient]['quantity'] += quantity * person_count
                else:
                    product_dict[ingredient] = {'measure': measure,
                                                'quantity': quantity * person_count}
        # return product_dict
        # Additional output with format
        res = '{\n'
        for product, counts in product_dict.items():
            res += f'    \'{product}\' : {counts}\n'
        return res[:-2] + '\n}'


cb = CookBook()
cb.read_recipes("recipes.txt")
print('Cok book from recipe.txt:\n', cb)
print()
print('Ingredients for three dishes:\n', cb.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
