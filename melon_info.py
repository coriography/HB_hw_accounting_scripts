"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melon_type, attributes in melons.items():
        print('\n', melon_type.upper(), '\n')
        for melon_attr, val in attributes.items():
            print(f'{melon_attr}: {val}')

print_melon(melons)