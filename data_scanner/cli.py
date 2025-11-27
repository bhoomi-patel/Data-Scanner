import argparse
from data_scanner.profiler import DataProfiler
from data_scanner.insights import DataInsights
from data_scanner.report import generate_md_report
def main():
    parser = argparse.ArgumentParser(description="Data-Scanner: Automated CSV Profiler")
    parser.add_argument("csv_path", help="Path to CSV file")
    parser.add_argument("-o", "--output" , default="report.md", help="Output report file(Markdown)")
    args = parser.parse_args() 

    profiler = DataProfiler(args.csv_path)
    summary = profiler.basic_summary()
    numeric_summary = profiler.numeric_summary()
    categorical_summary = profiler.categorical_summary()

    insights = DataInsights(profiler.df)
    insight_data = {
        "skewness":insights.skewness_suggestions(),
        "correlation":insights.correlation_analysis(),
        "cardinality":insights.cardinality_warnings()
    }
    report = generate_md_report(summary,numeric_summary,categorical_summary,insight_data)
    with open(args.output,"w") as f:
        f.write(report)
    print(f"Report generated: {args.output}")
if __name__ == "__main__":
    main()