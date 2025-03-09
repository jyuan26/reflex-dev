import pandas as pd
import re

def fix_latex_for_reflex(text):
    if pd.isna(text):
        return text  # Skip if empty
    
    # Convert block math \[ ... \] to $$ ... $$
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text, flags=re.DOTALL)

    # Convert inline math \( ... \) to $ ... $
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text)

    # Ensure percentage expressions (e.g., 30\%) are wrapped in dollar signs
    text = re.sub(r'(?<!\$)(\d+\\%)', r'$\1$', text)

    # Wrap LaTeX commands not inside dollar signs
    pattern = r"(?<!\$)(\\[a-zA-Z]+(?:\{.*?\})?)(?!\$)"
    text = re.sub(pattern, r"$\1$", text)

    return text

def process_csv(input_file, output_file):
    # Load CSV file
    df = pd.read_csv(input_file)

    # Ensure 'Problem latex' column exists
    if "Problem latex" not in df.columns:
        raise ValueError("CSV file must contain a 'Problem latex' column.")

    # Apply the function to the 'Problem latex' column
    df["Problem latex"] = df["Problem latex"].apply(fix_latex_for_reflex)

    # Save the modified CSV
    df.to_csv(output_file, index=False)
    print(f"Processed CSV saved to {output_file}")

# Example usage
input_csv = "./quiz/bmt-problems.csv"
output_csv = "./quiz/bmt-problems_fixed.csv"
process_csv(input_csv, output_csv)
print(f"Processed CSV saved to {output_csv}")
