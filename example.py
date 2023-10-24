import lexc_parser as lp
Sakha = lp.download('Sakha')
tree = lp.Tree(Sakha)

print('------------------------------------')
print('Nouns')
print('------------------------------------')
print(tree.tree['Nouns'])

print('------------------------------------')
print('N1')
print('------------------------------------')
print(tree.print_tree('N1', depth_restrict=3))

print('------------------------------------')
print('V-IV')
print('------------------------------------')
print(tree.print_tree('V-IV', depth_restrict=3))
