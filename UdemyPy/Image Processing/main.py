import cv2, os


def greyscale():
    color = cv2.imread('images/galaxy.jpeg', 0)
    cv2.imwrite('converted_images/galaxy-gray.jpeg', color)

def convert_multiple_images():
    images = os.listdir('images')
    for item in images:
        gray = cv2.imread(f'images/{item}', 0)
        cv2.imwrite(f'converted_images/gray-{item}', gray)

def resize(image_path, scale, resized_path):
    image = cv2.imread(image_path)
    im_height = image.shape[1]
    im_width = image.shape[0]
    rs_scale = scale/100
    new_dim = int(im_height * rs_scale), int(im_width * rs_scale)
    rs_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, rs_image)

if __name__ == '__main__':
    convert_multiple_images()
    image_path = 'images/galaxy.jpeg'
    resized_path = 'converted_images/resized-galaxy.jpeg'
    resize(image_path, 10, resized_path)
