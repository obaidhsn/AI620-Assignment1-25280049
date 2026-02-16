import kagglehub
import shutil
from pathlib import Path


class PublicDatasetExtractor:
    def __init__(self):
        pass

    def download_dataset_from_kaggle(self, dataset_path: str, file_to_download: str, output_dir: str = None):
        cached_path = kagglehub.dataset_download(dataset_path)

        if output_dir:
            if not Path(output_dir).exists():
                Path(output_dir).mkdir(parents=True, exist_ok=True)
                
            output_dir = Path(output_dir)
            for item in Path(cached_path).iterdir():
                if item.name == file_to_download:
                    dest = output_dir / item.name

                    if item.is_dir():
                        shutil.copytree(item, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, dest)

                    print("Dataset copied to project directory:", output_dir)
                    return dest
        return cached_path
