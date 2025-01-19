# TOPSIS
# TOPSIS Algorithm Implementation

## Overview
The TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method is a multi-criteria decision-making approach. This Python implementation computes rankings for alternatives based on their proximity to ideal best and worst solutions.

---

## PyPI Package
This implementation is available as a Python package on [`https://pypi.org/project/Topsis-Soumya-102203802/1.0.0/`](https://pypi.org/project/Topsis-Soumya-102203802/1.0.0/). You can easily install it via `pip`:

```bash
pip install Topsis-Soumya-102203802==1.0.0
```
---

## Features
- Custom **weights** and **impacts** for decision criteria.
- Calculates **Topsis Score** and **Rank** for alternatives.
- Saves results to a specified **output file**.
- Robust validation for data and inputs.

---

## Prerequisites
- Python 3.6 or higher
- Required Libraries: `pandas`, `numpy`, `pyexcel`


Install dependencies using:
```bash
pip install pandas numpy pyexcel
```

---

## How to Use
### Command-Line Usage
```bash
python <script_name.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>
```
### Parameters
1. **InputDataFile**: Path to the dataset file (CSV/XLSX). The first column lists alternatives, followed by numeric data for criteria.
2. **Weights**: Comma-separated values for criterion importance (e.g., `"1,2,3"`).
3. **Impacts**: Comma-separated values (`+` for maximize, `-` for minimize) indicating desired impact for each criterion (e.g., `"+,-,+"`).
4. **ResultFileName**: Name of the output file where results will be saved.

### Example Command
```bash
python 102203802.py 102203802-data.xlsx "1,1,1,1,1" "+,+,-,+,+" 102203802-result.csv
```

---

## Input Data Format
1. Input file must contains 3 or more columns.
2. First column is object/variable name.
3. Subsequent columns with numeric values for criteria.


---

## Output
The output file includes:
- **Topsis Score**: Calculated score for each alternative.
- **Rank**: Rank based on the Topsis Score.

---

## Error Handling
The script validates:
- Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
- Show the appropriate message for wrong inputs.
- Handling of “File not Found” exception
- Number of weights, number of impacts and number of columns (from 2nd to last columns) must
be same.
- Impacts must be either +ve or -ve.
- Impacts and weights must be separated by ‘,’ (comma).
