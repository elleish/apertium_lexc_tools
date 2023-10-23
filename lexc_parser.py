def clear(x):
    return x.split(';')[0].split('!')[0].split('#')[0].strip()

def load_lexc(x):
    f = open(x, "r")
    lexc = f.read()
    lexc_lines = lexc.split('\n')
    tree = dict()
    header, block = '__empty', []
    for line in lexc_lines:
        if line.startswith("LEXICON Root") or line.startswith("Multichar_Symbols") or line.startswith("LEXICON"):
            line = line.split("LEXICON ")[-1]
            tree[header] = block.copy()
            block = []
            header = clear(line)
        else:
            if line != '' and not line.startswith('!'):
                block.append(clear(line))
    return tree
    
def it_is_node(x):
    x = str(x)
    if len(x) > 0:
        return x==x.upper() and x in tree.keys()
    else:
        return False

def triple(x):
    tempa, tempb, tempc = "", "", ""
    if ';' in x:
        x = x.split(';', 1)[0]
    if ':' in x:
        tempa, x = x.split(':', 1)
    if ' ' in x:
        tempb, tempc = x.split(' ', 1)
    else:
        tempc = x
    if not '<' in tempa.strip():
        tempa = ''
    return tempa.strip(), tempb.strip(), tempc.strip()

def go(x, depth_restrict=16, morph='', surface='', depth=1):
    if depth > depth_restrict:
        return
    # print('┃  ' * max(0, depth-1) + '┠──', x)
    visited = []
    if x in tree.keys():
        for line in tree[x]:
            tag, form, node = triple(line)
            if it_is_node(node):
                if line == tree[x][-1]:
                    noder ='┖──'
                else:
                    noder ='┠──'
                print('┃  ' * max(0, depth-1) + noder, (morph + tag).replace("%",""),':', (surface + form).replace("%",""), end=' ')
                if node != 'CLITICS-NO-COP':
                    print(node)
                else:
                    print('')
                visited.append(node)
                if not node in ('CLITICS-NO-COP', 'COPULA', 'CLITICS-INCL-COP', 'CLIT-EMPH'):
                    go(node, depth_restrict=depth_restrict, morph=morph + tag, surface=surface + form,  depth=depth + 1)
    return
