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

1. get the .lexc file `!wget https://raw.githubusercontent.com/apertium/apertium-sah/master/apertium-sah.sah.lexc`

  - kazakh language `!wget https://raw.githubusercontent.com/apertium/apertium-kaz/master/apertium-kaz.kaz.lexc`
  - tatar language `!wget https://raw.githubusercontent.com/apertium/apertium-tat/master/apertium-tat.tat.lexc`
  - kyrgyz language `!wget https://raw.githubusercontent.com/apertium/apertium-kir/master/apertium-kir.kir.lexc`
  - tuvan language `!wget https://raw.githubusercontent.com/apertium/apertium-tyv/master/apertium-tyv.tyv.lexc`

2. import this python package: `import sakha_language_tools.lexc_parser`
3. load the .lecx file into python: `tree = load_lexc("apertium-sah.sah.lexc")` 
4. Examine the parts of speech in the language: `tree['Root']`
5. Count the lemmas in a specific part of speech: `len(tree['Verbs'])`, `len(tree['Nouns'])`, 
6. Visualize a tree from any node: tree('Nouns')
7. Visualize a tree from any node with a specified depth: tree('Nouns', depth=4) 
8. Additional examples can be found in the `examples.ipynb` file.
