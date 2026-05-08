import cv2
import matplotlib.pyplot as plt

img1_path = "data/mision.jpg"
img2_path = "data/oscura.jpg"

# cargar las imágenes
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

if img1 is not None and img2 is not None:
    # escala de grises para el análisis de brillo
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

     # figura comparativa
    plt.figure(figsize=(12, 8))

    # --- IMAGEN CLARA ---
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Imagen Clara (Misión)")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.hist(gray1.flatten(), bins=50, color='blue', alpha=0.7)
    plt.title("Histograma Clara (Cargado a la derecha)")

    # --- IMAGEN OSCURA ---
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title("Imagen Oscura (Niño)")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.hist(gray2.flatten(), bins=50, color='gray', alpha=0.7)
    plt.title("Histograma Oscura (Cargado a la izquierda)")

    plt.tight_layout()
    plt.show()
else:
    if img1 is None: print(f"Error: No se encontró {img1_path}")
    if img2 is None: print(f"Error: No se encontró {img2_path}")