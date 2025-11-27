# Data Scanner

A simple and powerful CLI tool for automated CSV data profiling and analysis.

## Features

- **Basic Summary**: Get row count, column count, missing values, and data types
- **Numeric Summary**: Statistical overview of numeric columns
- **Categorical Summary**: Insights into categorical data
- **Insights**: Skewness suggestions, correlation analysis, and cardinality warnings

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-scanner.git
   cd data-scanner
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the profiler on a CSV file:

```bash
python -m data_scanner.cli path/to/your/file.csv
```

Generate a custom output report:

```bash
python -m data_scanner.cli path/to/your/file.csv -o custom_report.md
```

## Example

```bash
python -m data_scanner.cli examples/sample.csv
```

This will generate a `report.md` file with comprehensive data insights.
