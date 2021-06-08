from PIL import Image

def main():
    img_store = Image.open('shop_icon2.png', 'r').convert("RGBA")
    img_store = img_store.resize((40, 40), Image.ANTIALIAS)

    img_possible_warehouse = Image.open('possible_warehouse_icon.png', 'r').convert("RGBA")
    img_possible_warehouse = img_possible_warehouse.resize((50, 50), Image.ANTIALIAS)

    img_warehouse = Image.open('warehouse_icon.png', 'r').convert("RGBA")
    img_warehouse = img_warehouse.resize((65, 65), Image.ANTIALIAS)

    problem_index = int(input('Which problem set are you visualizing?'))

    try:
        with open("input/loc{}.txt".format(problem_index), "r") as file:
            lines = file.readlines()
    except IOError:
        print("Error while reading file")

    list_stores = []
    list_warehouses = []

    num_warehouses = int(lines[0].split(' ')[0])
    map_size = int(lines[1])

    background = Image.open('mapbackground3.jpg', 'r').convert("RGBA")
    background = background.resize((map_size, map_size), Image.ANTIALIAS)

    for ind, line in enumerate(lines):
        if ind in (0, 1):
            continue

        x = int(line.split(' ')[0])
        y = int(line.split(' ')[1])
        if ind <= num_warehouses + 1:
            list_warehouses.append((x, y))
        else:
            list_stores.append((x, y))

    for store in list_stores:
        background.paste(img_store, store, img_store)

    try:
        with open("solutions/sol{}.txt".format(problem_index), "r") as file:
            sol_strings = file.readline().split(',')
    except IOError:
        print("Error while reading file")

    background_final = background.copy()

    for ind, value in enumerate(sol_strings):
        background.paste(img_possible_warehouse, list_warehouses[ind], img_possible_warehouse)
        if value == "True":
            background_final.paste(img_warehouse, list_warehouses[ind], img_warehouse)

    background.save('images/candidates{}.png'.format(problem_index))
    background_final.save('images/final{}.png'.format(problem_index))

if __name__ == '__main__':
    main()
