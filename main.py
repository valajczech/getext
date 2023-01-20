import cv2
from PIL import Image
import pytesseract
import os

directory = "./images"


def loadImagesFromFolder(folder):
    print("Nacitani souboru ve slozce" + folder)
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    print("Dokonceno, startuji generaci textu pomoci openCV.")
    return images


def generateTextFromImage(image):
    f = open("output.txt", "a")
    content = "\n" + pytesseract.image_to_string(image)
    f.write(content)
    f.close
    print("Strana vygenerovana.")


if __name__ == "__main__":
    images = loadImagesFromFolder(directory)

    for image in images:
        generateTextFromImage(image)
