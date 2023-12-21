import numpy as np


def RectPS(x1, y1, x2, y2):
    """
    Calculate the perimeter P and area S of a rectangle
    with opposite vertices at (x1, y1) and (x2, y2).
    Returns P and S as a tuple.
    """
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    P = 2 * (length + width)
    S = length * width
    return P, S

def task1():
    """
    Input data, call function RectPS, and output results.
    """
    rectangles = []

    for i in range(3):
        x1 = int(input(f"Enter x1 for rectangle {i + 1}: "))
        y1 = int(input(f"Enter y1 for rectangle {i + 1}: "))
        x2 = int(input(f"Enter x2 for rectangle {i + 1}: "))
        y2 = int(input(f"Enter y2 for rectangle {i + 1}: "))

        rectangles.append((x1, y1, x2, y2))

    for i, rectangle in enumerate(rectangles):
        P, S = RectPS(*rectangle)
        print(f"Rectangle {i + 1} - Perimeter: {P}, Area: {S}")

def process_matrix(file_name):
    """
    Зовнішня функція без параметрів.
    Викликає внутрішню функцію для обробки матриці зчитаної з файлу.
    """
    matrix = read_matrix_from_file(file_name)
    
    if matrix is not None:
        row_number = find_row_with_equal_positive_negative(matrix)
        print("Номер першого рядка з однаковою кількістю додатних і від'ємних елементів:", row_number)
        
        if row_number != 0:
            transformed_matrix = elementwise_quotient(matrix)
            print("Результат поелементної частки матриці:")
            print(transformed_matrix)

def read_matrix_from_file(file_name):
    """
    Внутрішня функція для зчитування матриці з файлу.
    Повертає матрицю або None, якщо файл не існує або має некоректний формат.
    """
    try:
        matrix = np.loadtxt(file_name, dtype=int)
        return matrix
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except ValueError:
        print(f"Некоректний формат даних у файлі '{file_name}'.")
    return None

def find_row_with_equal_positive_negative(matrix):
    """
    Внутрішня функція для знаходження номера рядка із
    однаковою кількістю додатних і від'ємних елементів.
    Повертає номер рядка або 0, якщо немає відповідних рядків.
    """
    for i, row in enumerate(matrix):
        positive_count = np.sum(row > 0)
        negative_count = np.sum(row < 0)
        
        if positive_count == negative_count:
            return i + 1  # Нумерація рядків починається з 1
            
    return 0

def elementwise_quotient(matrix):
    """
    Внутрішня функція для знаходження поелементної частки матриці
    на випадковою матриці того ж розміру, заповненою випадковими числами.
    """
    random_matrix = np.random.randint(1, 10, size=matrix.shape)
    return np.divide(matrix, random_matrix)