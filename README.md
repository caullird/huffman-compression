# proj631-huffman

A python project to compress data based on character frequency

This repository contains files for huffman package and test files for it in `tests/` directory.

## Installation instructions (dev)

Clone the repositories:

```bash
git clone git@github.com:caullird/proj631-huffman.git
```

## Usage

With a string of characters : 

```python
HuffmanCompress("ProjetAlgorithmique", debug = True)
```

With a text file (put the txt file in 'data/initial_data'
```python
HuffmanCompress("fichier.txt",debug = True)
```
You can then see the results with the debug mode or in the 'data/result_data' 

## Unit Test Case

You can run Unit Test Case with

```bash
python3 -m unittest tests/HuffmanTest.py
```

All tests must be passed

