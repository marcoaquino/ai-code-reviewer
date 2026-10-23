import os

print("Starting AI Code Reviewer tool...")


def analyze_file(file_path):
    # Check if the file actually exists before opening
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    print(f"\n🔍 Analyzing file: {file_path}")
    print("-" * 50)

    warnings_found = 0

    # Open and read the target Python file line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Loop through each line to search for anti-patterns
    for index, line in enumerate(lines):
        line_number = index + 1
        clean_line = line.strip()

        # 1. Check for functions missing docstrings or comments right after definition
        if clean_line.startswith("def "):
            # Check the next line if it exists
            if line_number < len(lines):
                next_line = lines[line_number].strip()
                # If the next line doesn't start with quotes or comments, trigger a warning
                if not (next_line.startswith('"""') or next_line.startswith("'''") or next_line.startswith("#")):
                    print(f"⚠️ Warning [Line {line_number}]: Function definition lacks documentation.")
                    warnings_found += 1

        # 2. Check for bad usage of the 'global' keyword
        if "global " in clean_line and not clean_line.startswith("#"):
            print(f"⚠️ Warning [Line {line_number}]: Avoid using the 'global' keyword. Keep variables scoped.")
            warnings_found += 1

    print("-" * 50)
    if warnings_found == 0:
        print("✅ Analysis complete: Code looks clean and compliant!")
    else:
        print(f"🚨 Analysis complete: Found {warnings_found} code quality warnings.")


# For testing, we will make our script analyze itself!
analyze_file("codigo_teste.py")
