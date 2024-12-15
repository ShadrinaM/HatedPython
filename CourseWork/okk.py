import cv2
import numpy as np

def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open video camera")
        return

    while True:
        ret, original = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Create windows
        cv2.namedWindow("Original")
        cv2.namedWindow("Red Colour Detect, GreyScale")
        cv2.namedWindow("Processing")

        # Filter red color
        bw = cv2.inRange(original, (0, 0, 125), (80, 80, 256))

        # Image processing: blur, erode, dilate
        bw = cv2.GaussianBlur(bw, (15, 15), 1.5)
        bw = cv2.erode(bw, None)
        bw = cv2.dilate(bw, None, iterations=10)

        # Edge detection using Canny
        processing = cv2.Canny(bw, 0, 30, 3)

        # Detect lines using Hough Transform
        lines = cv2.HoughLines(processing, 1, np.pi / 180, 100)

        if lines is not None:
            # Convert lines from polar to cartesian and draw them
            pt1, pt2 = [], []
            for rho_theta in lines:
                rho, theta = rho_theta[0]
                a, b = np.cos(theta), np.sin(theta)
                x0, y0 = a * rho, b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                pt1.append((x1, y1))
                pt2.append((x2, y2))
                cv2.line(original, (x1, y1), (x2, y2), (255, 255, 0), 2)

            # Find perpendicular intersecting lines
            f1, f2 = [], []
            for i, (p1_start, p2_start) in enumerate(zip(pt1, pt2)):
                for j, (p1_next, p2_next) in enumerate(zip(pt1, pt2)):
                    if i >= j:
                        continue

                    # Calculate gradients
                    denom1 = p2_start[0] - p1_start[0] or 0.00001
                    denom2 = p2_next[0] - p1_next[0] or 0.00001
                    m1 = (p2_start[1] - p1_start[1]) / denom1
                    m2 = (p2_next[1] - p1_next[1]) / denom2
                    m3 = -m1 * m2

                    if 0.1 < m3 < 4.0:
                        f1.extend([p1_start, p1_next])
                        f2.extend([p2_start, p2_next])

            # Remove duplicates
            f1, f2 = list(dict.fromkeys(f1)), list(dict.fromkeys(f2))

            # Find intersection points
            points = []
            for i, (f1_start, f2_start) in enumerate(zip(f1, f2)):
                for j, (f1_next, f2_next) in enumerate(zip(f1, f2)):
                    if i >= j:
                        continue

                    denom = ((f1_next[0] - f2_next[0]) * (f1_start[1] - f2_start[1]) -
                             (f1_next[1] - f2_next[1]) * (f1_start[0] - f2_start[0]) or 0.00001)
                    numer_x = ((f1_start[0] * f2_start[1] - f1_start[1] * f2_start[0]) * (f1_next[0] - f2_next[0]) -
                               (f1_start[0] - f2_start[0]) * (f1_next[0] * f2_next[1] - f1_next[1] * f2_next[0]))
                    numer_y = ((f1_start[0] * f2_start[1] - f1_start[1] * f2_start[0]) * (f1_next[1] - f2_next[1]) -
                               (f1_start[1] - f2_start[1]) * (f1_next[0] * f2_next[1] - f1_next[1] * f2_next[0]))
                    px, py = numer_x / denom, numer_y / denom

                    if 0 <= px <= original.shape[1] and 0 <= py <= original.shape[0]:
                        points.append((int(px), int(py)))

            # Remove duplicate points
            points = list(dict.fromkeys(points))

            for point in points:
                cv2.circle(original, point, 3, (255, 0, 0), 3)

            # Calculate the rectangle's center
            if points:
                x_coords = [p[0] for p in points]
                y_coords = [p[1] for p in points]
                xmin, xmax = min(x_coords), max(x_coords)
                ymin, ymax = min(y_coords), max(y_coords)
                center_x, center_y = (xmax + xmin) // 2, (ymax + ymin) // 2
                cv2.circle(original, (center_x, center_y), 10, (0, 0, 0), 3)
                print(f"Centre X = {center_x}, Centre Y = {center_y}")

        # Display results
        cv2.imshow("Original", original)
        cv2.imshow("Processing", processing)
        cv2.imshow("Red Colour Detect, GreyScale", bw)

        # Exit on 'ESC'
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
