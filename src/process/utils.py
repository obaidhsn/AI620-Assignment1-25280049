import json
import pandas as pd

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def load_json_data(file_path: str) -> dict:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            return None
    
    @staticmethod
    def save_json_data(data: dict, file_path: str):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error saving JSON data: {e}")

    @staticmethod
    def load_csv_data(file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error loading CSV data: {e}")
            return None
    
    @staticmethod
    def convert_json_to_dataframe(json_data: dict) -> pd.DataFrame:
        try:
            df = pd.json_normalize(json_data)
            return df
        except Exception as e:
            print(f"Error converting JSON to DataFrame: {e}")
            return None
    
    @staticmethod
    def convert_df_to_json(df: pd.DataFrame) -> dict:
        try:
            json_data = df.to_dict(orient='records')
            return json_data
        except Exception as e:
            print(f"Error converting DataFrame to JSON: {e}")
            return None
    
    @staticmethod
    def save_dataframe_to_csv(df: pd.DataFrame, output_file_path: str):
        try:
            df.to_csv(output_file_path, index=False)
            print(f"DataFrame saved to {output_file_path}")
        except Exception as e:
            print(f"Error saving DataFrame to CSV: {e}")