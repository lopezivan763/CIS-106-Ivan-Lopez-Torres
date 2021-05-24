# Test Assignment 1.

import test


def test_assignment_1_folder_structure():
    test.check_assignment_folder_structure(
        assignment="Assignment 1",
        pattern=r"activity[ _]?1\.txt|package-lock.json",
        required=True)


def test_assignment_1_required_pseudocode_files():
    test.check_required_files("Assignment 1", "txt", 1)


def test_assignment_1_activity_1_code():
    assignment = "Assignment 1"
    activity = "Activity 1"

    path = test.get_path(assignment)
    assert path, f"Could not find folder named \"{assignment}\"."

    filename = test.get_filename(path, activity + r"\.txt")
    assert filename, \
        f"Could not find file named \"{assignment}\\{activity}.txt\"."

    text = test.read_file(path, filename)

    lines = text.split("\n")
    assert len(lines) >= 10, \
        f"{filename} lacks detail. Include more steps " \
        "to describe the preparation process."

    words = text.split()
    assert len(words) >= 100, \
        f"{filename} lacks detail. Include more words " \
        "to describe the preparation process. " \
        f"Expecting 100+ words, found {len(words)}."
