Uz/Eng

# Yuzni Tanib Olish uchun Mashg‘ulot Loyihasi

Ushbu loyiha OpenCV yordamida LBPH yuz tanish modelini yaratadi. Tizim yuz rasmlaridan iborat datasetni mashg'ulot uchun ishlatadi, har bir rasmni unikal ID bilan bog'laydi va o'rgatilgan modelni kelajakdagi yuz tanish vazifalari uchun saqlaydi.

 Xususiyatlari

- Yuzni aniqlash va mashg'ulot: Yuz rasmlarini `dataset` papkasidan yuklab, ularni kulrang formatga o‘tkazadi va yuz tanish modelini o‘rgatadi.
- Modelni saqlash: O‘rgatilgan modelni `.yml` formatida saqlaydi va uni qayta ishlatish imkoniyatini beradi.
- Moslashuvchan dataset: Yuz rasmlarini oson qo'shib, mashg'ulot uchun foydalanish mumkin.

 Talablar

Loyihani ishga tushirishdan oldin quyidagi kutubxonalar o‘rnatilganligiga ishonch hosil qiling:

- Python 3.x
- OpenCV (`opencv-contrib-python` LBPH yuz tanish funksiyasi uchun)
- Pillow (tasvirlar bilan ishlash uchun)
- Numpy (hisoblash amallari uchun)

Kutubxonalarni o'rnatish:

```bash
pip install opencv-contrib-python pillow numpy
```

 Loyihaning Tuzilishi

- `dataset/`: Yuz rasmlari joylashgan katalog. Rasmlar `person.[ID].jpg` formatida nomlangan bo'lishi kerak, bunda `ID` har bir shaxs uchun noyob raqam bo‘ladi.
- `trainer.py`: `dataset` papkasidagi rasmlar yordamida yuzni tanish modelini o‘rgatish uchun asosiy skript.
- `recognizer/trainingdata.yml`: O‘rgatilgan model saqlanadigan fayl.

 Boshlang‘ich Sozlamalar

1. Datasetni tayyorlang:
   - Barcha mashg‘ulot rasmlarini `dataset/` papkasiga joylang.
   - Har bir rasm `person.[ID].jpg` shaklida nomlangan bo‘lishi kerak, bunda `ID` har bir shaxs uchun noyob raqam (masalan, `person.1.jpg`, `person.2.jpg`).

2. Mashg'ulot Skriptini Ishga Tushiring:
   Mashg'ulot skriptini ishga tushiring va modelni yarating:

   ```bash
   python trainer.py
   ```

3. Natijalarni Tekshiring:
   - Mashg'ulotdan so'ng, `recognizer/trainingdata.yml` fayli yaratiladi.
   - Ushbu fayl keyingi yuz tanish skriptlarida foydalanish uchun tayyor bo‘ladi.

 Kodga Umumiy Ko'rinish

Asosiy kod (`trainer.py`) quyidagicha ishlaydi:

1. Tasvirlarni Yuklash va Qayta Ishlash:
   - Har bir rasmni `dataset/` papkasidan yuklaydi va ID raqamni ajratadi.
2. Mashg‘ulot:
   - OpenCV `LBPH` yuz tanish funksiyasi yordamida tasvirlarni va ularga mos keluvchi IDlarni o‘rgatadi.
3. Modelni Saqlash:
   - O‘rgatilgan model `recognizer/trainingdata.yml` fayliga saqlanadi.

 Foydalanish Bo'yicha Misol

Model o‘rgatilgach, u yangi rasmlarda yuzlarni tanish vazifalarida foydalanish uchun yuklanishi mumkin.

 Muammolarni Tuzatish

- "Unknown C++ exception" xatosi: Rasmlar kulrang formatda va bir xil o'lchamda ekanligiga ishonch hosil qiling. `cv2.face.LBPHFaceRecognizer_create()` funksiyasi to‘g‘ri ishlatilganligiga e’tibor bering.
- Ma'lumotlarni Moslashtirish: `faces` va `ids` massivlari `np.uint8` va `np.int32` formatida ekanligini tekshiring.

 Hissa Qo'shish

Muammolarni xabar qilish, loyihani `fork` qilish va yaxshilash uchun `pull request`lar jo‘natishdan ozod foydalanishingiz mumkin.

===================================================================================================================================================================================================================================

Face Recognition Training Project

This project implements a Face Recognition System using Python and OpenCV’s LBPH Face Recognizer. The system trains on a dataset of face images, associates each image with a unique ID, 
and saves the trained model for future use in recognition tasks.

Features
•	Face Detection and Training: Processes face images from a dataset, converts them to grayscale, and trains a face recognition model.
•	Model Persistence: Saves trained data in a .yml file, making it reusable for face recognition applications.
•	Flexible Dataset Input: Supports easy addition of face images with IDs for training.

Requirements
Before running the project, make sure you have the following libraries installed:
•	Python 3.x
•	OpenCV (with opencv-contrib-python for face recognizer support)
•	Pillow for image handling
•	Numpy for numerical operations

Install the required libraries:
pip install opencv-contrib-python pillow numpy

Project Structure
•	dataset/: Directory where face images are stored. Images should be named in the format person.[ID].jpg, where ID is a unique identifier for each person.
•	trainer.py: Main script for training the face recognizer using images from the dataset folder.
•	recognizer/trainingdata.yml: File where the trained model is saved.

Getting Started
1.	Prepare the Dataset:
Place all training images in the dataset/ folder.
Each image should follow the naming convention person.[ID].jpg, where ID is a unique integer for each person (e.g., person.1.jpg, person.2.jpg).
2.	Run the Training Script: Execute the training script to generate the trained model:
python trainer.py
3.	Check for Output:
After training, recognizer/trainingdata.yml will be generated.
This file can be used by other scripts to recognize faces based on the trained data.

Code Overview
The main code (trainer.py) works as follows:
1.	Image Loading and Processing:
Loads each image in grayscale format from dataset/ and extracts the person’s ID.
2.	Training:
Uses OpenCV’s LBPH face recognizer to train on the images and labels.
3.	Saving the Model:
Saves the trained recognizer model in recognizer/trainingdata.yml for later use.

Example Usage
Once the model is trained, it can be loaded into another script for face recognition tasks like verifying or identifying faces in new images.

Troubleshooting
•	Unknown C++ exception: Ensure images are in grayscale and have consistent dimensions. The correct function to initialize the recognizer is cv2.face.LBPHFaceRecognizer_create().
•	Data Compatibility: Ensure faces and ids are numpy arrays of np.uint8 and np.int32 types, respectively.

Contributing
Feel free to submit issues, fork the repository, and make pull requests to improve the project.
