# shared test utility functions

import datetime
import pytest
import os
import re
import subprocess

_output_cache = []


def add_csharp_project(path, filename):
    try:
        with open(os.path.join(path, filename), "r") as file:
            text = file.read()

        pattern = "public class .+?\n"
        match = re.search(pattern, text)
        assert match, \
            f"{filename} could not find public class name"

        class_name = \
            filename.replace(".cs", "").replace("\\", "").replace(" ", "")

        text = text.replace(match.group(0), f"public class {class_name}\n")
        with open(os.path.join(path, filename), "w") as file:
            file.write(text)

        with open(os.path.join(path, "test.csproj"), "w") as file:
            file.write(
                "<Project Sdk=\"Microsoft.NET.Sdk\">\n"
                "  <PropertyGroup>\n"
                "    <OutputType>Exe</OutputType>\n"
                "    <TargetFramework>net5.0</TargetFramework>\n"
                f"    <StartupObject>{class_name}</StartupObject>\n"
                "  </PropertyGroup>\n"
                "</Project>\n"
            )
    except Exception as exception:
        assert False, exception


def add_javascript_window_methods(path, filename):
    try:
        with open(os.path.join(path, filename), "r+") as file:
            text = file.read()
            if "typeof window" in text:
                return

            if "window" in text or "alert" in text or "prompt" in text:
                file.write(
                    "\n"
                    "if (typeof alert === \"undefined\") {\n"
                    "    global.alert = function(message) {\n"
                    "        console.log(message);\n"
                    "    };\n"
                    "}\n"
                    "\n"
                    "if (typeof prompt === \"undefined\") {\n"
                    "    global.prompt = function(message) {\n"
                    "        var fs = require(\"fs\");\n"
                    "        var result = \"\";\n"
                    "        var buffer = Buffer.alloc(1);\n"
                    "\n"
                    "        console.log(message);\n"
                    "        for(;;){\n"
                    "            fs.readSync(0, buffer, 0, 1);\n"
                    "            if(buffer[0] === 10){\n"
                    "                break;\n"
                    "            }else if(buffer[0] !== 13){\n"
                    "                result += buffer.toString();\n"
                    "            }\n"
                    "        }\n"
                    "\n"
                    "        return result;\n"
                    "    }\n"
                    "}\n"
                    "\n"
                    "if (typeof window === \"undefined\") {\n"
                    "    global.window = {\n"
                    "        alert : global.alert,\n"
                    "        prompt : global.prompt\n"
                    "    };\n"
                    "}\n"
                )
                file.close()
    except Exception as exception:
        assert False, exception


def add_javascript_main_call(path, filename):
    try:
        with open(os.path.join(path, filename), "r+") as file:
            text = file.read()
            pattern = "^main()"
            match = re.search(pattern, text, re.MULTILINE)
            if not match:
                file.write(
                    "\n"
                    "main();\n"
                )
                file.close()
    except Exception as exception:
        assert False, exception


def append_text(path, filename, text):
    with open(os.path.join(path, filename), "a") as file:
        file.write(f"{datetime.datetime.now()} {text}\n")


def check_assignment_folder_structure(assignment, pattern, required=False):
    path = get_path(assignment)

    if required:
        assert path, f"Could not find folder named \"{assignment}\"."

    if not path:
        pytest.skip()
        return

    check_files(assignment, path, pattern)


def check_duplicate_activities(assignment1, assignment2):
    path1 = get_path(assignment1)
    if not path1:
        pytest.skip()
        return

    path2 = get_path(assignment2)
    if not path2:
        pytest.skip()
        return

    activities1 = [file for file in os.listdir(path1)]
    activities2 = [file for file in os.listdir(path2)]

    for activity1 in activities1:
        for activity2 in activities2:
            assert re.sub(r"#|\s", "", activity1) != \
                re.sub(r"#|\s", "", activity2), \
                f"{assignment2} duplicate activity already completed " \
                f"in {assignment1}. Select a different activity. " \
                f"Found {activity2}."


def check_files(assignment, path, pattern):
    files = []
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(path) as iterator:
        for entry in iterator:
            if entry.is_file():
                match = regex.match(entry.name)
                if not match:
                    files.append(entry.name)
    assert len(files) == 0, \
        f"{assignment} unexpected file name(s).\n{files}"


def check_file_contains(assignment, activity, file_extension,
    pattern, message):

    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\." + file_extension)
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    assert len(matches) >= 1, \
        f"{assignment} {filename} {message}"


def check_file_does_not_contain(assignment, activity, file_extension,
    pattern, message):

    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\." + file_extension)
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    assert len(matches) == 0, \
        f"{assignment} {filename} {message}\n" \
        f"Found: {matches}"


