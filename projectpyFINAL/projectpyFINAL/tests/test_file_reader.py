import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from project.base_reader import CustomObject
from project.advanced_reader import ExtendedCustomObject

@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello\nworld\n")
    return str(file)

def test_filename_property(sample_file):
    reader = CustomObject(sample_file)
    assert reader.filename.endswith("sample.txt")

def test_file_extension():
    assert CustomObject.file_extension("note.txt") == "txt"

def test_str_output(sample_file, capsys):
    reader = CustomObject(sample_file)
    print(reader)
    out, _ = capsys.readouterr()
    assert "<CustomObject:" in out

def test_add_operator(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("first")
    f2.write_text("second")
    reader1 = ExtendedCustomObject(str(f1))
    reader2 = ExtendedCustomObject(str(f2))
    merged = reader1 + reader2
    with open(merged.filename) as f:
        content = f.read()
    assert "first" in content and "second" in content

def test_concatenate(tmp_path):
    f1 = tmp_path / "1.txt"
    f2 = tmp_path / "2.txt"
    f3 = tmp_path / "3.txt"
    f1.write_text("one")
    f2.write_text("two")
    f3.write_text("three")
    reader = ExtendedCustomObject(str(f1))
    result = reader.concatenate(
        ExtendedCustomObject(str(f2)),
        ExtendedCustomObject(str(f3)),
        output_filename=str(tmp_path / "result.txt")
    )
    with open(result.filename) as f:
        content = f.read()
    assert "one" in content and "two" in content and "three" in content