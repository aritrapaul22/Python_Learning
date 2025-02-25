import os, cv2


def detect_faces():
    image = cv2.imread('images/humans.jpeg', 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)

    faces = face_cascade.detectMultiScale(image, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 255), 4)

    cv2.imwrite('humans_detected.jpeg', image)

def has_faces(image_face):
    image = cv2.imread(f"{INPUT_FOLDER}/{image_face}", 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)

    faces = face_cascade.detectMultiScale(image, SCALE, NEIGHBORS)
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), COLOR, WIDTH)

        return image

def watermark_image(image_water):
    image = cv2.imread(f"{INPUT_FOLDER}/{image_water}", 1)
    watermark = cv2.imread('watermark.jpeg')

    x = image.shape[1] - watermark.shape[1]
    y = image.shape[0] - watermark.shape[0]

    watermark_place = image[x:, y:]
    cv2.imwrite('watermark_place.jpeg', watermark_place)

    blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
    # watermarked = cv2.imwrite('blend.jpeg', blend)

    return blend


if __name__ == '__main__':
    CASCADE = 'haarcascade_frontalface_default.xml'
    INPUT_FOLDER = 'images'
    OUTPUT_FOLDER = 'converted_images'
    COLOR = (255, 255, 255)
    WIDTH = 4
    SCALE = 1.1
    NEIGHBORS = 4

    # detect_faces()

    # for image_path in os.listdir(INPUT_FOLDER):
    #     face_image = has_faces(f'{INPUT_FOLDER}/{image_path}')
    #     if face_image is not None:
    #         cv2.imwrite(f'{OUTPUT_FOLDER}/{image_path}', face_image)

    # for image_path in os.listdir(INPUT_FOLDER):
    #     final = watermark_image(image_path)
    #     if final is not None:
    #         cv2.imwrite(f'{OUTPUT_FOLDER}/{image_path}', final)
    """Not working as watermark is bigger"""

