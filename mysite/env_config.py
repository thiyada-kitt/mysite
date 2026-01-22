"""
Environment-based settings configuration
"""

import os
from pathlib import Path

def load_env_file(env_file):
    """Load environment variables from file"""
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent

# Try to load .env file (development)
load_env_file(BASE_DIR / '.env')

def get_env_bool(key, default=False):
    """Convert environment variable to boolean"""
    value = os.environ.get(key, str(default)).lower()
    return value in ('true', '1', 'yes', 'on')

def get_env_list(key, default=None):
    """Convert environment variable to list"""
    value = os.environ.get(key, '')
    if value:
        return [item.strip() for item in value.split(',') if item.strip()]
    return default or []