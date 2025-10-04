"""Main script to execute data analysis using the DataAnalyzer class."""

from data_checker import DataChecker


def run_analysis(data):
    """
    Run analysis on the provided data and print results.

    """
    analyzer = DataChecker(data)
    print(f"Total length: {analyzer.total_length()}")
    print(f"Uppercase count: {analyzer.count_uppercase()}")
    print(f"Digit count: {analyzer.count_digits()}")
    print(f"Special character count: {analyzer.count_special_characters()}")


if __name__ == "__main__":
    user_input1 = input("Please enter a sentence to check:")
    run_analysis(user_input1)
