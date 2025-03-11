import re

def get_number_input(user_input: str) -> float:
    user_input = user_input.strip()

    if user_input == "":
        return 0  

    # def
    delimiters = [",", "\n"]

    if user_input.startswith("//"):
        match = re.match(r"//(\[.*?\]|\S)\n(.*)", user_input, re.DOTALL)
        if match:
            delimiter_part, numbers_part = match.groups()

            if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
                delimiters = re.findall(r"\[(.*?)\]", delimiter_part)  
            else:
                delimiters = [delimiter_part]  

            user_input = numbers_part 

    for delimiter in delimiters:
        user_input = user_input.replace(delimiter, "\n")

    try:
        numbers = list(map(float, user_input.splitlines()))

        if any(n < 0 for n in numbers):
            raise ValueError("Invalid input! Please enter valid numbers.")

        return sum(n for n in numbers if n <= 1000)

    except ValueError:
        raise ValueError("Invalid input! Please enter valid numbers.")
