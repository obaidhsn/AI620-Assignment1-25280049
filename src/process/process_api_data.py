from src.process.utils import Utils

class APIDataProcessor:
    def __init__(self):
        pass

    def process_api_data(self, api_data: dict) -> dict:
        processed_data = []

        for jobs in api_data.get('results', []):
            id = jobs.get('id', -1)
            title = jobs.get('title', 'N/A')
            company_name = jobs.get('company', 'N/A').get('name', 'N/A')
            company_website = jobs.get('company', {}).get('website_url', 'N/A')
            company_linkedin = jobs.get('company', {}).get('linkedin_url', 'N/A')
            company_twitter_handle = jobs.get('company', {}).get('twitter_handle', 'N/A')
            company_github = jobs.get('company', {}).get('github_url', 'N/A')
            location = jobs.get('location', 'N/A')

            job_types = []
            for type in jobs.get('types', []):
                job_types.append(type.get('name', 'N/A'))

            cities = []
            for city in jobs.get('cities', []):
                cities.append(city.get('name', 'N/A'))

            states = []
            for state in jobs.get('states', []):
                states.append(state.get('name', 'N/A'))

            countries = []
            for country in jobs.get('countries', []):
                countries.append(country.get('name', 'N/A'))

            regions = []
            for region in jobs.get('regions', []):
                regions.append(region.get('name', 'N/A'))

            has_remote = jobs.get('has_remote', False)
            published_at = jobs.get('published', 'N/A')
            job_description = jobs.get('description', 'N/A')
            experience_level = jobs.get('experience_level', 'N/A')
            application_url = jobs.get('application_url', 'N/A')
            language = jobs.get('language', [])
            min_salary = jobs.get('min_salary', 'N/A')
            max_salary = jobs.get('max_salary', 'N/A')
            salary_currency = jobs.get('currency', 'N/A')

            processed_data.append({
                'id': id,
                'title': title,
                'company': company_name,
                'location': location,
                'job_types': job_types,
                'company_website': company_website,
                'company_linkedin': company_linkedin,
                'company_twitter_handle': company_twitter_handle,
                'company_github': company_github,
                'regions': regions,
                'has_remote': has_remote,
                'published_at': published_at,
                'job_description': job_description,
                'experience_level': experience_level,
                'application_url': application_url,
                'language': language,
                'min_salary': min_salary,
                'max_salary': max_salary,
                'salary_currency': salary_currency
            })
            
        return processed_data
    
    def process_data_to_json_and_csv(self, input_path: str, output_dir: str):
        processor = APIDataProcessor()
    
        raw = Utils.load_json_data(input_path)
        processed = processor.process_api_data(raw)

        paths = {
            "json": f"{output_dir}/processed_api_data_jobdataapi.json",
            "csv": f"{output_dir}/processed_api_data_jobdataapi.csv"
        }

        Utils.save_json_data(processed, paths["json"])
        Utils.save_dataframe_to_csv(
            Utils.convert_json_to_dataframe(processed),
            paths["csv"]
        )

        print("API processing completed.")