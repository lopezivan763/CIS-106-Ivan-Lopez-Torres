# Test Assignment 11.

import test


def test_assignment_11_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 11",
        r"(defined|fixed) activity[ _]?#?\d\.(class|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_11_required_source_code_files():
    test.check_required_files("Assignment 11", "(cs|java|js|lua|py)", 2)


def test_assignment_11_defined_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 11", "Defined Activity 1", 1)


def test_assignment_11_defined_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 11", "Defined Activity 1", 1, 1, 1)


def test_assignment_11_defined_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 11", "Defined Activity 1")


def test_assignment_11_defined_activity_1_source_code_file_contains():
    test.check_file_contains(
        "Assignment 11",
        "Defined Activity 1",
        r"(cs|java|js|lua|py)",
        "January.+?February.+?March",
        "must include defined array for month names.")

    test.check_file_contains(
        "Assignment 11",
        "Defined Activity 1",
        r"(cs|java|js|lua|py)",
        "31.+?(28|29).+?31",
        "must include defined array for month days.")


def test_assignment_11_defined_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2020\n1\n0\n0\n",
        "year.*?\n?.*?month",
        "Input label(s) missing or incorrect. "
            "Expecting year and month.")


def test_assignment_11_defined_activity_1_output():
    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2020\n2\n0\n0\n",
        r"February.+?29",
        "output is incorrect. Expected:\n"
            "February 2020 has 29 days")

    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2000\n2\n0\n0\n",
        r"February.+?29",
        "output is incorrect. Expected:\n"
            "February 2000 has 29 days")

    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2021\n2\n0\n0\n",
        r"February.+?28",
        "output is incorrect. Expected:\n"
            "February 2021 has 28 days")

    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2100\n2\n0\n0\n",
        r"February.+?28",
        "output is incorrect. Expected:\n"
            "February 2100 has 28 days")


    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2020\n1\n2020\n12\n2020\n0\n",
        r"January.+?31.+?December.+?31",
        "output is incorrect. Expected:\n"
            "January 2020 has 31 days..."
            "December 2020 has 31 days")


    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 1",
        "",
        "2020\n1\n2020\n12\n2020\n13\n",
        r"January.+?31.+?December.+?31",
        "output is incorrect. Expected:\n"
            "January 2020 has 31 days..."
            "December 2020 has 31 days")


def test_assignment_11_defined_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 11", "Activity 2", 1)


def test_assignment_11_defined_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 11", "Activity 2", 1, 1, 1)


def test_assignment_11_defined_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 11", "Activity 2")


def test_assignment_11_defined_activity_1_source_code_file_contains():
    test.check_file_contains(
        "Assignment 11",
        "Defined Activity 2",
        r"(cs|java|js|lua|py)",
        "Monday.+?Tuesday.+?Wednesday",
        "must include defined array for day names.")


def test_assignment_11_defined_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 2",
        "",
        "2020\n1\n1",
        "year.*?\n?.*?month.*?\n.*?day",
        "Input label(s) missing or incorrect. "
            "Expecting year, month, and day.")


def test_assignment_11_defined_activity_2_output():
    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 2",
        "",
        "2020\n1\n1",
        "Wednesday",
        "January 1, 2020 was a Wednesday.")

    test.check_source_code_output(
        "Assignment 11",
        "Defined Activity 2",
        "",
        "2020\n12\n31",
        "Thursday",
        "December 31, 2020 was a Thursday.")


def test_assignment_11_fixed_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 11", "Fixed Activity 1", 1)


def test_assignment_11_fixed_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 11", "Fixed Activity 1", 1, 1, 1)


def test_assignment_11_fixed_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 11", "Fixed Activity 1")


def test_assignment_11_fixed_activity_1_source_code_file_contains():
    test.check_file_contains(
        "Assignment 11",
        "Fixed Activity 1",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must include a fixed-length array. "
            "Expected array = [None] * length or "
            "array = [None] * count.")


def test_assignment_11_fixed_activity_1_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 11",
        "Fixed Activity 1",
        r"py",
        r"\.append",
        "must use fixed length arrays. "
            "Save .append for dynamic array activities (Assignment 12).")


def test_assignment_11_fixed_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "3\n1\n2\n3\n",
        "(grades|scores).*?\n?.*?(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting scores and score.")


def test_assignment_11_fixed_activity_1_output():
    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "3\n1\n2\n3\n",
        r"2",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "2\n1\n2\n",
        r"1\.5",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "2\n1\n2\n",
        r"1\.5.+?(average|mean)|(average|mean).+?1\.5",
        "average output label is missing or incorrect. "
            "Expected average. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "2\n1\n2\n",
        r"1.+?(low|minimum)|(low|minimum).+?1",
        "low output value or label is missing or incorrect. "
            "Expected low: 1. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 1",
        "",
        "2\n1\n2\n",
        r"2.+?(high|maximum)|(high|maximum).+?2",
        "low output value or label is missing or incorrect. "
            "Expected high: 2. "
            "Include output label on same line as result.")


def test_assignment_11_fixed_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 11", "Fixed Activity 2", 1)


def test_assignment_11_fixed_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 11", "Fixed Activity 2", 1, 1, 1)


def test_assignment_11_fixed_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 11", "Fixed Activity 2")


def test_assignment_11_fixed_activity_2_source_code_file_contains():
    test.check_file_contains(
        "Assignment 11",
        "Fixed Activity 2",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must include a fixed-length array. "
            "Expected array = [None] * length or "
            "array = [None] * count.")


def test_assignment_11_fixed_activity_2_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 11",
        "Fixed Activity 2",
        r"py",
        r"\.append",
        "must use fixed length arrays. "
            "Save .append for dynamic array activities (Assignment 12).")


def test_assignment_11_fixed_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 11", "Fixed Activity 3", 1)


def test_assignment_11_fixed_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 11", "Fixed Activity 3", 1, 1, 1)


def test_assignment_11_fixed_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 11", "Fixed Activity 3")


def test_assignment_11_fixed_activity_3_source_code_file_contains():
    test.check_file_contains(
        "Assignment 11",
        "Fixed Activity 3",
        r"py",
        r"\[(None|0)\] \* .+?\n",
        "must include a fixed-length array. "
            "Expected array = [None] * length or "
            "array = [None] * count.")

    test.check_file_contains(
        "Assignment 11",
        "Fixed Activity 3",
        r"py",
        r"sort",
        "must include sorting. "
            "Expected array.sort.")


def test_assignment_11_fixed_activity_3_source_code_file_does_not_contain():
    test.check_file_does_not_contain(
        "Assignment 11",
        "Fixed Activity 3",
        r"py",
        r"\.append",
        "must use fixed length arrays. "
            "Save .append for dynamic array activities (Assignment 12).")


def test_assignment_11_fixed_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 3",
        "",
        "3\n1\n2\n3\n",
        "(grades|scores).*?\n?.*?(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting scores and score.")


def test_assignment_11_fixed_activity_3_output():
    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 3",
        "",
        "3\n1\n2\n3\n",
        r"2",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 3",
        "",
        "2\n1\n2\n",
        r"1\.5",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 3",
        "",
        "2\n1\n2\n",
        r"1\.5.+?average|average.+?1\.5",
        "average output label is missing or incorrect. "
            "Expected average. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 11",
        "Fixed Activity 3",
        "",
        "3\n80\n90\n100\n",
        r"100.+?90.+?80",
        "sort sequence is incorrect. "
            "Expected 100...90...80.")
