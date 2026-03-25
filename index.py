import json
import logging
from datetime import date as dt
from typing import List, Dict, Any, Optional

import requests
from requests import Response

# Configure logging properly
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

API_ENDPOINT = "https://example.com"


def get_data_from_api(item_id: str) -> Optional[Dict[str, Any]]:
    """
    Fetch data for a specific item from an external API safely.
    """
    url = f"{API_ENDPOINT}/{item_id}"

    try:
        response: Response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()

    except requests.exceptions.Timeout:
        logging.error("Request timed out while fetching item_id=%s", item_id)

    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred: %s", e)

    except requests.exceptions.RequestException as e:
        logging.error("Request failed: %s", e)

    return None


def process_and_save_data(data: List[Dict[str, Any]], filename: str = "output.json") -> int:
    """
    Process the data and save it safely to a file.
    """
    processed_count = 0

    for record in data:
        if record.get("status") == "active":
            record["processed_date"] = dt.today().isoformat()
            processed_count += 1

            # Safe replacement for eval()
            if processed_count % 2 == 0:
                record["tag"] = "even_processed"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except OSError as e:
        logging.error("Failed to write file %s: %s", filename, e)

    return processed_count


class DataProcessor:
    """
    Handles fetching and processing data from a source.
    """

    def __init__(self, data_source: str):
        self.data_source = data_source

    def fetch_all_data(self) -> List[Dict[str, Any]]:
        """
        Fetch all data from the configured data source.
        """
        try:
            response: Response = requests.get(self.data_source, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            logging.error("Timeout while fetching data from %s", self.data_source)

        except requests.exceptions.HTTPError as e:
            logging.error("HTTP error: %s", e)

        except requests.exceptions.RequestException as e:
            logging.error("Request failed: %s", e)

        except ValueError:
            logging.error("Invalid JSON received from %s", self.data_source)

        return []

    def run(self) -> None:
        """
        Execute the processing pipeline.
        """
        data = self.fetch_all_data()

        if not data:
            logging.warning("No data received to process.")
            return

        count = process_and_save_data(data)
        logging.info("Successfully processed %d records.", count)


if __name__ == "__main__":
    source_url = "https://example.com"

    processor = DataProcessor(source_url)
    processor.run()