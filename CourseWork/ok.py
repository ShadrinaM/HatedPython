import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread("image211.jpg")

# Преобразование в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск границ с помощью Canny
edges = cv2.Canny(gray, 50, 150)

# Поиск контуров
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Поиск наибольшего контура (предполагаем, что это доска)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
board_contour = contours[0]

# Аппроксимация контура до четырехугольника
epsilon = 0.02 * cv2.arcLength(board_contour, True)
approx = cv2.approxPolyDP(board_contour, epsilon, True)

# Убедимся, что найдено 4 угла
if len(approx) == 4:
    # Сортируем углы для задания порядка (верхний левый, верхний правый, нижний правый, нижний левый)
    points = sorted(approx.reshape(4, 2), key=lambda x: (x[1], x[0]))  # Сортируем по Y, затем по X
    top_points = sorted(points[:2], key=lambda x: x[0])  # Верхние точки по X
    bottom_points = sorted(points[2:], key=lambda x: x[0])  # Нижние точки по X
    ordered_points = np.array([top_points[0], top_points[1], bottom_points[1], bottom_points[0]], dtype="float32")
    
    # Задаем размеры выровненного изображения (например, ширина и высота учебной доски)
    width = 800
    height = 600
    dest_points = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype="float32")

    # Вычисляем матрицу перспективного преобразования
    matrix = cv2.getPerspectiveTransform(ordered_points, dest_points)

    # Применяем преобразование
    warped = cv2.warpPerspective(image, matrix, (width, height))

    # Сохраняем результат
    cv2.imshow("Warped Board", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Не удалось обнаружить 4 угла доски.")
