# Project Description

Quick-Calc is a small calculator application that supports following operations: addition, subtraction, multiplication, and division (division by zero handled). It also includes a Clear (C) action that resets the current input and result.  
This repository is created for a Software Testing & Quality Assurance practical assignment and focuses on clean, testable code and a multi-layered testing strategy.

# Setup and Run Instructions
1) Install Python (3.10+ recommended).  
2) Open a terminal in the project folder (where `requirements.txt` is).  
3) Install dependencies:
```bash
py -m pip install -r requirements.txt
```
4)Run the application
```bash
py -m quick_calc.cli
```
# How to Run all Tests
```bash
py -m pytest -q
```
# Testing Framework Research
unittest is the simplest method that comes to mind, it’s simple, you don’t need to download anything, probably the most popular, but the tests look cumbersome and are not very pleasant to read. 

However, there is an external pytest method that makes tests simpler, shorter and more readable, although this is an add-on that you need to install, this solution improves the design and also has powerful fixtures, and good error output. I chose it because it is easier and improves readability, and makes it faster to write and maintain a meaningful test suite.
