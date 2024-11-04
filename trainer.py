import os
import cv2
import numpy as np
from PIL import Image

# Initialize recognizer correctly
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"


def get_images_with_id(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []

    for single_image_path in image_paths:
        # Load image and convert to grayscale
        faceImg = Image.open(single_image_path).convert('L')
        faceNp = np.array(faceImg, np.uint8)

        # Extract ID from the filename
        id = int(os.path.split(single_image_path)[-1].split('.')[1])
        faces.append(faceNp)
        ids.append(id)

    return np.array(ids, dtype=np.int32), faces


# Get ids and faces, ensuring correct types
ids, faces = get_images_with_id(path)


# Train the recognizer and save the training data
try:
    recognizer.train(faces, ids)
    recognizer.save('recognizer/trainingdata.yml')
    print("Training completed and data saved successfully.")
except cv2.error as e:
    print(f"OpenCV Error: {e}")

cv2.destroyAllWindows()
