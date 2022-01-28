import matrix
import time
import sys
from sympy import *

def generateUserMatrix():
    rmain = int(input("Enter the number of rows you want in your matrix :"))
    cmain = int(input("Enter the number of columns you want in your matrix:"))

    matmain = []
    print("Enter your entries in here row-wise; entries wrap up to the next row after the row is filled: ")
    for i in range(rmain):
        k = []
        for j in range(cmain):
            k.append(float(input()))
        matmain.append(k)

    return matmain


def generateSecondMatrix():
    r2 = int(input("Enter the number of rows you want for matrix 2:"))
    c2 = int(input("Enter the number of columns you want for matrix 2:"))

    mat2 = []
    print("Enter your entries in here row-wise; entries wrap up to the next row after the row is filled: ")
    for i in range(r2):
        a = []
        for j in range(c2):
            a.append(float(input()))
        mat2.append(a)
    sys.stdout.flush()
    time.sleep(1)

    return mat2


def option1():
    """
    Generate Copy matrix
    """
    matrix1 = generateUserMatrix()
    copy_mat = matrix.copy_mat(matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    print('Here is an exact copy of the input matrix:')
    print('\n')
    return matrix.print_matrix("Copy", copy_mat)


def option2():
    """
    Generate Transpose matrix
    """
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    transpose = matrix.transpose_mat(matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    print('Here is the transpose of your matrix:')
    print('\n')
    return matrix.print_matrix("Transpose", transpose)


def option3():
    """
    Generate Identity matrix
    """
    n = int(input("Please enter an integer of your choice. "
                  "The larger it is, the slower the program:"))
    I = matrix.identity_mat(n)
    identity_name = "Identity matrix of size " + str(n) + " by " + str(n) + ": "
    return matrix.print_matrix(identity_name, I)


def option4():
    """
    Find Determinant
    """
    print('Please input a square matrix when prompted soon. '
          'A square matrix has the same number of rows and columns.')
    sys.stdout.flush()
    time.sleep(1.5)
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    det = matrix.determinant(matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    print('The determinant of this matrix is: ', det)


def option5():
    """
    Find Inverse
    """
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    inverse = matrix.invert_matrix(matrix1)
    print('\n')
    print('Generating inverse:')
    print('\n')
    sys.stdout.flush()
    time.sleep(0.5)
    matrix.print_matrix("Inverse", inverse)


def option6():
    """
    Add 2 matrices
    """
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    matrix2 = generateSecondMatrix()
    matrix.print_matrix("Matrix 2", matrix2)
    sum_matrix = matrix.add_mat(matrix1, matrix2)
    print('\n')
    print('The sum of the two matrices is: ')
    print('\n')
    return matrix.print_matrix("Summation", sum_matrix)


def option7():
    """
    Subtract 2 matrices
    """
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    matrix2 = generateSecondMatrix()
    matrix.print_matrix("Matrix 2", matrix2)
    difference = matrix.subtract_mat(matrix1, matrix2)
    print('\n')
    print('The difference of the two matrices is: ')
    print('\n')
    return matrix.print_matrix("Difference", difference)


def option8():
    """
    Multiply 2 matrices
    """
    print('Beware that in matrix multiplication, order matters!'
          ' The first matrix times the second is NOT the second times the first')
    matrix1 = generateUserMatrix()
    matrix.print_matrix("Matrix 1", matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    matrix2 = generateSecondMatrix()
    matrix.print_matrix("Matrix 2", matrix2)
    prod = matrix.multiply_mat(matrix1, matrix2)
    print('\n')
    print('The product of the two matrices is: ')
    print('\n')
    return matrix.print_matrix("Matrix Product", prod)

def option9():
    """
    Output the eigenvalues
    """
    print('Outputting eigenvalues')
    matrix1 = generateUserMatrix()
    list_matrix = Matrix(matrix1)
    matrix.print_matrix("Matrix 1", matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    eigenval = list_matrix.eigenvals()
    print("These are the eigenvalues in dictionary form, plus their multiplicity. "
          "The part to the left of the colon is the eigenvalue and to the right is the multiplicity.")
    print(eigenval)
def option10():
    """
    Output the eigenvalues
    """
    print(
        'Outputting eigenvectors and corresponding eigenvalues+multiplicities.This outputs a tuple of <eigenvalue> + <multiplicity> + <eigenvector>.\nKeep in mind that the eigenvector is NOT in reduced form')
    matrix1 = generateUserMatrix()
    list_matrix = Matrix(matrix1)
    matrix.print_matrix("Matrix 1", matrix1)
    sys.stdout.flush()
    time.sleep(0.5)
    eigenvect = list_matrix.eigenvects()
    print("These are the unreduced eigenvectors with corresponding eigenvalues + multiplicities")
    print(eigenvect)
