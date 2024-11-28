import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения
image = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Шаг 1: Сглаживание изображения
blurred = cv2.GaussianBlur(image, (5, 5), 1.4)

# Шаг 2: Вычисление градиентов (Собелевские фильтры)
Gx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)  # Горизонтальный градиент
Gy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)  # Вертикальный градиент

# Вычисление магнитуды градиента и направления
magnitude = np.sqrt(Gx**2 + Gy**2)
direction = np.arctan2(Gy, Gx)

# Нормализация магнитуды
magnitude = (magnitude / magnitude.max()) * 255
magnitude = magnitude.astype(np.uint8)

# Шаг 3: Подавление немаксимумов
def non_max_suppression(magnitude, direction):
    rows, cols = magnitude.shape
    suppressed = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = direction[i, j] * 180.0 / np.pi  # Преобразуем в градусы
            angle = angle % 180  # Убедимся, что угол в диапазоне [0, 180]

            # Определяем направление (0, 45, 90, 135)
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                neighbors = [magnitude[i, j - 1], magnitude[i, j + 1]]
            elif 22.5 <= angle < 67.5:
                neighbors = [magnitude[i - 1, j + 1], magnitude[i + 1, j - 1]]
            elif 67.5 <= angle < 112.5:
                neighbors = [magnitude[i - 1, j], magnitude[i + 1, j]]
            else:  # 112.5 <= angle < 157.5
                neighbors = [magnitude[i - 1, j - 1], magnitude[i + 1, j + 1]]

            # Подавляем пиксель, если он не максимален
            if magnitude[i, j] >= max(neighbors):
                suppressed[i, j] = magnitude[i, j]

    return suppressed

suppressed = non_max_suppression(magnitude, direction)

# Шаг 4: Двойная пороговая фильтрация
low_threshold = 50
high_threshold = 150

strong_edges = (suppressed >= high_threshold).astype(np.uint8)
weak_edges = ((suppressed >= low_threshold) & (suppressed < high_threshold)).astype(np.uint8)

# Финальная обработка гистерезисом
def edge_tracking(strong_edges, weak_edges):
    rows, cols = strong_edges.shape
    edges = np.copy(strong_edges)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if weak_edges[i, j] and np.any(strong_edges[i-1:i+2, j-1:j+2]):
                edges[i, j] = 1

    return edges

final_edges = edge_tracking(strong_edges, weak_edges)

# Отображение результатов
plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.title("Магнитуда градиента")
plt.imshow(magnitude, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Подавление немаксимумов")
plt.imshow(suppressed, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Итоговые границы (Canny)")
plt.imshow(final_edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
