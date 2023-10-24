### .lexc File Parser for Apertium Project

The .lexc File Parser is a tool designed to analyze files in the .lexc format used in the Apertium project. It provides several useful functions, including:

- Listing parts of speech in the language.
- Parsing and visualizing a tree from any node within a specified depth.
- Counting lemmas in any specific parts of speech.

### Installation

To install the .lexc File Parser, you can clone the GitHub repository using the following command:

```bash
git clone https://github.com/elleish/sakha_language_tools
```

### Usage

Once this python package is installed, you can use it to analyze .lexc files for the Apertium project.

1. Import this python package: `import lexc_parser as lp`
2. Load the .lecx file `Sakha = lp.download('Sakha')`, `Kazakh = lp.download('Kazakh')`, `Kyrgyz = lp.download('Kyrgyz')` or another language 
3. Parse the .lecx file into tree: `tree = lp.Tree(Sakha)`, `tree = lp.Tree(Kazakh)` or another language   
4. Examine the parts of speech in the language: `tree.tree['Root']`
5. Count the lemmas in a specific part of speech: `len(tree.tree['Verbs'])`, `len(tree.tree['Nouns'])`, etc.
6. List of tree nodes `tree.tree.keys()`  
7. Visualize a tree from any node: `tree.tree('N1')`
8. Visualize a tree from any node with a specified depth: `tree.tree('Nouns', depth_restrict=4)` 
9. Additional examples can be found in the `examples.py` or `examples.ipynb` files.
