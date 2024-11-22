import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')
print(f'This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}')

