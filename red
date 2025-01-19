# Topsis-Soumya-102203802

## Overview

**Topsis-Soumya-102203802** is a Python package that implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method for multi-criteria decision-making. It is designed to help users rank alternatives based on their proximity to an ideal best and worst solution.

This package is built to assist decision-makers in evaluating multiple alternatives using several criteria, offering a simple interface for performing the TOPSIS analysis with flexibility for custom weights and impacts for decision criteria.


## Installation

You can install **Topsis-Soumya-102203802** from PyPI using `pip`:

```bash
pip install Topsis-Soumya-102203802

Additionally, make sure you have the required dependencies installed:

```bash
pip install pandas numpy pyexcel

## Features

- **TOPSIS Ranking**: Computes the rankings for alternatives based on their similarity to the ideal solution.
- **Custom Weights**: Supports custom weights for each decision criterion.
- **Custom Impacts**: Allows specifying the impact of each criterion (maximize or minimize).
- **CSV/Excel Input**: Accepts input datasets in CSV or Excel format.
- **Output**: The package generates an output CSV or Excel file with two additional columns: **Topsis Score** and **Rank**.
- **Command-Line and Programmatic Usage**: Available both as a command-line tool and as a Python package for use in scripts.

## Usage
## Command Line Interface
```bash
topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>

##Parameters:

**InputDataFile**: Path to input dataset (CSV/XLSX)
**Weights**: Comma-separated criterion weights (e.g., "1,2,3")
**Impacts**: Comma-separated criterion impacts ('+' for maximize, '-' for minimize)
**ResultFileName**: Output file path for results

##Input Data Format
##File Requirements
1. Must contain at least 3 columns
2. First column: Names of alternatives
3. Columns 2 onwards: Numeric values for criteria

##Output Format
#The package generates a CSV file with the original data plus two additional columns:

1. Topsis Score: Calculated similarity to ideal solution
2. Rank: Final ranking of alternatives

##Prerequisites
#Python 3.6 or higher
##Dependencies:
pandas
numpy
pyexcel
##License
MIT License

##Author
Soumya (GitHub Profile)
