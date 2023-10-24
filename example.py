import lexc_parser as lp
Sakha = lp.download('Sakha')
tree = lp.Tree(Sakha)

print('------------------------------------')
print('Parts of speech')
print('------------------------------------')
print(tree.tree['Roots'])

print('------------------------------------')
print('Count the lemmas in a specific part of speech')
print('------------------------------------')
print(len(tree.tree['Nouns']))

print('------------------------------------')
print('List of tree nodes')
print('------------------------------------')
print(tree.tree.keys())

print('------------------------------------')
print('N1')
print('------------------------------------')
print(tree.print_tree('N1', depth_restrict=3))

print('------------------------------------')
print('V-IV')
print('------------------------------------')
print(tree.print_tree('V-IV', depth_restrict=3))
