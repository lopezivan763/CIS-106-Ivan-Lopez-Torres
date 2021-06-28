# Test Assignment 13.

import test


def test_assignment_13_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 13",
        r"activity[ _]?#?\d\.(class|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_13_required_source_code_files():
    test.check_required_files("Assignment 13", "(cs|java|js|lua|py)", 2)


def test_assignment_13_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 13", "Activity 1", 1)


def test_assignment_13_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 13", "Activity 1", 1, 1, 1)


def test_assignment_13_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 13", "Activity 1")


def test_assignment_13_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "Firstname Lastname\n",
        "name",
        "Input label(s) missing or incorrect. "
            "Expecting name.")


def test_assignment_13_activity_1_output():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "Firstname Lastname\n",
        r"Lastname, F.\n",
        "Output is incorrect. Expected 'Lastname, F.'")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "   Firstname   Lastname   \n",
        r"Lastname, F.\n",
        "Output is incorrect. Expected 'Lastname, F.' "
            "Remove leading, trailing, and extra spaces.")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "   Firstname   Middle   Lastname   \nFirstname Lastname\n",
        r"name",
        "Output is incorrect. Expected program to work with three name parts")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "Firstname\nFirstname Lastname\n",
        r"name",
        "Output is incorrect. Expected program to work with one name part")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "   Firstname   \nFirstname Lastname\n",
        r"name",
        "Output is incorrect. Expected program to work with one name part")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "\nFirstname Lastname\n",
        r"name",
        "Output is incorrect. Expected program to work with no name part")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 1",
        "",
        "   \nFirstname Lastname\n",
        r"name",
        "Output is incorrect. Expected program to work with blank name")


def test_assignment_13_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 13", "Activity 2", 1)


def test_assignment_13_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 13", "Activity 2", 1, 1, 1)


def test_assignment_13_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 13", "Activity 2")


def test_assignment_13_activity_2_output():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 2",
        "",
        "this is a test\n",
        r"tset a si siht",
        "Output is incorrect. Expected 'tset a si siht'")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 2",
        "",
        "  the  cat  in  the  hat  ",
        r"tah eht ni tac eht\n",
        "Output is incorrect. Expected 'tah eht ni tac eht'. "
            "Check leading, trailing, and extra spaces.")


def test_assignment_13_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 13", "Activity 3", 1)


def test_assignment_13_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 13", "Activity 3", 1, 1, 1)


def test_assignment_13_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 13", "Activity 3")


def test_assignment_13_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 3",
        "",
        "test\n",
        "enter",
        "Input label(s) missing or incorrect. "
            "Expecting 'Enter'")


def test_assignment_13_activity_3_output():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 3",
        "",
        "this,is,a,test\n",
        "this\nis\na\ntest",
        "Output is incorrect. Expecting:\nthis\nis\na\ntest")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 3",
        "",
        "this is, another test\n",
        "this is\nanother test",
        "Output is incorrect. Expecting:\nthis is\nanother test")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 3",
        "",
        "  this  ,  is  ,  a  ,  ,  third  ,  test  \n",
        "this\nis\na\n\nthird\ntest|this\nis\na\nthird\ntest",
        "Output is incorrect. Expecting:\nthis\nis\na\ntest")


def test_assignment_13_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 13", "Activity 4", 1)


def test_assignment_13_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 13", "Activity 4", 1, 1, 1)


def test_assignment_13_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 13", "Activity 4")


def test_assignment_13_activity_4_input_labels():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 4",
        "",
        "Repeat this.\n20\n2\nleft\n",
        "Enter.+?characters.+?lines.+?(direction|right|left)",
        "Input label(s) missing or incorrect. "
            "Expecting Enter...characters...lines...direction (left or right)")


def test_assignment_13_activity_4_output():
    test.check_source_code_output(
        "Assignment 13",
        "Activity 4",
        "",
        "Repeat this.\n20\n2\nleft\n",
        "Repeat this. Repeat \nepeat this. Repeat t",
        "Output is incorrect. Expecting:\n"
            "Repeat this. Repeat \nepeat this. Repeat t")

    test.check_source_code_output(
        "Assignment 13",
        "Activity 4",
        "",
        "Repeat this.\n20\n2\nright\n",
        "Repeat this. Repeat \n Repeat this. Repeat",
        "Output is incorrect. Expecting:\n"
            "Repeat this. Repeat \n Repeat this. Repeat")
