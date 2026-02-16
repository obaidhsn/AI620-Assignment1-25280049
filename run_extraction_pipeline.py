from datetime import datetime
from pathlib import Path
import shutil
import pandas as pd

from paths import FilePaths
from src.extract.extract_public_dataset import PublicDatasetExtractor
from src.extract.extract_api import APIExtractor
from src.extract.extract_time_series import TimeSeriesExtractor
from src.process.utils import Utils
from src.process.process_api_data import APIDataProcessor
from config import config

def create_dated_directory(base_path: str) -> Path:
    path = Path(base_path) / str(datetime.now().date())
    path.mkdir(parents=True, exist_ok=True)
    return path


raw_output_dir = create_dated_directory(FilePaths.RAW_DATA_DIR.value)
processed_output_dir = FilePaths.PROCESSED_DATA_DIR.value


public_dataset_extractor = PublicDatasetExtractor()
api_extractor = APIExtractor()
trends_data_extractor = TimeSeriesExtractor()
api_data_processor = APIDataProcessor()


def process_dataframe_file(df: pd.DataFrame, file_path: Path, output_dir: Path):
    try:
        shutil.copy2(file_path, output_dir / file_path.name)

        json_data = Utils.convert_df_to_json(df)
        Utils.save_json_data(
            json_data,
            output_dir / f"{file_path.stem}.json"
        )

        print(f"Processed file: {file_path.name}")

    except Exception as e:
        print(f"Error processing file {file_path.name}: {e}")

def run_pipeline():

    print("Starting EL Pipeline\n")
    print("Starting Extraction Layer")

    # ---------------------------------------------------
    # Extraction
    # ---------------------------------------------------

    try:
        dataset_id = config.KAGGLE_DATASET
        public_data_file_path = public_dataset_extractor.download_dataset_from_kaggle(
            dataset_id,
            file_to_download="ai_job_market.csv",
            output_dir=raw_output_dir
        )
        print("Public dataset extracted successfully.\n")

    except Exception as e:
        print(f"Error extracting public dataset: {e}")
        public_data_file_path = None

    try:
        url = config.API_DATA_LINK
        api_data_file_path = raw_output_dir / "api_data_jobdataapi_ai.json"

        api_extractor.extract_data_using_url(
            url=url,
            save_to_file=True,
            file_path=api_data_file_path
        )

        print("API data extracted successfully.\n")

    except Exception as e:
        print(f"Error extracting API data: {e}")
        api_data_file_path = None

    try:
        keywords = config.PYTRENDS_KEYWORDS

        trends_data_file_path = raw_output_dir / "ai_trends_data.csv"

        trends_data_extractor.google_trends_extractor(
            keywords=keywords,
            output_file_path=trends_data_file_path,
            timeframe="today 5-y"
        )

        print("Google Trends data extracted successfully.\n")

    except Exception as e:
        print(f"Error extracting Google Trends data: {e}")
        trends_data_file_path = None

    # ---------------------------------------------------
    # Processing
    # ---------------------------------------------------

    print("Starting Processing Layer")

    try:
        if api_data_file_path:
            api_data_processor.process_data_to_json_and_csv(
                input_path=api_data_file_path,
                output_dir=processed_output_dir
            )
            print("API data processed successfully.\n")

    except Exception as e:
        print(f"Error processing API data: {e}")

    if public_data_file_path:
        public_dataset_df = Utils.load_csv_data(public_data_file_path)
        process_dataframe_file(public_dataset_df, public_data_file_path, processed_output_dir)

    if trends_data_file_path:
        trends_data_df = Utils.load_csv_data(trends_data_file_path)
        process_dataframe_file(trends_data_df, trends_data_file_path, processed_output_dir)

    print("Pipeline completed.")


if __name__ == "__main__":
    run_pipeline()
