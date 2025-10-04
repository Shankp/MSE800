"""Main script to execute data analysis using the DataChecker class."""

from typing import Union


class DataChecker:
    """Analyzes input data for length and uppercase characters."""

    def __init__(self, data: Union[str, list]):
        """Initialize with data (string or list)."""
        if not isinstance(data, (str, list)):
            raise TypeError("Data must be a string or a list.")
        self.data = data

    def total_length(self) -> int:
        """Return the total length of the data."""
        return len(self.data)

    def count_uppercase(self) -> int:
        """Count uppercase characters in the data."""
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isupper())
        return sum(1 for item in self.data if isinstance(item, str) and item.isupper())

    def count_digits(self) -> int:
        """Count digit characters in the data."""
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isdigit())
        return sum(
            1 for item in self.data
            if isinstance(item, str) and item.isdigit()
        )

    def count_special_characters(self) -> int:
        """Count special characters in the data, excluding spaces."""
        if isinstance(self.data, str):
            return sum(
                1 for char in self.data
                if not char.isalnum() and not char.isspace()
            )
        return sum(
            1 for item in self.data
            if isinstance(item, str) and not item.isalnum() and not item.isspace()
        ) 
