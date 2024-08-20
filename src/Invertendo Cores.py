import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Cor vermelha
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    # Cor azul
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    
    # Cor verde
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    
    # Criar imagens substitutas para as cores detectadas
    red_substitute = np.zeros_like(frame)
    blue_substitute = np.zeros_like(frame)
    green_substitute = np.zeros_like(frame)
    
    # Definir cores substitutas em BGR
    red_color = [0, 255, 0]      # Verde em BGR
    blue_color = [0, 0, 255]     # Azul em BGR
    green_color = [255, 0, 0]    # Vermelho em BGR
    
    # Aplicar cores substitutas
    red_substitute[red_mask > 0] = red_color
    blue_substitute[blue_mask > 0] = blue_color
    green_substitute[green_mask > 0] = green_color
    
    # Combinar imagens substitutas
    combined_substitutes = cv2.bitwise_or(red_substitute, blue_substitute)
    combined_substitutes = cv2.bitwise_or(combined_substitutes, green_substitute)
    
    # Mostrar as imagens
    cv2.imshow("Frame", frame)
    cv2.imshow("Substituted Colors", combined_substitutes)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
