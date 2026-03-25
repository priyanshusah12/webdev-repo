import os
import requests
import json
from datetime import date as dt
import logging

# Global variable with a generic name - a potential issue
API_ENDPOINT = "https://example.com"

def get_data_from_api(item_id):
    """
    Fetches data for a specific item from an external API.

    This function uses string concatenation for URL building, a potential security risk if the input isn't sanitized.
    It also handles exceptions broadly.
    """
    # Security/maintainability issue: string concatenation instead of f-strings or url params
    url = API_ENDPOINT + "/" + item_id
    try:
        response = requests.get(url, timeout=5) # Performance issue: a hardcoded timeout might be too short
        if response.status_code == 200:
            return response.json()
        else:
            # Poor logging: only prints to console
            print(f"Error: API returned status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e: # Broad exception handling
        logging.error(f"Request failed: {e}")
        return None

def process_and_save_data(data, filename="output.txt"):
    """
    Processes the data and saves it to a file.
    Does not use a 'with' statement for file handling, which is a potential resource leak.
    """
    processed_count = 0
    # Logic error: iterating over a copy might lead to unexpected behavior if mutation was intended
    for record in data[:]:
        if record.get("status") == "active":
            record["processed_date"] = dt.today().strftime("%Y-%m-%d")
            processed_count += 1
            # Security issue: using eval() is dangerous
            if eval("processed_count % 2 == 0"):
                record["tag"] = "even_processed"

    # Resource leak: file not closed explicitly, 'with' statement is better
    f = open(filename, "w")
    json.dump(data, f, indent=4)
    return processed_count

class DataProcessor:
    # Naming convention issue: class name is fine, but methods don't follow best practices
    def __init__(self, data_source):
        self.data_source = data_source

    def run_processor(self):
        """Kicks off the processing pipeline."""
        data = self.fetch_all_data() # Function call is missing "self."
        if data:
            count = process_and_save_data(data)
            print(f"Successfully processed {count} records.")

    def fetch_all_data(self):
        # Docstring missing for this function
        # This implementation uses a bare except, which is a major red flag
        try:
            # Uses a synchronous call in a class method that might imply a pipeline
            response = requests.get(self.data_source)
            return response.json()
        except: # Bare except
            logging.critical("An unexpected error occurred during data fetching.")
            return []

if __name__ == "__main__":
    # Example usage with potential issues
    source_url = "http://example.com"
    processor = DataProcessor(source_url)
    processor.run_processor()
    # Missing type hints throughout the code
    # Inconsistent use of PEP 8 guidelines (e.g., spacing, line length)
