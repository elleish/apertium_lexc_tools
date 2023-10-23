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

Once the parser is installed, you can use it to analyze .lexc files for the Apertium project.
-get the lexc file `!wget https://raw.githubusercontent.com/apertium/apertium-sah/master/apertium-sah.sah.lexc`</li>
 -kazakh language `!wget https://raw.githubusercontent.com/apertium/apertium-kaz/master/apertium-kaz.kaz.lexc`</li>
 -tatar language `!wget https://raw.githubusercontent.com/apertium/apertium-tat/master/apertium-tat.tat.lexc`</li>
 -kyrgyz language `!wget https://raw.githubusercontent.com/apertium/apertium-kir/master/apertium-kir.kir.lexc`</li>
 -tuvan language `!wget https://raw.githubusercontent.com/apertium/apertium-tyv/master/apertium-tyv.tyv.lexc`</li>
-Check parts of speech in the language `tree() `</li>
-Count lemmas in part of speech `count('Nouns')`</li>
-Visulizing a tree from any node `tree('Nouns')`</li>
-Visulizing a tree from any node with prescribed depth `tree('Nouns', depth=4)`</li>  
