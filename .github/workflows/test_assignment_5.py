# Test Assignment 5.

import test


def test_assignment_5_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 5",
        r"activity[ _]?#?\d\.(class|fprg|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_5_required_flowgorithm_files():
    test.check_required_files("Assignment 5", "fprg", 1)


def test_assignment_5_required_source_code_files():
    test.check_required_files("Assignment 5", "(cs|java|js|lua|py)", 2)


def test_assignment_5_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 1", 1, "fprg")


def test_assignment_5_activity_1_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 1", 2, 3, 1)


def test_assignment_5_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 1", 1)


def test_assignment_5_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 1", 2, 3, 1)


def test_assignment_5_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 1")


def test_assignment_5_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        "hours.*?\n?.*?(rate|per hour|hourly)",
        "Input label(s) missing or incorrect. "
            "Expecting hours and rate.")


def test_assignment_5_activity_1_weekly_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        "150",
        "weekly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "162.75",
        "weekly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        r"week.+?150|150.+?week",
        "weekly output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_1_monthly_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        "600|650",
        "monthly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "651|705.25",
        "monthly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        r"month.+?6|6.+?month",
        "monthly output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_1_yearly_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        "7800",
        "yearly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "8463",
        "yearly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 1",
        "",
        "10\n15\n",
        r"year.+?7800|7800.+?year|annual.+?7800|7800.+?annual",
        "yearly output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_2_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 2", 1, "fprg")


def test_assignment_5_activity_2_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 2", 1, 4, 1)


def test_assignment_5_activity_2_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 2", 1)


def test_assignment_5_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 2", 1, 4, 1)


def test_assignment_5_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 2")


def test_assignment_5_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "age|years",
        "Input label(s) missing or incorrect. Expecting years.")


def test_assignment_5_activity_2_months_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "12",
        "months calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "month.+?12|12.+?month",
        "months output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_2_days_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "365",
        "days calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "day.+?365|365.+?day",
        "days output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_2_hours_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "8760",
        "hours calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "hour.+?8760|8760.+?hour",
        "hours output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_2_seconds_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "31536000|3.1536E7",
        "seconds calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 2",
        "",
        "1\n",
        "seconds.+?31536000|31536000.+?seconds|"
            "seconds.+?3.1536E7|3.1536E7.+?seconds",
        "seconds output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_2_minutes_output():
    test.check_file_does_not_contain(
        "Assignment 5",
        "Activity 2",
        r"(cs|java|js|lua|py)",
        "minute",
        "processing error. Processing should not include minutes.")


def test_assignment_5_activity_3_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 3", 1, "fprg")


def test_assignment_5_activity_3_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 3", 1, 3, 1)


def test_assignment_5_activity_3_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 3", 1)


def test_assignment_5_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 3", 1, 3, 1)


def test_assignment_5_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 3")


def test_assignment_5_activity_3_source_code_file_contains():
    test.check_file_contains(
        "Assignment 5",
        "Activity 3",
        r"(cs|java|js|lua|py)",
        "feet|meter",
        "must include output labels with either feet or meters.")


def test_assignment_5_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "",
        "1\n",
        "mile",
        "input label(s) missing or incorrect. Expecting miles.")


def test_assignment_5_activity_3_yards_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        "1760",
        "yards calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        r"yard.+?1760|1760.+?yard",
        "yards output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_3_feet_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        "5280",
        "feet calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        r"feet.+?5280|5280.+?feet",
        "feet output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_3_inches_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        r"63360",
        "inches calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "feet",
        "1\n",
        r"inches.+?63360|63360.+?inches",
        "inches output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_3_kilometers_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        "1.6",
        "kilometers calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        r"kilometer.+?1\.6|1\.6.+?kilometer",
        "kilometers output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_3_meters_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{2}",
        "meters calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        r"meter.+?16\d{2}|16\d{2}.+?meter",
        "mneters output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_3_centimeters_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{4}",
        "centimeters calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 3",
        "meter",
        "1\n",
        r"centimeter.+?16\d{4}|16\d{4}.+?centimeter",
        "centimeters output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 4", 1, "fprg")


def test_assignment_5_activity_4_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 4", 2, 2, 1)


def test_assignment_5_activity_4_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 4", 1)


def test_assignment_5_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 4", 2, 2, 1)


def test_assignment_5_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 4")


def test_assignment_5_activity_4_source_code_file_contains():
    test.check_file_contains(
        "Assignment 5",
        "Activity 4",
        r"(cs|java|js|lua|py)",
        "triangle|rectangle|trapezoid|ellipse|"
            "square|parallelogram|circle|sector",
        "must indicate shape type.")


def test_assignment_5_activity_4_triangle_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_5_activity_4_triangle_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "triangle area calculation output is incorrect. "
            "Expected 0.5")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "triangle.+?area.+?0.5|area.+?triangle.+?0.5|"
            "0.5.+?triangle.+?0.5.+?area|area.+?triangle",
        "triangle output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_rectangle_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"width.*?\n?.*?height|length.*?\n?.*?width",
        "input label(s) missing or incorrect. "
            "Expecting width and height.")


