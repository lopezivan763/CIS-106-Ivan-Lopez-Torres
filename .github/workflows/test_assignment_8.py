# Test Assignment 8.

import test


def test_assignment_8_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 8",
        r"(nested )?activity[ _]?#?\d\.(class|fprg|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_8_required_flowgorithm_files():
    test.check_required_files("Assignment 8", "fprg", 1)


def test_assignment_8_required_source_code_files():
    test.check_required_files("Assignment 8", "(cs|java|js|lua|py)", 2)


def test_assignment_8_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 8", "Activity 1", 1, "fprg")


def test_assignment_8_activity_1_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 8", "Activity 1", 1, 1, 1)


def test_assignment_8_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 1", 1)


def test_assignment_8_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 1", 1, 1, 1)


def test_assignment_8_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 1")


def test_assignment_8_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "1\n3\n",
        "(value|number).*?\n?.*?(expression|times)",
        "Input label(s) missing or incorrect. "
            "Expecting value and expressions.")


def test_assignment_8_activity_1_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "1\n3\n",
        r"1 \* 1 = 1\n1 \* 2 = 2\n1 \* 3 = 3",
        "output is incorrect. Expected:\n"
            "1 * 1 = 1\n1 * 2 = 2\n1 * 3 = 3")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 1",
        "",
        "3\n5\n",
        r"3 \* 1 = 3\n3 \* 2 = 6\n3 \* 3 = 9\n3 \* 4 = 12\n3 \* 5 = 15",
        "output is incorrect. Expected:\n"
            "3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15")


def test_assignment_8_activity_2_flowgorithm_comments():
    test.check_source_code_comments("Assignment 8", "Activity 2", 1, "fprg")


def test_assignment_8_activity_2_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 8", "Activity 2", 1, 1, 1)


def test_assignment_8_activity_2_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 2", 1)


def test_assignment_8_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 2", 1, 1, 1)


def test_assignment_8_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 2")


def test_assignment_8_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "3\n1\n2\n3\n",
        "(grades|scores).*?\n?.*?(grade|score)",
        "Input label(s) missing or incorrect. "
            "Expecting scores and score.")


def test_assignment_8_activity_2_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "3\n1\n2\n3\n",
        r"2",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "2\n1\n2\n",
        r"1\.5",
        "average is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 2",
        "",
        "2\n1\n2\n",
        r"1\.5.+?average|average.+?1\.5",
        "average output label is missing or incorrect."
            "Expected average. "
            "Include output label on same line as result.")


def test_assignment_8_activity_3_flowgorithm_comments():
    test.check_source_code_comments("Assignment 8", "Activity 3", 1, "fprg")


def test_assignment_8_activity_3_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 8", "Activity 3", 1, 1, 1)


def test_assignment_8_activity_3_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 8", "Activity 3", 1)


def test_assignment_8_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 8", "Activity 3", 1, 1, 1)


def test_assignment_8_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 8", "Activity 3")


def test_assignment_8_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "1\n",
        "number|times|iterations",
        "Input label(s) missing or incorrect. "
            "Expecting number.")


def test_assignment_8_activity_3_output():
    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "1\n",
        r"3",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "2\n",
        r"3\.16",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "3\n",
        r"3\.13",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "4\n",
        r"3\.14",
        "output calculation is incorrect.")

    test.check_source_code_output(
        "Assignment 8",
        "Activity 3",
        "",
        "4\n",
        r"3\.14.+?pi|pi.+?3\.14",
        "(Pi output label is missing or incorrect. "
            "Expected pi. "
            "Include output label on same line as result.")
