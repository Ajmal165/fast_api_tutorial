def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("Ajmal", "Hossain"))



def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e



from typing import Any
def some_function(data: Any):
    print(data)


'''Some types can take "type parameters" in square brackets, to define their internal types,
 for example a "list of strings" would be declared list[str].'''

def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items_set(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
