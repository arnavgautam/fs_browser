from os import mkdir
from shutil import rmtree
from pathlib import Path
import pytest

from .fs_browser import FileSystemInformation, app

@pytest.fixture(autouse=True)
def beforeAndAfterEach():
    # Before each test
    mkdir(".temp")
    mkdir(".temp/nested")
    mkdir(".temp/nested/doubly_nested")
    mkdir(".temp/other_nested")
    with open(".temp/file.txt", 'w') as f:
        f.write("Hello world!")
        f.close()

    # Each test runs now
    yield

    # After the test
    rmtree(".temp")


def test_basic_init():
    with app.app_context():
        fsi = FileSystemInformation(".")
        assert Path(".").resolve() == fsi.home_dir

def test_init():
    with app.app_context():
        fsi = FileSystemInformation(".temp/nested")
        assert Path(".temp/nested").resolve() == fsi.home_dir

def test_valid_get():
    with app.app_context():
        fsi = FileSystemInformation(".temp/nested")
        fsi.get("doubly_nested")

def test_outside_get():
    with app.app_context():
        fsi = FileSystemInformation("./.temp/nested")
        with pytest.raises(ValueError) as err_info:
            fsi.get("../other_nested")
        assert "is not within the permitted area" in str(err_info.value)

def test_nonexistent_get():
    with app.app_context():
        fsi = FileSystemInformation("./.temp/nested")
        with pytest.raises(ValueError) as err_info:
            fsi.get("../yet_other_nested")
        assert "is invalid" in str(err_info.value)

def test_file_get():
    with app.app_context():
        fsi = FileSystemInformation(".temp")
        assert "Hello world!" in fsi.get("file.txt").json