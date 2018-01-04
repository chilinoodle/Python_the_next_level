# solve: runs through all possible combinations testing each for valid solution
# fill_in: creates a new formula replacing letters with numbers
# valid: tests out filled in string

import re
import string
import itertools


def valid(formula):
    """
    Formula is valid only if it has no leading zeros on any of its numbers
    and the formula evaluates as True
    :param formula: String
    :return: True or False
    """
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False


def fill_in(raw_formula):
    """
    Generates all possible translations between Chars and Numbers
    :param raw_formula:
    :return: Generator of translated raw formula
    """
    letters = "".join(set(re.findall("[A-Z]", raw_formula)))
    for digits in itertools.permutations("0123456789", len(letters)):
        table = string.maketrans(letters, "".join(digits))
        yield raw_formula.translate(table)


def solve(raw_formula):
    """
    Test all possible translations between chars and numbers
    :param raw_formula:
    :return: The solution to the puzzle or none if a solution was not found
    """
    for formula in fill_in(raw_formula):
        if valid(formula):
            return formula
    return None

question = "SEND + MORE == MONEY"

print solve(question)
