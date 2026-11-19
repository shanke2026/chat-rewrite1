def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))


def total(*args):
    return sum(args)
print(total(1, 2, 3)) 
print(total(5))       


def show(**kwargs):
    print(kwargs)
show(name="小明", age=20)