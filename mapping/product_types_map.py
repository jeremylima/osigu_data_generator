product_types = {
    1: 'drug',
    2: 'laboratory',
    3: 'diagnostic test',
    4: 'medical service',
    5: 'medical procedure',
    6: 'medical equipment'

}


def get_product_type_name(product_type_id):
    return product_types[product_type_id]