def test_assignment_5_activity_4_rectangle_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "rectangle area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "rectangle.+?area.+?1|area.+?rectangle.+?1|"
            "1.+?rectangle.+?1.+?area|area.+?rectangle",
        "rectangle output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_trapezoid_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "trapezoid area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "trapezoid.+?area.+?1|area.+?trapezoid.+?1|"
            "1.+?trapezoid.+?1.+?area|area.+?trapezoid",
        "trapezoid output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_ellipse_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "ellipse area calculation output is incorrect. "
            "Expected 3.14")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "ellipse.+?area.+?3.14|area.+?ellipse.+?3.14|"
            "3.14.+?ellipse.+?3.14.+?area|area.+?ellipse",
        "ellipse output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_square_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "side|base|height|length|width",
        "input label(s) missing or incorrect. "
            "Expecting side.")


def test_assignment_5_activity_4_square_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "square area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "square.+?area.+?1|area.+?square.+?1|"
            "1.+?square.+?1.+?area|area.+?square",
        "square output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_parallelogram_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_5_activity_4_parallelogram_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1",
        "parallelogram area calculation output is incorrect. "
            "Expected 1")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "parallelogram.+?area.+?1|area.+?parallelogram.+?1|"
            "1.+?parallelogram.+?1.+?area|area.+?parallelogram",
        "parallelogram output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_circle_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_5_activity_4_circle_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "circle area calculation output is incorrect. "
            "Expected 3.14")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "circle.+?area.+?3.14|area.+?circle.+?3.14|"
            "3.14.+?circle.+?3.14.+?area|area.+?circle",
        "circle output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_4_sector_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_5_activity_4_sector_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "sector area calculation output is incorrect. "
            "Expected 0.5")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "sector.+?area.+?0.5|area.+?sector.+?0.5|"
            "0.5.+?sector.+?0.5.+?area|area.+?sector",
        "sector output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_5_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 5", 1, "fprg")


def test_assignment_5_activity_5_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 5", 2, 1, 1)


def test_assignment_5_activity_5_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 5", 1)


def test_assignment_5_activity_5_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 5", 2, 1, 1)


def test_assignment_5_activity_5_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 5")


def test_assignment_5_activity_5_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 5",
        "",
        "10\n10\n",
        "length.*?\n?.*?width|long.*?\n?.*?wide",
        "input label(s) missing or incorrect. "
            "Expecting length and width.")


def test_assignment_5_activity_5_area_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 5",
        "",
        "12\n10\n",
        r"13\.33",
        "area calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 5",
        "",
        "12.5\n10.5\n",
        "14.58",
        "area calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 5",
        "",
        "10\n10\n",
        r"(area|yards).+?11\.11|11\.11.+?(yards|area)",
        "area output label is missing or incorrect. "
            "Expecting yards. "
            "Include output label on same line as result.")


def test_assignment_5_activity_6_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 6", 1, "fprg")


def test_assignment_5_activity_6_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 6", 5, 3, 1)


def test_assignment_5_activity_6_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 6", 1)


def test_assignment_5_activity_6_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 6", 5, 3, 1)


def test_assignment_5_activity_6_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 6")


def test_assignment_5_activity_6_gallons_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "2",
        "gallons calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "gallon.+?2|2.+?gallon",
        "gallons output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_6_cost_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        "60",
        "cost calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 6",
        "",
        "10\n10\n8\n30\n300\n",
        r"(cost|price).+?60|60.+?(price|cost)",
        "cost output label is missing or incorrect. "
            "Include output label on same line as result.")


def test_assignment_5_activity_7_flowgorithm_comments():
    test.check_source_code_comments("Assignment 5", "Activity 7", 1, "fprg")


def test_assignment_5_activity_7_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 5", "Activity 7", 2, 1, 1)


def test_assignment_5_activity_7_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_comments():
    test.check_source_code_comments("Assignment 5", "Activity 7", 1)


def test_assignment_5_activity_7_source_code_formatting():
    test.check_source_code_formatting("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_functions():
    test.check_source_code_functions("Assignment 5", "Activity 7", 2, 1, 1)


def test_assignment_5_activity_7_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 5", "Activity 7")


def test_assignment_5_activity_7_input_labels():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 7",
        "",
        "Rover\n2\n",
        "name.*?\n?.*?(age|years|old)",
        "input label(s) missing or incorrect. "
            "Expecting name and age.")


def test_assignment_5_activity_7_age_output():
    test.check_source_code_output(
        "Assignment 5",
        "Activity 7",
        "",
        "Rover\n2\n",
        "14",
        "age calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 7",
        "",
        "Rover\n2\n",
        "Rover.+?14|14.+?Rover",
        "name label output is missing or incorrect.")

    test.check_source_code_output(
        "Assignment 5",
        "Activity 7",
        "",
        "Rover\n2\n",
        "year.+?14|14.+?year",
        "age output label is missing or incorrect. "
            "Expected years. "
            "Include output label on same line as result.")
