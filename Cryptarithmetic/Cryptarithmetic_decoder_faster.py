import re
import string
import itertools
import cProfile


def fast_solve(rawFormula):
    f, letters = compile_formula(rawFormula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, "".join(map(str, digits)))
                candidate = rawFormula.translate(table)
                if not re.search(r'\b0[0-9]', candidate):
                    return candidate
        except ArithmeticError:
            pass


def compile_formula(rawFormula, debug = True):
    """
    Compile formula into a function.
    :param rawFormula, debug = True if we want to actually  print how does lambda look like
    :return: the function as well as the letters used as an argument in the function
    """
    letters = "".join(set(re.findall("[A-Z]", rawFormula)))
    params = ", ".join(letters)
    partitions = map(compile_partition, re.split("([A-Z]+)", rawFormula))
    formula = "".join(partitions)
    f = "lambda {}: {}".format(params, formula)
    if debug: print f
    return eval(f), letters


def compile_partition(formulaPartition):
    """
    Compile a formula Partition of UPPER case letters as numeric digits (each word is a partition)
    None uppercase formula partition to be unchanged
    """
    if formulaPartition.isupper():
        terms = [('{}*{}'.format(10**i, d)) for i, d in enumerate(formulaPartition[::-1])]
        return "("+"+".join(terms)+")"
    else:
        return formulaPartition


question = "SEND + MORE == MONEY"

print fast_solve(question)

