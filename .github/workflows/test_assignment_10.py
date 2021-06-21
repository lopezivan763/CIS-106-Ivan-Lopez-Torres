# Test Assignment 9.

import test


def test_assignment_10_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 10",
        r"(nested )?activity[ _]?#?\d\.(class|fprg|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_10_required_flowgorithm_files():
    test.check_required_files("Assignment 10", "fprg", 1)


def test_assignment_10_required_source_code_files():
    test.check_required_files("Assignment 10", "(cs|java|js|lua|py)", 2)


def test_assignment_10_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 10", "Activity 1", 1, "fprg")


def test_assignment_10_activity_1_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 10", "Activity 1", 1, 1, 1)


def test_assignment_10_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 10", "Activity 1", 1)


def test_assignment_10_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 10", "Activity 1", 1, 1, 1)


def test_assignment_10_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 10", "Activity 1")


def test_assignment_10_activity_1_output_negative_termination():
    test.check_source_code_output(
        "Assignment 10",
        "Activity 1",
        "",
        "1\n2\n3\n-1\n",
        r"2.+?average|average.+?2",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 1",
        "",
        "1\n2\n-1\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 1",
        "",
        "1\n2\n-2\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 1",
        "",
        "3\n0\n-1\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect. 0 is a valid input value.")


def test_assignment_10_activity_2_flowgorithm_comments():
    test.check_source_code_comments("Assignment 10", "Activity 2", 1, "fprg")


def test_assignment_10_activity_2_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 10", "Activity 2", 1, 1, 1)


def test_assignment_10_activity_2_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 10", "Activity 2", 1)


def test_assignment_10_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 10", "Activity 2", 1, 1, 1)


def test_assignment_10_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 10", "Activity 2")


def test_assignment_10_activity_2_output():
    test.check_source_code_output(
        "Assignment 10",
        "Activity 2",
        "",
        "h\ne\n",
        r"75",
        "higher guess is incorrect.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 2",
        "",
        "h\ne\n",
        r"2.+?guess|guess.+?2",
        "number of guesses output or label is missing or incorrect."
            "Expected 2 guesses.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 2",
        "",
        "l\ne\n",
        r"24|25",
        "lower guess is incorrect.")

    test.check_source_code_output(
        "Assignment 10",
        "Activity 2",
        "",
        "l\ne\n",
        r"2.+?guess|guess.+?2",
        "number of guesses output or label is missing or incorrect."
            "Expected 2 guesses.")


def test_assignment_10_activity_3_flowgorithm_comments():
    test.check_source_code_comments("Assignment 10", "Activity 3", 1, "fprg")


def test_assignment_10_activity_3_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 10", "Activity 3", 1, 1, 1)


def test_assignment_10_activity_3_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 10", "Activity 3", 1)


def test_assignment_10_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 10", "Activity 3", 1, 1, 1)


def test_assignment_10_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 10", "Activity 3")


def test_assignment_10_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 10", "Activity 3")


def test_assignment_10_activity_4_flowgorithm_comments():
    test.check_source_code_comments("Assignment 10", "Activity 4", 1, "fprg")


def test_assignment_10_activity_4_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 10", "Activity 4", 1, 1, 1)


def test_assignment_10_activity_4_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 10", "Activity 4", 1)


def test_assignment_10_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 10", "Activity 4", 1, 1, 1)


def test_assignment_10_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 10", "Activity 4")


def test_assignment_10_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 10", "Activity 4")


def test_assignment_10_nested_activity_1_flowgorithm_comments():
    test.check_source_code_comments(
        "Assignment 10", "Nested Activity 1", 1, "fprg")


def test_assignment_10_nested_activity_1_flowgorithm_functions():
    test.check_flowgorithm_functions(
        "Assignment 10", "Nested Activity 1", 1, 0, 1)


def test_assignment_10_nested_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_source_code_comments():
    test.check_source_code_comments(
        "Assignment 10", "Nested Activity 1", 1)


def test_assignment_10_nested_activity_1_source_code_functions():
    test.check_source_code_functions(
        "Assignment 10", "Nested Activity 1", 1, 0, 1)


def test_assignment_10_nested_activity_1_source_code_formatting():
    test.check_source_code_formatting(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting(
        "Assignment 10", "Nested Activity 1")


def test_assignment_10_nested_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "1\n3\n",
        r"(start|begin).+?\n.+?(stop|end)",
        "Input label(s) missing or incorrect. "
            "Expecting starting and ending.")


def test_assignment_10_nested_activity_1_output():
    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "1\n3\n",
        r"1\s+2\s+3\s*\n+.*?2\s+4\s+6\s*\n+.*?3\s+6\s+9",
        "output is incorrect. Check multiplication values.")

    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "1\n3\n",
        r"1\s+2\s+3\s*\n+.*?1\s+2\s+3\s*\n+.*?2\s+4\s+6\s*\n+.*?3\s+6\s+9",
        "output is incorrect. Check column headings.")

    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "1\n3\n",
        r"1\s+1\s+2\s+3\s*\n+2\s+2\s+4\s+6\s*\n+3\s+3\s+6\s+9",
        "output is incorrect. Check row headings.")

    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "3\n5\n",
        r"9\s+12\s+15\s*\n+.*?12\s+16\s+20\s*\n+.*?15\s+20\s+25",
        "output is incorrect. Check multiplication values.")

    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "3\n5\n",
        r"3\s+4\s+5\s*\n+.*?9\s+12\s+15\s*\n+.*?12\s+16\s+20\s*\n+.*?15\s+20\s+25",
        "output is incorrect. Check column headings.")

    test.check_source_code_output(
        "Assignment 10",
        "Nested Activity 1",
        "",
        "3\n5\n",
        r"3\s+9\s+12\s+15\s*\n+4\s+12\s+16\s+20\s*\n+5\s+15\s+20\s+25",
        "output is incorrect. Check row headings.")


def test_assignment_10_nested_activity_2_flowgorithm_comments():
    test.check_source_code_comments(
        "Assignment 10", "Nested Activity 2", 1, "fprg")


def test_assignment_10_nested_activity_2_flowgorithm_functions():
    test.check_flowgorithm_functions(
        "Assignment 10", "Nested Activity 2", 1, 1, 1)


def test_assignment_10_nested_activity_2_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_comments():
    test.check_source_code_comments(
        "Assignment 10", "Nested Activity 2", 1)


def test_assignment_10_nested_activity_2_source_code_functions():
    test.check_source_code_functions(
        "Assignment 10", "Nested Activity 2", 1, 1, 1)


def test_assignment_10_nested_activity_2_source_code_formatting():
    test.check_source_code_formatting(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting(
        "Assignment 10", "Nested Activity 2")


def test_assignment_10_nested_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting(
        "Assignment 10", "Nested Activity 2")
