import requests
import json

class APIExtractor:
    def __init__(self):
        pass

    def extract_data_using_url(self, url, save_to_file=False, 
                               file_path=None, authentication_token=None):
        try:
            headers = {}
            if authentication_token:
                headers['Authorization'] = f'Bearer {authentication_token}'

            response = requests.get(url, headers=headers)
            response.raise_for_status()  

            if save_to_file and not file_path:
                print("File path must be provided if save_to_file is True.")
                return None
            
            if save_to_file and file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f, indent=4)
                    
                print(f"Data saved to {file_path}")
                
            return response.json()
        except Exception as e:
            print(f"Error fetching data from API: {e}")
            return None