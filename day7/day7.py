fin = open("input2.txt", "r")

data = [data.replace('.', '') for data in fin.readlines() if data.strip()]
bags = {}
for x in data:
    splitted = [a.strip() for a in x.split('contain')]
    contained_bags = []
    for x in splitted[1].split(','):
        if x == 'no other bags':
            contained_bags.append('')
        else:
            contained_bags.append(x[2:].replace('bag', 'bags').replace('bagss', 'bags').strip())
    #
    quantities = []
    for x in splitted[1].split(','):
        if x != 'no other bags':
            quantities.append(int(x[:2].strip()))
        else:
            quantities.append('')
    # bags[splitted[0]] = contained_bags
    bags[splitted[0]] = dict(zip(contained_bags, quantities))

for bag in bags:
    if bags[bag] == {'': ''}:
        bags[bag] = {}


# print(bags)
#
# def getbag(_bag, my, found):
#     currentbag = bags.get(_bag)
#     if currentbag:
#         if my not in currentbag:
#             # print(f'{_bag} - searching bag')
#             return any(getbag(i, my, found) for i in currentbag)
#         if _bag not in found:
#             # print(f'{_bag} - contains gold bag')
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# found = ['shiny gold bags']
# mybag = 'shiny gold bags'
# total = 0
# for bag in bags:
#     total += getbag(bag, mybag, found)
# print(f'Part 1: {total}')
#
print(bags)

def getbag_inside_shiny(node: dict):  # sourcery skip
    #print(node)
    # is node end node?
    store = []
    if not node.keys():  # End node
        store.append(1)
    else:
        for value in node:
            #print(f'xxxy {bags[value]}')
            #print(f'node { node[value]}')
            #print(f'len {len(node)}')
            test=(node[value]*(getbag_inside_shiny(bags[value]))*(len(node)))
            store.append(test)
    print(store, node)
    return sum(store)


mybag = 'shiny gold bags'
#a = getbag_inside_shiny({'faded blue bags': 3, 'dotted black bags': 4}) #OK
#a = getbag_inside_shiny({'faded blue bags': 5, 'dotted black bags': 6}) #OK -->11
#print(bags.get(mybag))
a = getbag_inside_shiny(bags.get(mybag)) # 127

print(f'Part 2: {a}')
