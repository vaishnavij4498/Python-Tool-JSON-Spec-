# yaml_spec_validator/
# ├── main.py
# ├── yaml_loader.py
# ├── validator.py
# ├── schema.json
# ├── test_validator.py
# └── README.md

# ---------------------------
# File: yaml_loader.py
import yaml
import json

def load_yaml(path):
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"YAML parsing error: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")


def load_json_schema(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON parsing error: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found: {path}")
