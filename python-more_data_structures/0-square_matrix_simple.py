#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Matrisin hər bir elementinin kvadratından ibarət yeni matris yaradır."""
    # Xarici list comprehension hər bir sətir üçün, 
    # daxili olan isə hər element üçün kvadrat hesablayır.
    return [[x**2 for x in row] for row in matrix]
