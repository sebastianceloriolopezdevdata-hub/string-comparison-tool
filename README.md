# String Comparison Tool

A Python application for comparing pairs of strings using three metrics:

- Hamming Distance
- Jaccard Similarity
- T Similarity (Tanimoto with character frequencies)

The project applies Object-Oriented Programming (OOP) concepts such as abstraction, inheritance, polymorphism, and separation of responsibilities.

## Project Structure

```text
string-comparison-tool/
├── data/
│   ├── raw/
│   │   └── input.csv
│   └── processed/
│       └── output.csv
├── src/
│   ├── base.py
│   ├── control_flow.py
│   ├── hamming.py
│   ├── input_output.py
│   ├── jaccard.py
│   └── tanimoto.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- pandas

## Installation

Go to the project directory:

```bash
cd string-comparison-tool
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Input File

The program reads:

```text
data/raw/input.csv
```

The CSV file must contain:

```text
input_one,input_two
```

Each row contains two strings to compare.

## How to Run

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Create the output directory if necessary:

```bash
mkdir -p data/processed
```

Run the program from the project root:

```bash
python main.py
```

The generated output is saved to:

```text
data/processed/output.csv
```

## Processing Flow

```text
input.csv
    |
    v
extract_data()
    |
    v
control_flow.run()
    |
    +----> Hamming
    |
    +----> Jaccard
    |
    +----> T Similarity
    |
    v
results
    |
    v
write_output()
    |
    v
output.csv
```

## Output

The output CSV contains:

```text
input_one,input_two,H,J,T
```

Where:

- `H` = Hamming Distance
- `J` = Jaccard Similarity
- `T` = T Similarity

Example:

```text
input_one,input_two,H,J,T
hello,hello,0.0,1.0,1.0
hello,hullo,1.0,0.6,0.6666666666666666
```

For Hamming Distance, strings with different lengths return an empty value because the algorithm requires strings of equal length.

## Class Diagram

```text
                    +------------------------+
                    |    SimilarityMetric    |
                    |         <<ABC>>        |
                    +------------------------+
                    | + calculate(s1, s2)    |
                    +-----------+------------+
                                |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
     +----------------+ +----------------+ +----------------+
     | HammingDistance| |JaccardSimilarity| |  TSimilarity  |
     +----------------+ +----------------+ +----------------+
     | + calculate()  | | + calculate()  | | + calculate()  |
     +----------------+ +----------------+ +----------------+

                    +----------------+
                    |  control_flow  |
                    +----------------+
                    | + run()        |
                    +-------+--------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
          Hamming        Jaccard       TSimilarity
                            |
                            v
                    +----------------+
                    | input_output   |
                    +----------------+
                    | + extract_data()|
                    | + write_output()|
                    +----------------+
```

## Class Responsibilities

### SimilarityMetric
Defines the common interface for all similarity algorithms through the abstract `calculate()` method.

### HammingDistance
Counts the positions that differ between two strings. Both strings must have the same length.

### JaccardSimilarity
Compares the sets of characters in two strings using intersection and union.

### TSimilarity
Compares character frequencies using the sum of minimum frequencies divided by the sum of maximum frequencies.

### input_output.py
Reads the input CSV with Pandas and writes the calculated results to the output CSV.

### control_flow.py
Coordinates the complete process: extraction, metric calculation, and output generation.

### main.py
The entry point of the application. It starts the process by calling `run()`.

## Technologies

- Python
- Pandas
- Object-Oriented Programming
- Abstract Base Classes
- CSV processing
