# ---------------------------
# File: README.md
# YAML Spec Validator

A simple Python-based tool to validate machine-readable YAML specifications for hardware IP registers.

## Features
- Supports YAML input with optional JSON Schema validation
- Modular OOP structure
- Clear error reporting and CLI usage

## Usage
```bash
python main.py path/to/spec.yaml
python main.py path/to/spec.yaml --schema schema.json
```

## Run Tests
```bash
pytest test_validator.py
```

## Example YAML
```yaml
ip_name: Timer
registers:
  - name: CTRL
    address: 0x00
    description: Control register
    fields:
      - name: ENABLE
        bit_offset: 0
        bit_width: 1
      - name: MODE
        bit_offset: 1
        bit_width: 2
```

## License
MIT
