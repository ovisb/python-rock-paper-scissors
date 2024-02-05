import pytest

from python_rock_paper_scissors.file_handler import FileHandler


@pytest.fixture
def test_file_object():
    file_name = "test_file.txt"
    with open(file_name, "w") as f:
        f.write("Ovi 50\n")

    return FileHandler(file_name)


def test_read_file(test_file_object):
    assert test_file_object.load() == {"Ovi": 50}


def test_file_not_found():
    file_handler = FileHandler("not_found.txt")
    with pytest.raises(FileNotFoundError):
        file_handler.load()


def test_save_file(test_file_object):
    d = test_file_object.load()
    d["test"] = 1
    test_file_object.save(d)
    assert test_file_object.load() == {"Ovi": 50, "test": 1}
