#  & "C:/Users/MM Shadrina/AppData/Local/Programs/Python/Python312/python.exe" "D:\Фото-видео файлы  оригинал\Учёба\Учёба ВУЗ\Githubproject\HatedPython\CourseWork\CannyOpenCV.py"
# D:
# cd "D:/Фото-видео файлы оригинал/Учёба/Учёба ВУЗ/Githubproject/HatedPython/CourseWork"

# python CannyOpenCV.py

import cv2
# pip install opencv-python
import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib


# Загрузка изображения
image = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Шаг 1: Сглаживание изображения (Gaussian Blur)
blurred = cv2.GaussianBlur(image, (5, 5), 1.4)

# Шаг 2: Применение алгоритма Canny
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Отображение результата
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title("Исходное изображение")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Выделенные границы (Canny)")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
