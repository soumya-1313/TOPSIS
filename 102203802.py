
import sys
import os
import pandas as pd
import numpy as np

def validate_input_file(input_file, weights, impacts):
    """Validates the input file and checks structure, weights, and impacts."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Error: File '{input_file}' not found.")
    
    # Load file based on extension
    if input_file.endswith('.csv'):
        data = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        data = pd.read_excel(input_file)
    else:
        raise ValueError("Error: Input file must be in .csv or .xlsx format.")

    # Ensure the file has at least 3 columns
    if data.shape[1] < 3:
        raise ValueError("Error: Input file must contain at least 3 columns.")

    # Validate numeric values in the columns (from 2nd to last column)
    if not data.iloc[:, 1:].apply(lambda col: col.map(lambda x: isinstance(x, (int, float, np.number)))).all().all():
        raise ValueError("Error: From the second column onward, all values must be numeric.")



    # Check if weights and impacts match the number of criteria
    if len(weights) != len(impacts):
        raise ValueError("Error: Number of weights and impacts must match the number of criteria.")

    # Validate impacts
    if any(impact not in ['+', '-'] for impact in impacts):
        raise ValueError("Error: Impacts must be either '+' or '-'.")

    return data

def calculate_topsis(data, weights, impacts):
    """Computes the TOPSIS scores and ranks."""
    matrix = data.iloc[:, 1:].values.astype(float)  # Exclude the first column (names/IDs)
    weights = np.array(weights).astype(float)
    impacts = np.array(impacts)

    # Step 1: Normalize the matrix
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Step 2: Multiply by weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and ideal worst
    ideal_best = np.max(weighted_matrix, axis=0) if impacts[0] == '+' else np.min(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0) if impacts[0] == '+' else np.max(weighted_matrix, axis=0)

    # Step 4: Calculate distances from ideal best and worst
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate TOPSIS score
    topsis_score = dist_worst / (dist_best + dist_worst)

    # Step 6: Rank the alternatives
    ranks = topsis_score.argsort()[::-1] + 1  # Descending order

    return topsis_score, ranks

def save_result_file(data, scores, ranks, output_file):
    """Saves the result to the output file with additional columns."""
    data['TOPSIS Score'] = scores
    data['Rank'] = ranks
    data.to_csv(output_file, index=False)
    print(f"Results successfully saved to '{output_file}'.")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print('Example: python 102203802.py 102203802-data.csv "1,1,1,1,1" "+,+,-,+,-" 102203802-result.csv')
        sys.exit(1)

    # Parse command-line arguments
    input_file = sys.argv[1]
    weights = sys.argv[2].split(',')
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    try:
        # Validate input file and arguments
        data = validate_input_file(input_file, weights, impacts)

        # Perform TOPSIS
        scores, ranks = calculate_topsis(data, weights, impacts)

        # Save the result file
        save_result_file(data, scores, ranks, output_file)

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
