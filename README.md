# proj631-huffman

A python project to compress data based on character frequency


## Explanation of the algorithm

![image](https://user-images.githubusercontent.com/54810120/111121329-cbf93080-856c-11eb-94d3-18ba8f5ebc4e.png)


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

