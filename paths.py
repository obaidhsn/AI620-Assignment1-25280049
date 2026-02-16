from enum import Enum
from pathlib import Path

class FilePaths(Enum):
    RAW_DATA_DIR = "data/raw"
    PROCESSED_DATA_DIR = "data/processed"
    CLEANED_DATA_DIR = "data/cleaned"

for path in FilePaths:
    Path(path.value).mkdir(parents=True, exist_ok=True)
