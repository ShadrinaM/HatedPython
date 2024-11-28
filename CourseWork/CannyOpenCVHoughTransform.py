# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Загрузка изображения
# # image = cv2.imread('image22.jpg', cv2.IMREAD_GRAYSCALE)

# # # Шаг 1: Сглаживание изображения (Gaussian Blur)
# # blurred = cv2.GaussianBlur(image, (5, 5), 1.4)

# # # Шаг 2: Применение алгоритма Canny
# # edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# # # Шаг 3: Применение Hough Transform для нахождения прямых
# # # Hough Transform находит линии, заданные параметрами (ρ, θ)
# # lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# # # Отображение результатов
# # plt.figure(figsize=(10, 6))

# # # 1. Исходное изображение с границами
# # plt.subplot(1, 2, 1)
# # plt.title("Выделенные границы (Canny)")
# # plt.imshow(edges, cmap='gray')
# # plt.axis('off')

# # # 2. Применение Hough Transform и отображение линий
# # plt.subplot(1, 2, 2)
# # plt.title("Прямые, найденные Hough Transform")
# # plt.imshow(edges, cmap='gray')

# # # Отображаем найденные линии на изображении
# # if lines is not None:
# #     for line in lines:
# #         rho, theta = line[0]
# #         # Вычисление координат точек на изображении для каждой линии
# #         a = np.cos(theta)
# #         b = np.sin(theta)
# #         x0 = a * rho
# #         y0 = b * rho
# #         x1 = int(x0 + 1000 * (-b))
# #         y1 = int(y0 + 1000 * (a))
# #         x2 = int(x0 - 1000 * (-b))
# #         y2 = int(y0 - 1000 * (a))

# #         # Рисуем найденные прямые
# #         plt.plot([x1, x2], [y1, y2], color='red', linewidth=2)

# # plt.axis('off')
# # plt.tight_layout()
# # plt.show()










# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Загрузка изображения
# # image = cv2.imread('image27.jpg', cv2.IMREAD_GRAYSCALE)

# # # Шаг 1: Уменьшение размытия (Gaussian Blur)
# # # Уменьшаем размер ядра и стандартное отклонение для более слабого размытия
# # blurred = cv2.GaussianBlur(image, (9, 9), 2.0)  # Уменьшено ядро и стандартное отклонение

# # # Шаг 2: Применение алгоритма Canny
# # edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# # # Шаг 3: Применение Hough Transform для нахождения прямых
# # lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# # # Отображение результатов
# # plt.figure(figsize=(12, 8))

# # # 1. Исходное изображение
# # plt.subplot(1, 3, 1)
# # plt.title("Исходное изображение")
# # plt.imshow(image, cmap='gray')
# # plt.axis('off')

# # # 2. Выделенные границы (Canny)
# # plt.subplot(1, 3, 2)
# # plt.title("Выделенные границы (Canny)")
# # plt.imshow(edges, cmap='gray')
# # plt.axis('off')

# # # 3. Применение Hough Transform и отображение линий
# # plt.subplot(1, 3, 3)
# # plt.title("Прямые, найденные Hough Transform")
# # plt.imshow(edges, cmap='gray')

# # # Отображаем найденные линии на изображении
# # if lines is not None:
# #     for line in lines:
# #         rho, theta = line[0]
# #         # Вычисление координат точек на изображении для каждой линии
# #         a = np.cos(theta)
# #         b = np.sin(theta)
# #         x0 = a * rho
# #         y0 = b * rho
# #         x1 = int(x0 + 1000 * (-b))
# #         y1 = int(y0 + 1000 * (a))
# #         x2 = int(x0 - 1000 * (-b))
# #         y2 = int(y0 - 1000 * (a))

# #         # Рисуем найденные прямые
# #         plt.plot([x1, x2], [y1, y2], color='red', linewidth=2)

# # plt.axis('off')
# # plt.tight_layout()
# # plt.show()








import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения
image = cv2.imread('image26.jpg', cv2.IMREAD_GRAYSCALE)

# Шаг 1: Изначальное размытие с меньшим ядром
blurred = cv2.GaussianBlur(image, (9, 9), 2.0)

# Шаг 2: Применение алгоритма Canny
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Шаг 3: Применение Hough Transform для нахождения прямых
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Подсчитываем количество линий
line_count = 0
if lines is not None:
    line_count = len(lines)

# Если количество найденных линий слишком большое, увеличиваем размытие
if line_count > 10:  # Пороговое значение для количества линий (вы можете настроить его)
    print(f"Найдено {line_count} линий, увеличиваем размытие.")
    blurred = cv2.GaussianBlur(image, (15, 15), 3.0)  # Увеличиваем размытие
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)  # Перезапуск Canny

    # Повторно применяем Hough Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Отображение результатов
plt.figure(figsize=(12, 8))

# 1. Исходное изображение
plt.subplot(1, 3, 1)
plt.title("Исходное изображение")
plt.imshow(image, cmap='gray')
plt.axis('off')

# 2. Выделенные границы (Canny)
plt.subplot(1, 3, 2)
plt.title("Выделенные границы (Canny)")
plt.imshow(edges, cmap='gray')
plt.axis('off')

# 3. Применение Hough Transform и отображение линий
plt.subplot(1, 3, 3)
plt.title("Прямые, найденные Hough Transform")
plt.imshow(edges, cmap='gray')

# Отображаем найденные линии на изображении
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        # Вычисление координат точек на изображении для каждой линии
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # Рисуем найденные прямые
        plt.plot([x1, x2], [y1, y2], color='red', linewidth=2)

plt.axis('off')
plt.tight_layout()
plt.show()








