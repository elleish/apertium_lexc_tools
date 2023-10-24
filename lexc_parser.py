import os
from urllib.request import urlretrieve

def clear(x):
    return x.split(';')[0].split('!')[0].split('#')[0].strip() 

# parsing a line of a .lexc file
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

class Tree:
    def __init__(self, lexcfile):     # load .lexc file and parse by first stage
        self.tree = dict()
        f = open(lexcfile, "r", encoding="utf-8")
        self.lexc_plain = f.read()
        self.lexc_lines = self.lexc_plain.split('\n')
        header, block = '__empty', []
        for line in self.lexc_lines:
            if line.startswith("LEXICON Root") or line.startswith("Multichar_Symbols") or line.startswith("LEXICON"):
                line = line.split("LEXICON ")[-1]
                self.tree[header] = block.copy()
                block = []
                header = clear(line)
            else:
                if line != '' and not line.startswith('!'):
                    block.append(clear(line))

    def it_is_node(self, x):     # all nodes are written in uppercase
        x = str(x)
        if len(x) > 0:
            return x==x.upper() and x in self.tree.keys()
        else:
            return False

    def print_tree(self, x, depth_restrict=16, morph='', surface='', depth=1):
    #     return pt(x, depth_restrict=depth_restrict, morph=morph, surface=surface, depth=depth)
    #
    # # printing .lexc recurrently
    # def pt(x, depth_restrict=16, morph='', surface='', depth=1):
        if depth > depth_restrict:
            return
        visited = []
        if x in self.tree.keys() and len(self.tree[x]) < 256:
            for line in self.tree[x]:
                tag, form, node = triple(line)
                if self.it_is_node(node):
                    if line == self.tree[x][-1]:
                        node_symbol ='┖──'
                    else:
                        node_symbol ='┠──'
                    print('┃  ' * max(0, depth-1) + node_symbol, (morph + tag).replace("%",""),':', (surface + form).replace("%",""), end=' ')
                    visited.append(node)
                    if not node in ('CLITICS-NO-COP', 'COPULA', 'CLITICS-INCL-COP', 'CLIT-EMPH'):
                        print(node)
                        self.print_tree(node, depth_restrict=depth_restrict, morph=morph + tag, surface=surface + form,  depth=depth + 1)
                    else:
                        print('')


def download(lang="Sakha"):
    if lang.lower() in ("kazakh", "kaz", "казах", "каз"):
        lang, url = "Kazakh", "https://raw.githubusercontent.com/apertium/apertium-kaz/master/apertium-kaz.kaz.lexc"
    elif lang.lower() in ("tatar", "tat", "татар", "тат"):
        lang, url = "Tatar", "https://raw.githubusercontent.com/apertium/apertium-tat/master/apertium-tat.tat.lexc"
    elif lang.lower() in ("kyrgyz", "kyr", "kirgiz", "kir", "кыргыз", "кыр", "кир"):
        lang, url = "Kyrgyz", "https://raw.githubusercontent.com/apertium/apertium-kir/master/apertium-kir.kir.lexc"
    elif lang.lower() in ("tyvan", "tyv", "tuvan", "tuv",  "тыва", "тыв"):
        lang, url = "Tuvan", "https://raw.githubusercontent.com/apertium/apertium-tyv/master/apertium-tyv.tyv.lexc"
    else:
        lang, url = "Sakha", "https://raw.githubusercontent.com/apertium/apertium-sah/master/apertium-sah.sah.lexc"

    lexcfile = url.split('/')[-1]
    if os.path.exists(lexcfile):
        print("Found the .lexc file of ", lang, "language")
    else:
        try:
            urlretrieve(url, lexcfile)
            # os.system(f"wget -c --read-timeout=5 --tries=2 '{url}'")
            print("The .lexc file of ", lang, "downloaded from", url)
        except:
            print("Cannot download", url)
    return lexcfile