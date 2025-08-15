import pandas as pd

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def convert_to_pd(self):
        try:
            df = pd.read_csv(self.filename)
            print(df.head())
            df.to_parquet("google_review_ratings.parquet", engine='pyarrow', index=False)
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_average_rating(self, column_name):
        try:
            df = pd.read_csv(self.filename)
            average_rating = df[column_name].mean()
            print(f"Average Rating: {average_rating}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def Calculate_maximum_rating(self, column_name):
        try:
            df = pd.read_csv(self.filename)
            max_rating = df[column_name].max()
            print(f"Maximum Rating: {max_rating}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_minimum_rating(self, column_name):
        try:
            df = pd.read_csv(self.filename)
            min_rating = df[column_name].min()
            print(f"Minimum Rating: {min_rating}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
def main():
    file = FileHandler('google_review_ratings.csv')
    columnName = input("Enter the column name to be used for calculations: ")
    file.convert_to_pd()
    file.calculate_average_rating(columnName)
    file.Calculate_maximum_rating(columnName)
    file.calculate_minimum_rating(columnName)
    

if __name__ == "__main__":
    main()