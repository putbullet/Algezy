import numpy as np

def print_matrix_input_instructions():
    print("\nTo input a matrix, please follow this format:")
    print("1. Use brackets to define the matrix.")
    print("2. Enter the matrix elements as a list of lists.")
    print("3. Separate elements with commas and rows with new lines.")
    print("4. Ensure all rows have the same number of columns for a valid matrix.")
    print("\nExamples:")
    print("\n1. 2x2 Matrix:")
    print("   [[1, 2], [3, 4]]")
    print("\n2. 3x3 Matrix:")
    print("   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    print("\n3. 4x4 Matrix:")
    print("   [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]")
    print("\n4. 3x2 Matrix:")
    print("   [[1, 2], [3, 4], [5, 6]]")
    print("\n5. 2x3 Matrix:")
    print("   [[1, 2, 3],   [[1, 2, 3]]")
    print("\n6. 4x1 Matrix :")
    print("   [[1], [2], [3], [4]]")
    print("\n7. 1x4 Matrix :")
    print("   [[1, 2, 3, 4]]")

def get_matrix_input(prompt):
    print(prompt)
    while True:
        try:
            matrix = eval(input("Enter the matrix (in list of lists format): "))
            matrix = np.array(matrix)
            if matrix.ndim != 2:
                raise ValueError("Matrix must be 2-dimensional.")
            return matrix
        except (SyntaxError, ValueError, TypeError) as e:
            print(f"Invalid input: {e}. Please try again.")

def matrix_sum(matrix1, matrix2):
    return matrix1 + matrix2

def matrix_subtraction(matrix1, matrix2):
    return matrix1 - matrix2

def matrix_scalar_multiplication(matrix, scalar):
    return matrix * scalar

def matrix_transposition(matrix):
    return np.transpose(matrix)

def matrix_determinant(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Determinant can only be computed for square matrices.")
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Inverse can only be computed for square matrices.")
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular and cannot be inverted.")

def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def matrix_elementwise_multiplication(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def matrix_menu():
    print("\nSelect the operation you want to perform on the matrix:")
    print("1. Add two matrices")
    print("2. Subtract two matrices")
    print("3. Multiply a matrix by a scalar")
    print("4. Transpose a matrix")
    print("5. Compute the determinant")
    print("6. Compute the inverse")
    print("7. Multiply two matrices")
    print("8. Element-wise multiplication of two matrices")
    print("9. Exit")
    
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        matrix1 = get_matrix_input("Enter the first matrix:")
        matrix2 = get_matrix_input("Enter the second matrix:")
        result = matrix_sum(matrix1, matrix2)
        print("Sum of the matrices:")
        print(result)
    elif choice == 2:
        matrix1 = get_matrix_input("Enter the first matrix:")
        matrix2 = get_matrix_input("Enter the second matrix:")
        result = matrix_subtraction(matrix1, matrix2)
        print("Difference of the matrices:")
        print(result)
    elif choice == 3:
        matrix = get_matrix_input("Enter the matrix:")
        scalar = float(input("Enter the scalar value: "))
        result = matrix_scalar_multiplication(matrix, scalar)
        print(f"Matrix multiplied by {scalar}:")
        print(result)
    elif choice == 4:
        matrix = get_matrix_input("Enter the matrix:")
        result = matrix_transposition(matrix)
        print("Transpose of the matrix:")
        print(result)
    elif choice == 5:
        matrix = get_matrix_input("Enter the square matrix:")
        try:
            result = matrix_determinant(matrix)
            print(f"Determinant of the matrix: {result}")
        except ValueError as e:
            print(e)
    elif choice == 6:
        matrix = get_matrix_input("Enter the square matrix:")
        try:
            result = matrix_inverse(matrix)
            print("Inverse of the matrix:")
            print(result)
        except ValueError as e:
            print(e)
    elif choice == 7:
        matrix1 = get_matrix_input("Enter the first matrix:")
        matrix2 = get_matrix_input("Enter the second matrix:")
        try:
            result = matrix_multiplication(matrix1, matrix2)
            print("Product of the matrices:")
            print(result)
        except ValueError as e:
            print(e)
    elif choice == 8:
        matrix1 = get_matrix_input("Enter the first matrix:")
        matrix2 = get_matrix_input("Enter the second matrix:")
        try:
            result = matrix_elementwise_multiplication(matrix1, matrix2)
            print("Element-wise multiplication of the matrices:")
            print(result)
        except ValueError as e:
            print(e)
    elif choice == 9:
        print("Exiting the program...")
        print("chose 4 as a choise to exit the whole program")
        return
    else:
        print("Invalid choice. Please select a number from 1 to 9.")
    
    matrix_menu()

if __name__ == "__main__":
    print_matrix_input_instructions()
    matrix_menu()
