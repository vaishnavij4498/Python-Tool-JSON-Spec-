# ---------------------------
# File: main.py
import argparse
from yaml_loader import load_yaml, load_json_schema
from validator import SpecValidator
from doc_generator import generate_html

def main():
    parser = argparse.ArgumentParser(description='Validate hardware spec YAML file.')
    parser.add_argument('file', help='Path to the YAML spec file')
    parser.add_argument('--schema', help='Path to optional JSON schema')
    parser.add_argument('--html', action='store_true', help='Generate HTML documentation')
    args = parser.parse_args()

    try:
        spec = load_yaml(args.file)
        schema = load_json_schema(args.schema) if args.schema else None
        validator = SpecValidator(spec, schema)
        if validator.validate():
            print("Spec is valid.")
            if args.html:
                generate_html(spec)

        else:
            print("Validation failed:")
            for err in validator.errors:
                print(f" - {err}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()