def check_flowgorithm_functions(assignment, activity, 
    input_count, processing_count, output_count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    functions = get_flowgorithm_functions(path, filename)

    result = f"{assignment} {filename}"

    main_functions = []
    input_functions = []
    processing_functions = []
    output_functions = []
    for function in functions:
        if function["type"] == "main":
            main_functions.append(function["name"])
        elif function["type"] == "input":
            input_functions.append(function["name"])
            if not function["returns"]:
                result += f"\n\nInput function {function['name']} " \
                "must return a value."
        elif function["type"] == "processing":
            processing_functions.append(function["name"])
            if not function["calls"] and not function["parameters"]:
                result += f"\n\nProcessing function {function['name']} " \
                    "must accept one or more parameters."
            if not function["calls"] and not function["returns"]:
                result += f"\n\nProcessing function {function['name']} " \
                    "should return a value."
        elif function["type"] == "output":
            output_functions.append(function["name"])
            # if not function["parameters"]:
            #     result += f"\n\nOutput function {function['name']} " \
            #         "must accept one or more parameters."
    
    if len(main_functions) < 1:
        result += f"\n\nExpected 1 main function. " \
            f"Found:\n{main_functions}"

    if len(input_functions) < input_count:
        result += f"\n\nExpected {input_count} input functions. " \
            f"Found:\n{input_functions}"

    if len(processing_functions) < processing_count:
        result += f"\n\nExpected {processing_count} processing functions. " \
            f"Found:\n{processing_functions}"

    if len(output_functions) < output_count:
        result += f"\n\nExpected {output_count} output functions. " \
            f"Found:\n{output_functions}"

    if "\n\n" in result:
        assert False, result


def check_flowgorithm_has_matching_source_code_file(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    assert filename, \
        f"{assignment} {activity} " \
        "Flowgorithm file is missing matching source code file."


def check_flowgorithm_input_functions(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = r"<function.+?<\/function>"
    matches = re.findall(pattern, text, re.DOTALL)
    functions = []
    for match in matches:
        if "<input variable=" in match:
            functions.append(match)

    matches = []
    pattern = "<function name=(.+?) type=(.+?) variable=(.+?)>"
    regex = re.compile(pattern, flags=re.DOTALL)
    for function in functions:
        match = regex.search(function)
        assert match, f"{assignment} {activity} " \
            "unexptected error searching for function name"

        name = match.group(1).replace("\"", "")
        type = match.group(2).replace("\"", "")
        assert "None" not in type, \
            f"{assignment} {activity} " \
            f"input function {name} must return a value."
        matches.append(name)

    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} input function(s). " \
        f"Found {len(matches)}.\n{matches}"


def check_flowgorithm_inputs(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = "<input variable="
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} input statement(s). " \
        f"Found {len(matches)}."


def check_flowgorithm_main_function(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = r"<function.+?<\/function>"
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        if "<function name=\"Main\"" not in match:
            continue

        assert "<input variable=" not in match, \
            "Main functions should not have input statements. " \
            "Use an input function instead."

        assert "<output expression=" not in match, \
            "Main functions should not have output statements. " \
            "Use an output function instead."


def check_flowgorithm_output(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = "<output expression="
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} output statement(s). " \
        f"Found {len(matches)}."


def check_flowgorithm_output_functions(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = r"<function.+?<\/function>"
    matches = re.findall(pattern, text, re.DOTALL)
    functions = []
    for match in matches:
        if "<input variable=" in match:
            continue

        if "<output expression=" not in match:
            continue

        functions.append(match)

    matches = []
    pattern = "<function name=(.+?) type=(.+?) variable=(.+?)>"
    regex = re.compile(pattern, flags=re.DOTALL)
    for function in functions:
        match = regex.search(function)
        assert match, f"{assignment} {activity} " \
            "unexptected error searching for function name"

        name = match.group(1).replace("\"", "")
        type = match.group(2).replace("\"", "")

        assert "None" in type, \
            f"{assignment} {activity} " \
            f"output function {name} should not return a value."

        pattern = "<parameter name=(.+?).+?>"
        parameters = re.findall(pattern, function)

        # assert len(parameters) > 0, \
        #     f"output function {name} should have parameters to output."

        matches.append(name)

    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} output function(s). " \
        f"Found {len(matches)}.\n{matches}"


def check_flowgorithm_processing(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = "<assign variable="
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} assignment statement(s). " \
        f"Found {len(matches)}. " \
        "Use intermediate variables for processing."


def check_flowgorithm_processing_functions(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = r"<function.+?<\/function>"
    matches = re.findall(pattern, text, re.DOTALL)
    functions = []
    for match in matches:
        if "<input variable=" in match:
            continue

        if "<output expression=" in match:
            continue

        functions.append(match)

    matches = []
    pattern = "<function name=(.+?) type=(.+?) variable=(.+?)>"
    regex = re.compile(pattern, flags=re.DOTALL)
    for function in functions:
        match = regex.search(function)
        assert match, f"{assignment} {activity} " \
            "unexptected error searching for function name"

        name = match.group(1).replace("\"", "")
        type = match.group(2).replace("\"", "")

        if name == "Main":
            continue

        pattern = "<parameter name=(.+?).+?>"
        parameters = re.findall(pattern, function)

        assert "None" not in type, \
            f"{assignment} {activity} " \
            f"processing function {name} must return a value."

        assert len(parameters) > 0, \
            f"processing function {name} should have parameters to process."

        matches.append(name)

    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} processing function(s). " \
        f"Found {len(matches)}.\n{matches}"


def check_flowgorithm_variables(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename).strip()

    assert text[0:5] == "<?xml", \
        f"{assignment} {filename} is not a valid Flowgorithm file."

    pattern = "<declare name="
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} " \
        f"variable declaration(s). Found {len(matches)}. " \
        "Use intermediate variables for processing."


def check_git_log(assignment, pattern, message):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    try:
        args = "git -C " + \
            os.getcwd().replace(" ", "\\ ") + \
            " --no-pager log -p"
        output = subprocess.check_output(
            args,
            shell=True,
            stderr=subprocess.PIPE,
            text=True)

        regex = re.compile(pattern, re.IGNORECASE)
        match = regex.search(output)
        assert match, message
    except UnicodeDecodeError:
        pass
    except subprocess.CalledProcessError as exception:
        assert False, exception


def check_java_class(path, filename):
    try:
        with open(os.path.join(path, filename), "r") as file:
            text = file.read()

        pattern = "public class (.+?) {"
        match = re.search(pattern, text)
        assert match, \
            f"{filename} could not find public class name"

        class_name = \
            filename.replace(".java", "").replace("\\", "").replace(" ", "")
        text = text.replace(match.group(0), f"public class {class_name} " + "{")

        with open(os.path.join(path, filename), "w") as file:
            file.write(text)
    except Exception as exception:
        assert False, exception


def check_javascript_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.js")
    if not filename:
        pytest.skip()
        return

    try:
        args = "npx eslint --no-eslintrc --env \"es6\" " + \
            os.path.join(path, filename).replace(" ", "\\ ")
        output = subprocess.check_output(
            args,
            shell=True,
            stderr=subprocess.PIPE,
            text=True)
    except subprocess.CalledProcessError as exception:
        output = exception.output
        output = output.replace(path + "/", "")

        assert not output, \
            f"{assignment} {activity} " \
            f"JavaScript source code formatting:\n{output}\n"


def check_javascript_output(assignment, activity, file_pattern,
    input, output_pattern, message):

    if file_pattern:
        path = get_path(assignment)
        if not path:
            pytest.skip()
            return

        filename = get_filename(path, activity + r"\.js")
        if not filename:
            pytest.skip()
            return

        text = read_file(path, filename)
        regex = re.compile(file_pattern, re.IGNORECASE)
        match = regex.search(text)
        if not match:
            pytest.skip()
            return

    output = get_javascript_output(assignment, activity, input)
    if output is None:
        pytest.skip()
        return

    regex = re.compile(output_pattern, re.IGNORECASE)
    match = regex.search(output)
    assert match, \
        f"{assignment} {activity} {message}\n" \
        f"Input:\n{input}\n" \
        f"Output:\n{output}"


def check_overall_folder_structure(pattern):
    folders = []
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(os.getcwd()) as iterator:
        for entry in iterator:
            if entry.is_dir():
                match = regex.match(entry.name)
                if not match:
                    folders.append(entry.name)
    assert len(folders) == 0, \
        f"Unexpected folder name(s)\n{folders}"


def check_overall_file_structure(pattern):
    files = []
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(os.getcwd()) as iterator:
        for entry in iterator:
            if entry.is_file():
                match = regex.match(entry.name)
                if not match:
                    files.append(entry.name)
    assert len(files) == 0, \
        "Unexpected root folder file name(s). " \
        "Use separate folders for each assignment. " \
        f"Found:\n{files}"


def check_pseudocode_output(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.txt")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    pattern = "Output "
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {filename} is missing output statement(s)."


def check_source_code_comma_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    if ".py" in filename:
        text = re.sub("#.*?\n", "", text)
    else:
        text = re.sub(r"\/\/.*?\n", "", text)

    pattern = r"\s,|,\S"
    matches = re.findall(pattern, text, flags=re.DOTALL)

    assert len(matches) == 0, \
        f"{assignment} {filename} " \
        f"has non-standard spacing around commas.\nFound: {matches}"


def check_python_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.py")
    if not filename:
        pytest.skip()
        return

    try:
        args = "flake8 " + \
            "--ignore=E125,E127,E128,E131,E722,W291,W292,W293,W504 " + \
            os.path.join(path, filename).replace(" ", "\\ ")
        output = subprocess.check_output(
            args,
            shell=True,
            stderr=subprocess.PIPE,
            text=True)
    except subprocess.CalledProcessError as exception:
        output = exception.output
        output = output.replace(path + "/", "")

    text = read_file(path, filename)

    pattern = "\t"
    match = re.search(pattern, text)
    if match:
        output = "Contains tab characters. Replace tabs with spaces.\n" + output

    pattern = r"^ +main\(\)$"
    match = re.search(pattern, text, re.MULTILINE)
    if match and "__main__" not in text:
        output = "Call to main() must not be indented.\n" + output

    assert not output, \
        f"{assignment} {activity} " \
        f"Python source code formatting:\n{output}\n"


def check_python_output(assignment, activity, file_pattern,
    input, output_pattern, message):

    if file_pattern:
        path = get_path(assignment)
        if not path:
            pytest.skip()
            return

        filename = get_filename(path, activity + r"\.py")
        if not filename:
            pytest.skip()
            return

        text = read_file(path, filename)
        regex = re.compile(file_pattern, re.IGNORECASE)
        match = regex.search(text)
        if not match:
            pytest.skip()
            return

    output = get_python_output(assignment, activity, input)
    if output is None:
        pytest.skip()
        return

    assert "Traceback" not in output, \
        f"{assignment} {activity} {message}\n" \
        f"Input:\n{input}\n" \
        f"Output:\n{output}"

    regex = re.compile(output_pattern, re.IGNORECASE)
    match = regex.search(output)
    assert match, \
        f"{assignment} {activity} {message}\n" \
        f"Input:\n{input}\n" \
        f"Output:\n{output}"


def check_python_output_functions(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.py")
    if not filename:
        pytest.skip()
        return

    functions = get_python_functions(path, filename)

    matches = []
    for function in functions:
        if "input(" in function["text"]:
            continue

        if "print(" not in function["text"]:
            continue

        matches.append(function["name"])

    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} output function(s). " \
        f"Found {len(matches)}.\n{matches}"


def check_readme_assignment_heading(assignment):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    text = read_file(os.getcwd(), "README.md")
    pattern = "## *" + assignment + " *\n"
    regex = re.compile(pattern, re.IGNORECASE)
    match = regex.search(text)
    if not match:
        assert False, f"README.md missing required ## {assignment} heading."


def check_readme_assignment_content(assignment):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    text = read_file(os.getcwd(), "README.md")
    pattern = "## *" + assignment + r"\s+(.+?)(\n#)?$"
    regex = re.compile(pattern, re.IGNORECASE | re.DOTALL)
    match = regex.search(text)
    if not match:
        assert False, f"README.md missing required {assignment} paragraph."

    paragraph = match.group(1)
    words = paragraph.split()
    if len(words) < 100:
        assert False, \
            f"README.md {assignment} paragraph lacks detail. " \
            "Expand on your ideas. Expecting 100+ words, found " \
            f"{len(words)}."


def check_required_files(assignment, file_extension, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    description = get_file_type(file_extension)
    pattern = r"activity[ _]?#?\d\." + file_extension + "|" + \
        r"final[ _]project." + file_extension
    files = get_files(path, pattern)
    assert len(files) >= count, \
        f"{assignment} requires {count} {description} file(s). " \
        f"Found {len(files)}.\n{files}"


def check_source_code_comments(assignment, activity, count,
    file_extension="(cs|java|js|lua|py)"):

    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\." + file_extension)
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    if file_extension == "fprg":
        pattern = "<comment text="
    elif file_extension == "txt":
        pattern = "... "
    elif ".lua" in filename:
        pattern = "^--"
    elif ".py" in filename:
        pattern = "^#"
    else:
        pattern = r"^\s*\/\/"

    matches = re.findall(pattern, text, re.MULTILINE)
    assert len(matches) >= count, \
        f"{assignment} {filename} is missing comments."

    # Commented out - currently checking Flowgorithm-generated code.
    # if "|" not in file_extension:
    #     return

    # matches = re.findall(pattern, text)
    # assert len(matches) >= count, \
    #     f"{assignment} {filename} is missing comments " \
    #         "at the top of the program."


def check_source_code_comment_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.py")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    if ".py" in filename:
        pattern = r"(^#.+?\n)*\n"
    else:
        pattern = r"(^\/\/.+?\n)*\n"

    matches = re.findall(pattern, text, flags=re.MULTILINE)
    assert len(matches) >= 1, \
        f"{assignment} {filename} " \
        "should include a blank line after comment."

    matches = re.findall(pattern, text)
    assert len(matches) >= 1, \
        f"{assignment} {filename} " \
        "should include a blank line after comment."


def check_source_code_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    if ".cs" in filename:
        pass
    elif ".java" in filename:
        pass
    elif ".js" in filename:
        check_javascript_formatting(assignment, activity)
    elif ".lua" in filename:
        pass
    elif ".py" in filename:
        check_python_formatting(assignment, activity)
    else:
        assert False, f"Unexpected file type for {filename}"


def check_source_code_functions(assignment, activity, 
    input_count, processing_count, output_count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    if ".cs" in filename:
        functions = get_csharp_functions(path, filename)
    elif ".java" in filename:
        functions = get_java_functions(path, filename)
    elif ".js" in filename:
        functions = get_javascript_functions(path, filename)
    elif ".lua" in filename:
        functions = get_lua_functions(path, filename)
    elif ".py" in filename:
        functions = get_python_functions(path, filename)
    else:
        assert False, f"Unexpected file type for {filename}"

    result = f"{assignment} {filename}"

    input_functions = []
    processing_functions = []
    output_functions = []
    main_functions = []
    for function in functions:
        if function["type"] == "main":
            main_functions.append(function["name"])
        elif function["type"] == "input":
            input_functions.append(function["name"])
            if not function["returns"]:
                result += f"\n\nInput function {function['name']} " \
                "must return a value."
        elif function["type"] == "processing":
            processing_functions.append(function["name"])
            if not function["calls"] and not function["parameters"]:
                result += f"\n\nProcessing function {function['name']} " \
                    "must accept one or more parameters."
            if  not function["calls"] and not function["returns"]:
                result += f"\n\nProcessing function {function['name']} " \
                    "should return a value."
        elif function["type"] == "output":
            output_functions.append(function["name"])
            # if not function["parameters"]:
            #     result += f"\n\nOutput function {function['name']} " \
            #         "must accept one or more parameters."

    if len(main_functions) < 1:
        result += f"\n\nExpected 1 main function. " \
            f"Found:\n{main_functions}"

    if len(input_functions) < input_count:
        result += f"\n\nExpected {input_count} input functions. " \
            f"Found:\n{input_functions}"

    if len(processing_functions) < processing_count:
        result += f"\n\nExpected {processing_count} processing functions. " \
            f"Found:\n{processing_functions}"

    if len(output_functions) < output_count:
        result += f"\n\nExpected {output_count} output functions. " \
            f"Found:\n{output_functions}"

    names = []
    for function in functions:
        if function["type"] == "main":
            continue
        name = function["name"]
        if ".lua" in filename or ".py" in filename:
            if name != name.lower() or "_" not in name:
                names.append(name)
        else:
            if name == name.lower() or "_" in name:
                names.append(name)

    if len(names) > 0:
        result += f"\n\nExpected snake_case (Python, Lua), " \
            "camelCase (Java, JavaScript), or PascalCase (C#) " \
            "function names. " \
            f"Found:\n{names}"

    if "\n\n" in result:
        assert False, result


def check_source_code_identifier_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    pattern = r"(\w+) *="
    matches = re.findall(pattern, text)
    if ".lua" in filename or ".py" in filename:
        variables = []
        for match in matches:
            if match == match.upper():
                continue
            if match == match.lower():
                continue
            variables.append(match)

        assert len(variables) == 0, \
            f"{assignment} {filename} " \
            "contains mixed case variable names. Use snake_case. " \
            f"Found:\n{variables}"
    else:
        # Consider checking camelCase or PascalCase here
        pass


def check_source_code_identifier_length(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    pattern = r"^\s*(\w+) *="
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    variables = []
    for match in matches:
        if len(match) == 1:
            variables.append(match)
    variables = sorted(list(set(variables)))

    assert len(variables) == 0, \
        f"{assignment} {filename} " \
        "needs meaningful identifiers. Avoid abbreviations. " \
        f"Found:\n{variables}"


def check_source_code_line_spacing(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    pattern = r"\n^\s*\n"
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    assert len(matches) >= 3, \
        f"{assignment} {filename} " \
        "should include a blank line between logical parts of the code. " \
        "Separate comments, input, processing, and output with a blank line."

    pattern = r"\n.+?\n.+?\n"
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    assert len(matches) > 0, \
        f"{assignment} {filename} " \
        "should include a blank line between logical parts of the code. " \
        "Separate comments, input, processing, and output " \
        "with a blank line. Avoid double-spacing every line."


def check_source_code_inputs(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    if ".cs" in filename:
        pattern = r"Console\.ReadLine\(|readValue\("
    elif ".java" in filename:
        pattern = r"input\."
    elif ".js" in filename:
        pattern = r"prompt\("
    elif ".lua" in filename:
        pattern = r"io\.read\("
    elif ".py" in filename:
        pattern = r"input\("
    else:
        assert False, f"Unexpected file type for {filename}"

    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} input statement(s). " \
        f"Found {len(matches)}."


def check_source_code_operator_formatting(assignment, activity):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.fprg")
    if filename:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)
    text = re.sub(r'".+?"', '""', text)
    text = re.sub(r"'.+?'", "''", text)

    if ".java" in filename:
        text = re.sub("import .+?;\n", "", text)
        text = re.sub(r"\/\/.*?\n", "\n", text)
    elif ".lua" in filename:
        text = re.sub(r"\-\-.*?\n", "\n", text)
    elif ".py" in filename:
        text = re.sub("#.*?\n", "\n", text)
        text = re.sub(r"\*\*", "", text)
    else:
        text = re.sub(r"\/\/.*?\n", "\n", text)

    if ".py" not in filename:
        pattern = r"\S[+\-\*\/=]\S|\S[+\-\*\/=]\s|\s[+\-\*\/=]\S"
        matches = re.findall(pattern, text)
        matches = sorted(list(set(matches)))

        pattern = r"\+=|-=|\*=|\/=|<=|>=|==|!=|===|!==|-\w+|\+\+|--|\/\/"
        for index in range(len(matches) - 1, -1, -1):
            if re.search(pattern, matches[index]):
                matches.remove(matches[index])

        assert len(matches) == 0, \
            f"{assignment} {filename} " \
            f"is missing spaces around operators.\nFound: {matches}"


def check_source_code_processing(assignment, activity, count):
    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    text = read_file(path, filename)

    pattern = r"\w+ *="
    matches = re.findall(pattern, text)
    assert len(matches) >= count, \
        f"{assignment} {activity} requires {count} assignment statement(s). " \
        f"Found {len(matches)}. " \
        "Use intermediate variables for processing."


def check_source_code_output(assignment, activity, file_pattern,
    input, output_pattern, message):

    path = get_path(assignment)
    if not path:
        pytest.skip()
        return

    filename = get_filename(path, activity + r"\.(cs|java|js|lua|py)")
    if not filename:
        pytest.skip()
        return

    if file_pattern:
        text = read_file(path, filename)
        regex = re.compile(file_pattern, re.IGNORECASE)
        match = regex.search(text)
        if not match:
            pytest.skip()
            return

    if ".cs" in filename:
        output = get_csharp_output(assignment, activity, input)
    elif ".java" in filename:
        output = get_java_output(assignment, activity, input)
    elif ".js" in filename:
        output = get_javascript_output(assignment, activity, input)
    elif ".lua" in filename:
        output = get_lua_output(assignment, activity, input)
    elif ".py" in filename:
        output = get_python_output(assignment, activity, input)
    else:
        assert False, f"{assignment} {activity} unexpected filename {filename}"

    if output is None:
        pytest.skip()
        return

    if ".cs" in filename:
        assert "exception" not in output, \
            f"{assignment} {activity} {message}\n" \
            f"Input:\n{input}\n" \
            f"Output:\n{output}"

    if ".py" in filename:
        assert "Traceback" not in output, \
            f"{assignment} {activity} {message}\n" \
            f"Input:\n{input}\n" \
            f"Output:\n{output}"

    regex = re.compile(output_pattern, re.IGNORECASE | re.DOTALL)
    match = regex.search(output)
    assert match, \
        f"{assignment} {activity} {message}\n" \
        f"Input:\n{input}\n" \
        f"Output:\n{output}"


def compile_java_program(path, filename):
    args = "javac " + \
        os.path.join(path, filename).replace(" ", "\\ ")
    try:
        output = subprocess.check_output(
            args,
            shell=True,
            stderr=subprocess.PIPE,
            text=True)
        output_cache(path, filename, input, output)
        return
    except subprocess.CalledProcessError as exception:
        output_cache(path, filename, input,
            f"{exception.output}\n"
            f"{exception.stderr}")


def get_csharp_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"(public|private) static (.+?) (.+?) *\((.*?)\)\s*\{"
    matches = []
    for match in re.finditer(pattern, text, re.MULTILINE):
        matches.append(match)

    functions = []
    for index in range(len(matches)):
        match = matches[index]
        function = {}
        function["name"] = match.group(3)
        if match.group(2) == "void":
            function["returns"] = None
        else:
            function["returns"] = match.group(2)
        function["parameters"] = match.group(4)
        if index < len(matches) - 1:
            next_match = matches[index + 1]
            function_text = \
                text[match.start(0):next_match.start(0)].strip()
        else:
            function_text = text[match.start(0):].strip()
            if function_text.count("}") > function_text.count("{"):
                function_text = re.sub("}$", "", function_text).strip()

        function_text = re.sub("}.+?$", "", function_text, flags=re.DOTALL)
        function["text"] = function_text
        functions.append(function)

    pattern = r"^\s*(\w+\s*=\s*)?(\w+)\(.*?\)"
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    for function in functions:
        if function["name"] == "Main":
            function["type"] = "main"
        elif "Console.Read" in function["text"]:
            function["type"] = "input"
        elif "Console.Write" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    return functions


def get_csharp_output(assignment, activity, input):
    path = get_path(assignment)
    if not path:
        return None

    filename = get_filename(path, activity + r"\.cs")
    if not filename:
        return None

    output = output_cache(path, filename, input)
    if output is None:
        add_csharp_project(path, filename)
        args = "dotnet run --project " + \
            os.path.join(path, "test.csproj").replace(" ", "\\ ")
        try:
            output = subprocess.check_output(
                args,
                input=input,
                shell=True,
                stderr=subprocess.PIPE,
                text=True)
            output_cache(path, filename, input, output)
        except subprocess.CalledProcessError as exception:
            output = f"{exception.output}\n{exception.stderr}"
            output_cache(path, filename, input, output)

    return output


def get_file_type(file_extension):
    dictionary = {
        "cs": "C#",
        "java": "Java",
        "js": "JavaScript",
        "lua": "Lua",
        "py": "Python",
        "txt": "pseudocode"
    }

    try:
        description = dictionary[file_extension]
    except:
        description = file_extension

    return description


def get_files(path, pattern):
    files = []
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(path) as iterator:
        for entry in iterator:
            if entry.is_file():
                match = regex.search(entry.name)
                if match:
                    files.append(entry.name)
    return files


def get_filename(path, pattern):
    pattern = pattern.replace(" ", "[ _]?#?")
    pattern = "^" + pattern + "$"
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(path) as iterator:
        for entry in iterator:
            if entry.is_file():
                match = regex.match(entry.name)
                if match:
                    return entry.name


def get_flowgorithm_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"<function name=\"(.+?)\" " \
        r"type=\"(.+?)\" " \
        r"variable=\"(.*?)\">" \
        r".+?<\/function>"
    matches = []
    for match in re.finditer(pattern, text, re.DOTALL):
        matches.append(match)

    functions = []
    for match in matches:
        function = {}
        function["name"] = match.group(1)
        function["text"] = match.group(0)
        function["returns"] = match.group(3)
        pattern = r"<parameter name=\"(.+?)\""
        parameters = re.findall(pattern, function["text"])
        function["parameters"] = ", ".join(parameters)
        functions.append(function)

    pattern = r"^\s+<(call|assign).+?expression=\"(.+?)\("
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    for function in functions:
        if function["name"] == "Main":
            function["type"] = "main"
        elif "<input variable" in function["text"]:
            function["type"] = "input"            
        elif "<output expression" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    
    return functions


def get_java_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"(public|private) static (.+?) (.+?) *\((.*?)\)\s*\{"
    matches = []
    for match in re.finditer(pattern, text, re.MULTILINE):
        matches.append(match)

    functions = []
    for index in range(len(matches)):
        match = matches[index]
        function = {}
        function["name"] = match.group(3)
        if match.group(2) == "void":
            function["returns"] = None
        else:
            function["returns"] = match.group(2)
        function["parameters"] = match.group(4)
        if index < len(matches) - 1:
            next_match = matches[index + 1]
            function_text = \
                text[match.start(0):next_match.start(0)].strip()
        else:
            function_text = text[match.start(0):].strip()
            if function_text.count("}") > function_text.count("{"):
                function_text = re.sub("}$", "", function_text).strip()

        function_text = re.sub("}.+?$", "", function_text, flags=re.DOTALL)
        function["text"] = function_text
        functions.append(function)

    pattern = r"^\s*(\w+\s*=\s*)?(\w+)\(.*?\)"
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    for function in functions:
        if function["name"] == "main":
            function["type"] = "main"
        elif "input." in function["text"]:
            function["type"] = "input"
        elif "System.out" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    return functions


def get_java_output(assignment, activity, input):
    path = get_path(assignment)
    if not path:
        return None

    filename = get_filename(path, activity + r"\.java")
    if not filename:
        return None

    check_java_class(path, filename)
    
    output = output_cache(path, filename, input)
    if output is None:
        compile_java_program(path, filename)
        args = "java -cp " + path + " " + \
            filename.replace(".java", "").replace(" ", "\\ ")
        try:
            output = subprocess.check_output(
                args,
                input=input,
                shell=True,
                stderr=subprocess.PIPE,
                text=True)
            output_cache(path, filename, input, output)
        except subprocess.CalledProcessError as exception:
            output = f"{exception.output}\n{exception.stderr}"
            output_cache(path, filename, input, output)
    
    return output


def get_javascript_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"function (.+?) *\((.*?)\)\s*\{"
    matches = []
    for match in re.finditer(pattern, text, re.MULTILINE):
        matches.append(match)

    functions = []
    for index in range(len(matches)):
        match = matches[index]
        function = {}
        function["name"] = match.group(1)
        function["parameters"] = match.group(2)
        if index < len(matches) - 1:
            next_match = matches[index + 1]
            function_text = \
                text[match.start(0):next_match.start(0)].strip()
        else:
            function_text = text[match.start(0):].strip()
            if function_text.count("}") > function_text.count("{"):
                function_text = re.sub("}$", "", function_text).strip()

        function_text = re.sub("}.+?$", "", function_text, flags=re.DOTALL)
        function["text"] = function_text
        functions.append(function)

    pattern = r"^\s*(\w+\s*=\s*)?(\w+)\(.*?\)"
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    pattern = r"return (.+?)$"
    for function in functions:
        match = re.search(pattern, function["text"], re.MULTILINE)
        if match:
            function["returns"] = match.group(1)
        else:
            function["returns"] = None

    for function in functions:
        if function["name"] == "main":
            function["type"] = "main"
        elif "prompt" in function["text"]:
            function["type"] = "input"
        elif "alert" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    return functions


def get_javascript_output(assignment, activity, input):
    path = get_path(assignment)
    if not path:
        return None

    filename = get_filename(path, activity + r"\.js")
    if not filename:
        return None

    output = output_cache(path, filename, input)

    if output is None:
        add_javascript_window_methods(path, filename)
        add_javascript_main_call(path, filename)
        args = "node " + os.path.join(path, filename).replace(" ", "\\ ")
        try:
            output = subprocess.check_output(
                args,
                input=input,
                shell=True,
                stderr=subprocess.PIPE,
                text=True)
            output_cache(path, filename, input, output)
        except subprocess.CalledProcessError as exception:
            output = f"{exception.output}\n{exception.stderr}"
            output_cache(path, filename, input, output)

    return output


def get_lua_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"function (.+?) *\((.*?)\)"
    matches = []
    for match in re.finditer(pattern, text, re.MULTILINE):
        matches.append(match)

    functions = []
    for index in range(len(matches)):
        match = matches[index]
        function = {}
        function["name"] = match.group(1)
        function["parameters"] = match.group(2)
        if index < len(matches) - 1:
            next_match = matches[index + 1]
            function_text = \
                text[match.start(0):next_match.start(0)].strip()
        else:
            function_text = text[match.start(0):].strip()

        function["text"] = function_text
        functions.append(function)

    pattern = r"^\s*(\w+\s*=\s*)?(\w+)\(.*?\)"
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    pattern = r"return (.+?)$"
    for function in functions:
        match = re.search(pattern, function["text"], re.MULTILINE)
        if match:
            function["returns"] = match.group(1)
        else:
            function["returns"] = None

    for function in functions:
        if function["name"] == "main":
            function["type"] = "main"
        elif "io.read" in function["text"]:
            function["type"] = "input"
        elif "print" in function["text"]:
            function["type"] = "output"
        elif "io.write" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    return functions


def get_lua_output(assignment, activity, input):
    path = get_path(assignment)
    if not path:
        return None

    filename = get_filename(path, activity + r"\.lua")
    if not filename:
        return None

    output = output_cache(path, filename, input)

    if output is None:
        args = "lua " + os.path.join(path, filename).replace(" ", "\\ ")
        try:
            output = subprocess.check_output(
                args,
                input=input,
                shell=True,
                stderr=subprocess.PIPE,
                text=True)
            output_cache(path, filename, input, output)
        except subprocess.CalledProcessError as exception:
            output = f"{exception.output}\n{exception.stderr}"
            output_cache(path, filename, input, output)

    return output


def get_path(pattern):
    pattern = "^" + pattern.replace(" ", "( *|_)") + "$"
    regex = re.compile(pattern, re.IGNORECASE)
    with os.scandir(os.getcwd()) as iterator:
        for entry in iterator:
            if entry.is_dir():
                match = regex.match(entry.name)
                if match:
                    return entry.path


def get_python_functions(path, filename):
    text = read_file(path, filename)

    pattern = r"^def (.+?)\((.*?)\).*?:"
    matches = []
    for match in re.finditer(pattern, text, re.MULTILINE):
        matches.append(match)

    functions = []
    pattern = r"^def (.+?)\((.*?)\).+?^\S"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
    for match in matches:
        function = {}
        function["name"] = match.group(1)
        function["parameters"] = match.group(2)
        end_match = regex.search(text[match.start(0):])
        if end_match:
            function["text"] = end_match.group(0)[:-1].strip()
        else:
            function["text"] = text[match.start(0):].strip()
        functions.append(function)

    pattern = r"^\s*(\w+\s*=\s*)?(\w+)\(.*?\)"
    for function in functions:
        matches = re.findall(pattern, function["text"], flags=re.MULTILINE)
        calls = [match[1] for match in matches]
        function["calls"] = ", ".join(calls)

    pattern = r"return (.+?)$"
    for function in functions:
        match = re.search(pattern, function["text"], re.MULTILINE)
        if match:
            function["returns"] = match.group(1)
        else:
            function["returns"] = None

    for function in functions:
        if function["name"] == "main":
            function["type"] = "main"
        elif "input(" in function["text"]:
            function["type"] = "input"            
        elif "print(" in function["text"]:
            function["type"] = "output"
        else:
            function["type"] = "processing"

    return functions


def get_python_output(assignment, activity, input):
    path = get_path(assignment)
    if not path:
        return None

    filename = get_filename(path, activity + r"\.py")
    if not filename:
        return None

    output = output_cache(path, filename, input)

    if output is None:
        args = "python3 " + os.path.join(path, filename).replace(" ", "\\ ")
        try:
            output = subprocess.check_output(
                args,
                input=input,
                shell=True,
                stderr=subprocess.PIPE,
                text=True)
            output_cache(path, filename, input, output)
        except subprocess.CalledProcessError as exception:
            output = f"{exception.output}\n{exception.stderr}"
            output_cache(path, filename, input, output)

    return output


def output_cache(path, filename, input, output=None):
    global _output_cache

    if output:
        dictionary = {
            "path": path,
            "filename": filename,
            "input": input,
            "output": output
        }
        _output_cache.append(dictionary)
        return output

    for entry in _output_cache:
        if entry["path"] == path and \
            entry["filename"] == filename and \
            entry["input"] == input:
            return entry["output"]

    return None


def read_file(path, filename):
    filepath = os.path.join(path, filename)
    try:
        with open(filepath, "r") as file:
            text = file.read()
        return text
    except Exception as exception:
        assert False, f"Error reading {filepath}\n{exception}"


if __name__ == "__main__":
    check_git_log(
        "Assignment 2",
        "hello.+?world",
        "Git log is missing required \"Hello world!\" text. "
            "You must commit Activity 1 changes before working on "
            "Activity 2.")
