# import cv2
# import numpy as np

# # Путь к изображению
# image_path = "image26.jpg"

# # Загружаем изображение
# Original = cv2.imread(image_path)
# if Original is None:
#     print("Не удалось загрузить изображение. Проверьте путь к файлу.")
#     exit()

# # Создаем окна для отображения
# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Red Colour Detect, GreyScale", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Processing", cv2.WINDOW_NORMAL)

# # Цветовая фильтрация
# BW = cv2.inRange(Original, (0, 0, 125), (80, 80, 256))  # Фильтрация красного цвета

# # Обработка изображения
# BW = cv2.GaussianBlur(BW, (15, 15), 1.5)
# BW = cv2.erode(BW, None)
# BW = cv2.dilate(BW, None, iterations=10)

# # Выявление границ с использованием Canny
# Processing = cv2.Canny(BW, 0, 30, apertureSize=3)

# # Выявление линий с помощью HoughLines
# lines = cv2.HoughLines(Processing, 1, np.pi / 180, 100)

# if lines is not None:
#     print(f"{len(lines)} линии обнаружено.")
    
#     # Перевод из полярных в декартовы координаты
#     points = []
#     for rho, theta in lines[:, 0]:
#         a, b = np.cos(theta), np.sin(theta)
#         x0, y0 = a * rho, b * rho
#         pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
#         pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
#         points.append((pt1, pt2))
#         cv2.line(Original, pt1, pt2, (255, 255, 0), 2)

#     # Определение пересечений и поиск центра прямоугольника
#     intersections = []
#     for i, (pt1_start, pt2_start) in enumerate(points[:-1]):
#         for pt1_next, pt2_next in points[i+1:]:
#             denom = (pt1_start[0] - pt2_start[0]) * (pt1_next[1] - pt2_next[1]) - \
#                     (pt1_start[1] - pt2_start[1]) * (pt1_next[0] - pt2_next[0])
#             if denom == 0:
#                 continue
#             numer_x = ((pt1_start[0] * pt2_start[1] - pt1_start[1] * pt2_start[0]) * (pt1_next[0] - pt2_next[0]) - 
#                        (pt1_start[0] - pt2_start[0]) * (pt1_next[0] * pt2_next[1] - pt1_next[1] * pt2_next[0]))
#             numer_y = ((pt1_start[0] * pt2_start[1] - pt1_start[1] * pt2_start[0]) * (pt1_next[1] - pt2_next[1]) - 
#                        (pt1_start[1] - pt2_start[1]) * (pt1_next[0] * pt2_next[1] - pt1_next[1] * pt2_next[0]))
#             x = numer_x / denom
#             y = numer_y / denom
#             intersections.append((int(x), int(y)))

#     if intersections:
#         for x, y in intersections:
#             cv2.circle(Original, (x, y), 5, (255, 0, 0), -1)

#         # Найдем центр прямоугольника
#         xs = [p[0] for p in intersections]
#         ys = [p[1] for p in intersections]
#         Cx = sum(xs) // len(xs)
#         Cy = sum(ys) // len(ys)
#         cv2.circle(Original, (Cx, Cy), 10, (0, 255, 0), -1)
#         print(f"Центр прямоугольника: ({Cx}, {Cy})")

# # Отображение результатов
# cv2.imshow("Original", Original)
# cv2.imshow("Red Colour Detect, GreyScale", BW)
# cv2.imshow("Processing", Processing)

# # Ожидание нажатия клавиши
# cv2.waitKey(0)
# cv2.destroyAllWindows()







import cv2
import numpy as np

# Путь к изображению
image_path = "image26.jpg"

# Загружаем изображение
Original = cv2.imread(image_path)
if Original is None:
    print("Не удалось загрузить изображение. Проверьте путь к файлу.")
    exit()

# Цветовая фильтрация
BW = cv2.inRange(Original, (0, 0, 125), (80, 80, 256))  # Фильтрация красного цвета

# Обработка изображения
BW = cv2.GaussianBlur(BW, (15, 15), 1.5)
BW = cv2.erode(BW, None)
BW = cv2.dilate(BW, None, iterations=10)

# Выявление границ с использованием Canny
Processing = cv2.Canny(BW, 0, 30, apertureSize=3)

# Накладываем выделенные границы на оригинальное изображение
Contours_Overlay = Original.copy()
Contours_Overlay[Processing > 0] = [0, 255, 0]  # Зеленый цвет для границ

# Создаем объединенное изображение
combined_image = np.hstack((Original, Contours_Overlay))

# Отображение результатов в одном окне
cv2.imshow("Original and Contours", combined_image)

# Ожидание нажатия клавиши
cv2.waitKey(0)
cv2.destroyAllWindows()
