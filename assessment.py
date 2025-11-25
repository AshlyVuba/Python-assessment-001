
def cube_number(number):
    """
    1. Receive a number.
    2. Return that number raised to the power of 3.
    """
    # TODO: Write your code here
    return pow(number, 3)
def check_even_or_odd(number):
    """
    1. Receive a number.
    2. If even, return "Even".
    3. If odd, return "Odd".
    """
    # TODO: Write your code here
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def combine_names(first_name, last_name):
    """
    1. Receive two strings (first_name and last_name).
    2. Return a single string in the format: "Last, First"
    Example: combine_names("James", "Bond") -> "Bond, James"
    """
    # TODO: Write your code here
    return f"{last_name}, {first_name}"

def get_last_item(my_list):
    """
    1. Receive a list.
    2. Return the last item in that list (use negative indexing).
    """
    # TODO: Write your code here
    return my_list[-1]

def sum_all_numbers(numbers):
    """
    1. Receive a list of numbers (e.g., [1, 2, 3]).
    2. Return the sum of all numbers in the list.
    Hint: You can use a 'for' loop or the built-in sum() function.
    """
    # TODO: Write your code here
    return sum(numbers)

def get_country_code(database : dict, country):
    """
    1. Receive a dictionary (database) and a key (country).
    2. Return the value associated with that key.
    Example input: {'ZA': 'South Africa', 'US': 'USA'}, 'ZA'
    Example output: 'South Africa'
    """
    # TODO: Write your code here
    for key, value in database.items():
        if key == country:
            return value
    return value
data = {"ZA": "South Africa", "JP": "Japan", "BR": "Brazil"}
print(get_country_code(data, "ZA"))