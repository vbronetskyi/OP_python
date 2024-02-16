"""Lab_3.Ex_1_markets"""

class Markets:
    """This class outputs a message with the received data: name, area, categories"""
    def __init__(self, name: str, area: int, categories: list) -> None:
        """
        Class constructor
        >>> market_family_food = Markets('Family Food', 80, \
['Bread and Bakery', 'Dairy', 'Beverages'])
        >>> market_family_food.name
        'Family Food'
        >>> market_family_food.area
        80
        >>> market_family_food.categories
        ['Bread and Bakery', 'Dairy', 'Beverages']
        """
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self) -> str:
        """
        outputs a message with the received data
        >>> print(market_family_food)
        Supermarket Family Food has an area of 80 m2 and has the following\
 categories: Bread and Bakery, Dairy, Beverages.
        """
        return "Supermarket %s has an area of %s m2 and has the following categories: %s." \
            %(self.name, self.area, ', '.join(self.categories))

market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
