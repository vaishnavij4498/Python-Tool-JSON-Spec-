# ---------------------------
# File: validator.py
from jsonschema import validate, ValidationError

class SpecValidator:
    def __init__(self, spec, schema=None):
        self.spec = spec
        self.schema = schema
        self.errors = []

    def validate(self):
        if self.schema:
            try:
                validate(instance=self.spec, schema=self.schema)
                return True
            except ValidationError as e:
                self.errors.append(str(e))
                return False
        else:
            # Fallback manual validation if schema not provided
            if 'registers' not in self.spec:
                self.errors.append("Missing 'registers' section.")
                return False

            for reg in self.spec['registers']:
                if 'name' not in reg:
                    self.errors.append("A register is missing the 'name' field.")
                if 'address' not in reg:
                    self.errors.append(f"Register {reg.get('name', '?')} missing 'address'.")
                if 'fields' not in reg:
                    self.errors.append(f"Register {reg.get('name', '?')} missing 'fields'.")
                else:
                    for field in reg['fields']:
                        if 'name' not in field:
                            self.errors.append(f"Field in register {reg.get('name', '?')} missing 'name'.")
                        if 'bit_offset' not in field or 'bit_width' not in field:
                            self.errors.append(f"Field {field.get('name', '?')} in register {reg.get('name', '?')} missing 'bit_offset' or 'bit_width'.")
            return not self.errors