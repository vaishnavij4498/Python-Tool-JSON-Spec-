# ---------------------------
# File: test_validator.py
import pytest
from validator import SpecValidator


def test_valid_spec():
    spec = {
        "registers": [
            {
                "name": "CTRL",
                "address": 0,
                "fields": [
                    {"name": "ENABLE", "bit_offset": 0, "bit_width": 1},
                    {"name": "MODE", "bit_offset": 1, "bit_width": 2}
                ]
            }
        ]
    }
    v = SpecValidator(spec)
    assert v.validate() == True
    assert len(v.errors) == 0


def test_missing_fields():
    spec = {"registers": [{"name": "CTRL"}]}
    v = SpecValidator(spec)
    assert not v.validate()
    assert any("missing 'address'" in e.lower() for e in v.errors)