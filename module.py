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

def process_matrix():
    # Зчитування матриці з файлу
    matrix = np.loadtxt('input_matrix.txt', dtype=int)

    # Знаходження номеру рядка
    row_number = find_row(matrix)

    # Виведення результату
    if row_number == 0:
        print("Не знайдено рядків з однаковою кількістю додатних і від'ємних елементів.")
    else:
        print(f"Номер першого рядка з однаковою кількістю додатних і від'ємних елементів: {row_number}")

    # Знаходження поелементної частки
    result_matrix = divide_matrix(matrix)

    # Збереження результату у файл
    np.savetxt('output_matrix.txt', result_matrix, fmt='%d')

def find_row(matrix):
    for i, row in enumerate(matrix):
        positive_count = np.count_nonzero(row > 0)
        negative_count = np.count_nonzero(row < 0)

        if positive_count == negative_count:
            return i + 1  # Повертаємо номер рядка (індекс + 1), бо індексація зазвичай починається з 0

    return 0  # Якщо не знайдено рядків з однаковою кількістю додатних і від'ємних елементів

def divide_matrix(matrix):
    random_matrix = np.random.randint(1, 10, size=matrix.shape)  # Заповнюємо випадковою матрицею

    # Захист від ділення на нуль
    random_matrix[random_matrix == 0] = 1

    return matrix / random_matrix
