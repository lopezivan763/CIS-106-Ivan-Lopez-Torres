# Test Assignment 12.

import test


def test_assignment_12_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 12",
        r"activity[ _]?#?\d\.(class|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_12_required_source_code_files():
    test.check_required_files("Assignment 12", "(cs|java|js|lua|py)", 2)


def test_assignment_12_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 12", "Activity 1", 1)


def test_assignment_12_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 12", "Activity 1", 1, 1, 1)


def test_assignment_12_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 12", "Activity 1")


def test_assignment_12_activity_1_source_code_file_contains():
    test.check_file_contains(
        "Assignment 12",
        "Activity 1",
        r"py",
        r"\.append",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_1_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 12",
        "Activity 1",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 12",
        "Activity 1",
        "",
        "1\n2\n-1\n",
        "(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting score.")


def test_assignment_12_activity_1_output():
    test.check_source_code_output(
        "Assignment 12",
        "Activity 1",
        "",
        "1\n2\n-1\n",
        r"1\.5.+?(average|mean)|(average|mean).+?1\.5",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 1",
        "",
        "1\n2\n-1\n",
        r"1.+?(low|minimum)|(low|minimum).+?1",
        "low output value or label is missing or incorrect. "
            "Expected low: 1. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 1",
        "",
        "1\n2\n-1\n",
        r"2.+?(high|maximum)|(high|maximum).+?2",
        "high output value or label is missing or incorrect. "
            "Expected high: 2. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 1",
        "",
        "1\n2\n-2\n",
        r"1\.5.+?(average|mean)|(average|mean).+?1\.5",
        "average calculation output is incorrect.")


def test_assignment_12_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 12", "Activity 2", 1)


def test_assignment_12_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 12", "Activity 2", 1, 1, 1)


def test_assignment_12_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 12", "Activity 2")


def test_assignment_12_activity_2_source_code_file_contains():
    test.check_file_contains(
        "Assignment 12",
        "Activity 2",
        r"py",
        r"\.append",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_2_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 12",
        "Activity 2",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_2_output():
    test.check_source_code_output(
        "Assignment 12",
        "Activity 2",
        "",
        "h\ne\n",
        r"75",
        "higher guess is incorrect.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 2",
        "",
        "h\ne\n",
        r"50,?\s75",
        "Guesses list is missing or incorrect."
            "Expected 50, 75.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 2",
        "",
        "l\ne\n",
        r"24|25",
        "lower guess is incorrect.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 2",
        "",
        "l\ne\n",
        r"50,?\s(24|25)",
        "Guesses list is missing or incorrect."
            "Expected 50, 25.")


def test_assignment_12_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 12", "Activity 3", 1)


def test_assignment_12_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 12", "Activity 3", 1, 1, 1)


def test_assignment_12_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 12", "Activity 3")


def test_assignment_12_activity_3_source_code_file_contains():
    test.check_file_contains(
        "Assignment 12",
        "Activity 3",
        r"py",
        r"\.append",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_3_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 12",
        "Activity 3",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must use dynamic arrays. Expected array.append.")


def test_assignment_12_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "1\n2\n-1\n",
        "(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting score.")


def test_assignment_12_activity_3_output():
    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "1\n2\n-1\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "1\n2\n-1\n",
        r"1.+?(low|minimum)|(low|minimum).+?1",
        "low output value or label is missing or incorrect. "
            "Expected low: 1. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "1\n2\n-1\n",
        r"2.+?(high|maximum)|(high|maximum).+?2",
        "high output value or label is missing or incorrect. "
            "Expected high: 2. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "1\n2\n-2\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 12",
        "Activity 3",
        "",
        "80\n90\n100\n-1\n",
        r"100.+?90.+?80.+?",
        "sort sequence is incorrect. "
            "Expected 100...90...80.")
