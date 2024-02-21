from PIL import Image,ImageDraw
from PIL import ImageOps
from PIL import ImageFilter
import argparse

# image = Image.open("cat_image.jpg")
# print(image.format)
# new_image = image.rotate(30)
# new_image.save("new_image.jpg")
# image.save("image_test.png", "png")

# img = Image.new('RGBA', (91, 91), 'white')
# draw = ImageDraw.Draw(img)
# draw.ellipse((0, 0, 90, 90), 'yellow', 'blue')
# draw.ellipse((25, 20, 35, 30), 'yellow', 'blue')
# draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
# draw.arc((20, 40, 70, 70), 0, 180, 0)
# img.save('draw-smile.png')



def apply_bw_filter(photo):
    photo = photo.convert('L')
    photo.save("bw_photo.jpg")


def apply_contrast_filter(photo):
    photo = ImageOps.autocontrast(photo, cutoff = 10)
    photo.save("contrast_photo.jpg")


def apply_blur_filter(photo):
    photo = photo.filter(ImageFilter.GaussianBlur(radius = 2.4))
    photo.save("blur_photo.jpg")


def apply_noise_filter(photo):
    photo = photo.filter(ImageFilter.MedianFilter(size = 9))
    photo.save("noise_photo.jpg")


def apply_border_filter(photo):
    width, height = photo.size
    photo = photo.transform((width + 100, height + 100), Image.EXTENT,
        (-10, -10, width + 10, height + 10), Image.BILINEAR)
    photo.save("border_photo.jpg")


def apply_sepia_filter(photo):
    sepia_r, sepia_g, sepia_b = (112, 66, 20)
    sepia_image = Image.new('RGB', photo.size)
    for x in range(photo.width):
        for y in range(photo.height):
            r, g, b = photo.getpixel((x,y))
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            sepia_r, sepia_g, sepia_b = (min(new_r, 255), min(new_g, 255), min(new_b, 255))
            sepia_image.putpixel((x,y), (sepia_r, sepia_g, sepia_b))
    sepia_image.save("sepia_photo.jpg")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="Получить название файла")
    args = parser.parse_args() 
    print('Название файла:', args.file_name)
    

    parser.add_argument("--bw_photo", action="store_true", help="чёрно-белый фильтр")
    
    args = parser.parse_args() 
    if args.bw_photo:
        print(f"Использование черно-белого фильтра:  {args.bw_photo}")
    else:
        print(f"Использование черно-белого фильтра:  {args.bw_photo}")

    parser.add_argument("--contrast_photo", action="store_true", help="контрастный фильтр")
    
    args = parser.parse_args() 
    if args.contrast_photo:
        print(f"Использование контрастного фильтра:  {args.contrast_photo}")
    else:
        print(f"Использование контрастного фильтра:  {args.contrast_photo}")

    parser.add_argument("--blur_photo", action="store_true", help="размытие фильтр")
    
    args = parser.parse_args() 
    if args.blur_photo:
        print(f"Использование фильтра размытия:  {args.blur_photo}")
    else:
        print(f"Использование фильтра размытия:  {args.blur_photo}")

    parser.add_argument("--noise_photo", action="store_true", help="медианный фильтр")
    
    args = parser.parse_args() 
    if args.noise_photo:
        print(f"Использование медианного фильтра:  {args.noise_photo}")
    else:
        print(f"Использование медианного фильтра:  {args.noise_photo}")

    parser.add_argument("--border_photo", action="store_true", help="фильтр рамки")
    
    args = parser.parse_args() 
    if args.border_photo:
        print(f"Использование рамки:  {args.border_photo}")
    else:
        print(f"Использование рамки:  {args.border_photo}")

    parser.add_argument("--sepia_photo", action="store_true", help="фильтр сепии")
    
    args = parser.parse_args() 
    if args.sepia_photo:
        print(f"Использование фильтра сепии:  {args.sepia_photo}")
    else:
        print(f"Использование фильтра сепии:  {args.sepia_photo}")

    original_photo = Image.open(f"{args.file_name}")
    filter_list = [
        apply_bw_filter,
        apply_contrast_filter,
        apply_blur_filter,
        apply_noise_filter,
        apply_border_filter,
        apply_sepia_filter
]
    for filter in filter_list:
        filter(original_photo)
    print("успешно")

if __name__ == "__main__":
    main()

#python main.py --file_name "photo_1.jpg"








