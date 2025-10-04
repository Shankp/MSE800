"""Main script to execute data analysis."""

from data_checker import DataChecker


def run_checker(data):
    analyzer = DataChecker(data)
    print(f"Total length: {analyzer.total_length()}")
    print(f"Uppercase count: {analyzer.count_uppercase()}")

if __name__ == "__main__":
    print()
    run_checker("Hello World!")
    run_checker(["A", "b", "C", "d", "E"])
