# Auto T&S Graph (Program Forest Analyzer)

A tool for constructing, reducing, and comparing **program structure graphs** to evaluate correctness, behavior, and safety properties of code.

---

## Overview

This project builds a **forest of program structure trees** from source code. Each node represents structural or semantic elements such as:

- Functions
- Function calls
- Control flow blocks
- Relationships between components

The system is designed to:

1. Parse code into a structural representation (forest)
2. Normalize / reduce the forest into a canonical form
3. Compare forests between a reference implementation and a candidate
4. Detect mismatches in logic, structure, or behavior

---

## Key Concepts

### Program Forest
A collection of trees representing code structure across files or modules.

Each tree typically represents:
- A function
- A class
- A logical unit of execution

---

### Nodes

Common node types include:

- Function definitions  
- Calls made within a function

---

### Forest Reduction

The forest is simplified to remove noise and normalize structure:

- Removes irrelevant nodes
- Collapses equivalent patterns
- Standardizes formatting differences
- Handles missing intermediate nodes

---

### Forest Comparison

Two forests are compared to determine similarity:

- Reference implementation (ground truth)
- Candidate implementation

Comparison accounts for:
- Missing nodes
- Extra nodes
- Structural mismatches
- Partial matches (children present, parent missing)

---

## Project Structure

### Classes
This contains all objects used in this program, organized by category.
---

### Extraction
This contains functions that perform the model extraction on the target codebase.
---

### Analysis
This contains functions that will build the model forest, consolidate the observed forest into a tag forest, and compare the two.
--

## Instructions to Run
1. Within the desired codebase, tag each function definition with the desired tags, defined in analysis/build_model_forest.py
2. These tags are of the form - Tag: action, category, subcategory
3. The keyword "tag" must be present, in that order
4. Subcategory is optional, but action and category are not
6. Open main.py
7. Run the program
8. When prompted, enter the absolute path to the codebase

