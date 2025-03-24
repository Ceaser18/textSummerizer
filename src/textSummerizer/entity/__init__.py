from dataclasses import dataclass
from pathlib import Path 
#input to data ingestion module
@dataclass 
class DataIngestionConfig:
    root_dir: Path 
    source_URL: Path 
    local_data_file: Path
    unzip_dir: Path


