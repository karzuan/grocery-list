def show_help():
    print("""
    Enter 'HELP' if you need help
    Enter 'DONE' if you want to finish the list
    Enter 'LIST' if you want to see the list
    """)

grocery_list = []
def add_an_item(an_item):
    grocery_list.append(an_item)
    print("'{}' has been added to the list. Now you have {} items in your grocery list.".format(an_item, len(grocery_list)))

def show_the_list():
    print('Here\'s our list to buy( total {} items):'.format(len(grocery_list)))
    for item in grocery_list:
        print("* ", item)


print("What should we pick up at the store?")

show_help()

while True:
    #do this
    item = input("> ")

    #if DONE break the loop
    if item == "DONE":
        break
    elif item == "HELP":
        show_help()
        continue
    elif item == "LIST":
        # show all the items in da list
        show_the_list()
        continue
    else:
        add_an_item(item)

show_the_list()
