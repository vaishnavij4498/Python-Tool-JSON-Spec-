# ---------------------------
# File: main.py
import argparse
from yaml_loader import load_yaml, load_json_schema
from validator import SpecValidator

def main():
    parser = argparse.ArgumentParser(description='Validate hardware spec YAML file.')
    parser.add_argument('file', help='Path to the YAML spec file')
    parser.add_argument('--schema', help='Path to optional JSON schema')
    args = parser.parse_args()

    try:
        spec = load_yaml(args.file)
        schema = load_json_schema(args.schema) if args.schema else None
        validator = SpecValidator(spec, schema)
        if validator.validate():
            print("Spec is valid.")
        else:
            print("Validation failed:")
            for err in validator.errors:
                print(f" - {err}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()