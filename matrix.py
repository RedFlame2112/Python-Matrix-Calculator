from sympy import *

def print_matrix(title, a):
    """
    Properly format a 2D array/matrix in a coherent manner
    """
    print(title)
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def zeros_mat(r, c):
    """
    r by c matrix full of zeroes
        :param r: rows of matrix
        :param c: columns of matrix
        :return: 2D array of the matrix (list containing elements of each row)
    """
    A = []
    while len(A) < r:
        A.append([])  # Generate Row
        while len(A[-1]) < c:  # traverse the columns until the last row is reached
            A[-1].append(0)  # initialize all column values to 0 until the last row is reached
    return A


def identity_mat(n):
    """
    Return an n by n square matrix such that each entry along the diagonal is 1 and the rest are all 0s
    To do this, take a zeroes matrix where every element [1][1], [2][2], ... , [i][i]
    for all i up to n is replaced with a 1
    """
    I = zeros_mat(n, n)  # initialize an n by n square zeroes matrix
    for i in range(0, n):
        I[i][i] = 1  # Traverse the matrix and replace every 0 along the diagonal with a 1
    return I


def copy_mat(M):
    """
    Creates and returns a copy of whatever matrix M was
    """
    row = len(M)  # get rows of matrix
    col = len(M[0])  # get all columns
    copy = zeros_mat(row, col)  # Create a 0's matrix of the same dimensions as the original

    for i in range(0, row):
        for j in range(0, col):
            copy[i][j] = M[i][j]  # elements are preserved
    return copy


def transpose_mat(M):
    """
    Takes a matrix M and transposes its columns and rows
    """
    res = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    print('\n')
    return res


def add_mat(A, B):
    """
    Add 2 matrices and return their sum
    """
    # Ensure that matrix addition is valid
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are incompatible as they are different sizes!')
    sum = zeros_mat(rowsA, colsB)
    # sum each matching element of A and B
    for i in range(0, rowsA):
        for j in range(0, colsB):
            sum[i][j] = A[i][j] + B[i][j]
    return sum


def subtract_mat(A, B):
    """
    subtract B from A and return the difference. More or less same principle as add_mat
    """
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are incompatible as they are different sizes!')
    diff = zeros_mat(rowsA, colsB)

    for i in range(0, rowsA):
        for j in range(0, colsB):
            diff[i][j] = A[i][j] - B[i][j]
    return diff


def multiply_mat(A, B):
    """
    matrix multiplication is arguably a tad more challenging than adding or subtracting lol
    the columns of matrix A(n*m) = rows of matrix B(m*p)
    ORDER MATTERS FOR MATRIX MULTIPLICATION

    for matrix C_(m*p) = A_(m*n)*B_(n*p) where C is a 3 by 3
    C[i][j] = (a[i][0]*b[0][j]) + (a[i][1]*b[1][j]) + (a[i][2]*b[2][j])
    """
    # once again, initialize rows and columns
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError('The number of columns of A must be equal to the number of rows of B!')

    # store the multiplication in a new 0s matrix of size (rowsA * colsB)
    product = zeros_mat(rowsA, colsB)
    for i in range(0, rowsA):
        for j in range(0, colsB):
            res = 0
            for ii in range(0, colsA):
                res += A[i][ii] * B[ii][j]
            product[i][j] = res

    return product


def multiply_many_mats(list):
    """
    given a list parameter of matrices, return the product of all of them.
    multiply_list_of_mats([A, B, C]) = ABC = (AB)C = A(BC). ORDER MATTERS AGAIN
    """
    mat_prod = list[0]  # initialize by beginning with the first matrix in the list
    # loop through every other matrix in the list
    for matrix in list[1:]:
        mat_prod = multiply_mat(mat_prod, matrix)

    return mat_prod


def check_square(A):
    """
    check if matrix is square or else warn that it is not invertible
    """
    if len(A) != len(A[0]):
        raise ArithmeticError('Matrix must be square.')


def determinant(A):
    """
    find determinant of matrix A
    """
    # Check for square matrix
    check_square(A)
    res = 0
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        res = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return res
    for cf in indices:
        Am = copy_mat(A)
        Am = Am[1:]
        height = len(Am)

        for i in range(0, height):
            Am[i] = Am[i][0:cf] + Am[i][cf + 1:]

        sign = (-1) ** (cf % 2)
        sub_det = determinant(Am)
        res += A[0][cf] * sign * sub_det
    return res


def check_singularity(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError('This is a singular matrix!')


def check_matrix_equality(A, B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check
        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], tol) != round(B[i][j], tol):
                    return False

    return True


def invert_matrix(A):
    """
    Returns the inverse of the passed in matrix.
    """
    # Confirm invertibility
    check_square(A)
    check_singularity(A)

    # Generate copies for row operations
    n = len(A)
    AM = copy_mat(A)
    I = identity_mat(n)
    IM = copy_mat(I)

    # Perform row operations
    indices = list(range(n))
    for fd in range(n):  # focus diagonal = fd
        fdScaler = 1.0 / AM[fd][fd]
        # scale fd row with fd inverse.
        for j in range(n):  # column loops with j
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:
            # skip row with fd in it.
            crScaler = AM[i][fd]  # cr stands for "current row".
            for j in range(n):
                # cr - crScaler * fdRow, but do this one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    return IM  # this is the inverse of the original matrix!



