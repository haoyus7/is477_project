"""
Utility functions for the data pipeline.
Shared helper functions used across all scripts.
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def sha256_checksum(filepath):
    """Calculate SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def save_metadata(csv_path, info):
    """Save metadata JSON file next to the CSV."""
    csv_path = Path(csv_path)
    info['file_size_bytes'] = csv_path.stat().st_size
    info['sha256'] = sha256_checksum(csv_path)
    info['retrieved_at_utc'] = datetime.now(timezone.utc).isoformat()
    
    json_path = csv_path.with_name(csv_path.stem + '_metadata.json')
    json_path.write_text(json.dumps(info, indent=2))
    print(f"Metadata saved: {json_path}")
    return json_path


def create_session():
    """Create HTTP session with retry logic."""
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    session.mount('https://', HTTPAdapter(max_retries=retry))
    return session


def load_config(config_path="config.yaml"):
    """Load configuration from YAML file."""
    import yaml
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def ensure_directories(config):
    """Create necessary directories if they don't exist."""
    for dir_name, dir_path in config['directories'].items():
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"Directory ready: {dir_path}")
