# Test README.md.

import os
import re

import test


def test_overall_folder_structure():
    test.check_overall_folder_structure(
        pattern=r"(assignment( *|_)\d+)|(final( *|_)project)|"
            r"node_modules|(\..*)")


def test_overall_file_structure():
    test.check_overall_file_structure(
        pattern=r"readme.md|package-lock.json|\..*")


def test_readme_exists():
    path = os.path.join(os.getcwd(), "README.md")
    if not os.path.isfile(path):
        assert False, "Could not find file named \"README.md\"."


def test_readme_heading():
    path = os.getcwd()
    filename = "README.md"
    text = test.read_file(path, filename)
    assert text, "Could not find file named \"README.md\"."

    pattern = r"# cis[ \-]*106[ \-]\w+[ \-]\w+"
    regex = re.compile(pattern, re.IGNORECASE)
    match = regex.search(text)
    assert match, "README.md missing required # CIS 106 Your Name heading."


def test_readme_check_spelling():
    path = os.getcwd()
    filename = "README.md"
    text = test.read_file(path, filename)
    if not text:
        return

    words = [
        "aasignment",
        "achivied",
        "acitivity",
        "acivities",
        "activitys",
        "activty",
        "activtys",
        "acuraretly",
        "alsp",
        "answeres",
        "asignment",
        "asociated",
        "assesments",
        "assigment",
        "assigmnents",
        "assignement",
        "assignemt",
        "assignent",
        "assignmet",
        "assignmetns",
        "assignmnent",
        "assingment",
        "atractive",
        "blunty",
        "bumby",
        "calculuations",
        "catagory",
        "catergorize",
        "certian",
        "cetain",
        "challening",
        "cheifly",
        "codeing",
        "comepletely",
        "comfusing",
        "comlexion",
        "comlpex",
        "compabtle",
        "completeing",
        "confusedo",
        "conist",
        "convertage",
        "convience",
        "countign",
        "createing",
        "desireable",
        "difficuly",
        "diffiuclt",
        "dodn",
        "eaisly",
        "easen",
        "emchanics",
        "encontered",
        "estabilished",
        "excersise",
        "experessions",
        "experiece",
        "familirize",
        "finially",
        "flogorithm",
        "florgorithim",
        "flowgarithm",
        "flowgorithim",
        "flowgoritm",
        "flowgorthim",
        "floworithm",
        "formant",
        "formating",
        "frusterated",
        "frusterating",
        "fuction",
        "funciton",
        "funtion",
        "futire",
        "futrue",
        "gdbonline",
        "generateing",
        "genral",
        "genrate",
        "genrated",
        "getage",
        "hnady",
        "hving",
        "implent",
        "inculding",
        "interger",
        "intergers",
        "intergrate",
        "invloved",
        "involed",
        "involoved",
        "itteration",
        "knowldge",
        "ladtly",
        "maight",
        "makign",
        "managable",
        "manuever",
        "mispell",
        "multipled",
        "multiplys",
        "mutiply",
        "mutliple",
        "nalikantha",
        "neccessity",
        "notcie",
        "orgranize",
        "othethr",
        "ouput",
        "outpur",
        "parallellogram",
        "pleasently",
        "pogram",
        "possibiltys",
        "possiblities",
        "possiblitys",
        "practive",
        "preciesly",
        "prgramming",
        "proffessor",
        "progams",
        "promated",
        "psuedocode",
        "qithboth",
        "referrence",
        "repition",
        "repititon",
        "reuseing",
        "rewmove",
        "scenerios",
        "sesion",
        "simalar",
        "similer",
        "simliler",
        "simplier",
        "slopply",
        "spaceing",
        "sperate",
        "statments",
        "stratch",
        "strenghtened",
        "strtch",
        "stucture",
        "suppsoed",
        "syas",
        "taks",
        "tiemframe",
        "tnight",
        "trimexcess",
        "tryingt",
        "usefullness",
        "utlized",
        "veriety",
        "versitility",
        "voculabory",
        "wasy",
        "wern",
        "whatin",
        "whille",
        "writeing"
    ]

    pattern = "|".join(words)
    matches = re.findall(pattern, text, re.IGNORECASE)
    matches = sorted(list(set(matches)))
    if len(matches) > 0:
        assert False, \
            "README.md check spelling. " \
            f"Found:\n{matches}"


def test_readme_capitalize_proper_nouns():
    path = os.getcwd()
    filename = "README.md"
    text = test.read_file(path, filename)
    if not text:
        return

    pattern = "boolean|flowgorithm| i |javascript" \
        "|microsoft|pycharm|python|thonny"
    matches = re.findall(pattern, text)
    matches = sorted(list(set(matches)))
    if len(matches) > 0:
        assert False, \
            "README.md capitalize proper nouns. " \
            f"Found:\n{matches}"


def test_readme_assignment_1():
    test.check_readme_assignment_heading("Assignment 1")
    test.check_readme_assignment_content("Assignment 1")


def test_readme_assignment_2():
    test.check_readme_assignment_heading("Assignment 2")
    test.check_readme_assignment_content("Assignment 2")


def test_readme_assignment_3():
    test.check_readme_assignment_heading("Assignment 3")
    test.check_readme_assignment_content("Assignment 3")


def test_readme_assignment_4():
    test.check_readme_assignment_heading("Assignment 4")
    test.check_readme_assignment_content("Assignment 4")


def test_readme_assignment_5():
    test.check_readme_assignment_heading("Assignment 5")
    test.check_readme_assignment_content("Assignment 5")


def test_readme_assignment_6():
    test.check_readme_assignment_heading("Assignment 6")
    test.check_readme_assignment_content("Assignment 6")


def test_readme_assignment_7():
    test.check_readme_assignment_heading("Assignment 7")
    test.check_readme_assignment_content("Assignment 7")


def test_readme_assignment_8():
    test.check_readme_assignment_heading("Assignment 8")
    test.check_readme_assignment_content("Assignment 8")


def test_readme_assignment_9():
    test.check_readme_assignment_heading("Assignment 9")
    test.check_readme_assignment_content("Assignment 9")


def test_readme_assignment_10():
    test.check_readme_assignment_heading("Assignment 10")
    test.check_readme_assignment_content("Assignment 10")


def test_readme_assignment_11():
    test.check_readme_assignment_heading("Assignment 11")
    test.check_readme_assignment_content("Assignment 11")


def test_readme_assignment_12():
    test.check_readme_assignment_heading("Assignment 12")
    test.check_readme_assignment_content("Assignment 12")


def test_readme_assignment_13():
    test.check_readme_assignment_heading("Assignment 13")
    test.check_readme_assignment_content("Assignment 13")


def test_readme_assignment_14():
    test.check_readme_assignment_heading("Assignment 14")
    test.check_readme_assignment_content("Assignment 14")


def test_readme_final_project():
    test.check_readme_assignment_heading("Final Project")
    test.check_readme_assignment_content("Final Project")
