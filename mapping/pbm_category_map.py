categories = {
    'category_1': {
        1: {
            '1': 'NO PREFERENTE'
        }
    },
    'category_2': {
        2: {
            '3': 'NON FORMULARY BRAND'
        }
    },
    'category_3': {
        3: {
            'A': 'PREFERENTE'
        }
    }

}


def get_category_id(name):
    return list(categories[name].keys())[0]


def get_category_code(name):
    category = categories[name]
    category_id = list(category.keys())[0]
    return list(category[category_id].keys())[0]
