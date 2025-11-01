import requests
import numpy as np
import cv2

# ✅ Use the correct IP from IP Webcam app
url = url = 'http://<your-ip-address>:8080'  # Replace <your-ip-address> with your phone's IP

while True:
    try:
        response = requests.get(url, timeout=2)
        video = np.array(bytearray(response.content), dtype=np.uint8)
        render = cv2.imdecode(video, -1)
        if render is not None:
            cv2.imshow('frame', render)
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
