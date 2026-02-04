import sys
import pandas as pd
import numpy as np

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
      data = pd.read_csv(input_file)
    except FileNotFoundError:
      print("Error: Input file not found")
      sys.exit(1)

    if data.shape[1] < 3:
      print("Error: Input file must contain at least three columns")
      sys.exit(1)

    weights = weights.split(",")
    impacts = impacts.split(",")

    num_criteria = data.shape[1] - 1

    if len(weights) != num_criteria or len(impacts) != num_criteria:# Yahan per hum no. columns ko match kar rhe hain with no. of weights and impacts provided
        print("Error: Number of weights and impacts must match number of criteria")
        sys.exit(1)

    for impact in impacts:
        if impact not in ['+', '-']:
            print("Error: Impacts must be either '+' or '-'")
            sys.exit(1)
    try:
        data.iloc[:, 1:] = data.iloc[:, 1:].astype(float)
    except ValueError:
        print("Error: Criteria columns must contain numeric values only")
        sys.exit(1)
### Validations end here
    weights = np.array(weights, dtype=float)
    weights = weights / np.sum(weights) # Normazing the Weights
    criteria = data.iloc[:, 1:].values
    norm = np.sqrt((criteria ** 2).sum(axis=0))# normalizing the Values in the matrix
    normalized_matrix = criteria / norm
    weighted_matrix = normalized_matrix * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))
    

    topsis_score = dist_worst / (dist_best + dist_worst)
    data["Topsis Score"] = topsis_score.round(6)
    data["Rank"] = data["Topsis Score"].rank(ascending=False, method='dense').astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully.")


if __name__ == "__main__":
    main()
