from PIL import Image,ImageDraw
from PIL import ImageOps
from PIL import ImageFilter
import argparse

def apply_bw_filter(photo):
    photo = photo.convert('L')
    photo.save("image/bw_photo.jpg")


def apply_contrast_filter(photo):
    photo = ImageOps.autocontrast(photo, cutoff = 10)
    photo.save("image/contrast_photo.jpg")


def apply_blur_filter(photo):
    photo = photo.filter(ImageFilter.GaussianBlur(radius = 2.4))
    photo.save("image/blur_photo.jpg")


def apply_noise_filter(photo):
    photo = photo.filter(ImageFilter.MedianFilter(size = 9))
    photo.save("image/noise_photo.jpg")


def apply_border_filter(photo):
    width, height = photo.size
    photo = photo.transform((width + 100, height + 100), Image.EXTENT,
        (-10, -10, width + 10, height + 10), Image.BILINEAR)
    photo.save("image/border_photo.jpg")


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
    sepia_image.save("image/sepia_photo.jpg")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="Получить название файла", default="image.png")
    parser.add_argument("--bw_photo", action="store_true", help="чёрно-белый фильтр")
    parser.add_argument("--contrast_photo", action="store_true", help="контрастный фильтр")
    parser.add_argument("--blur_photo", action="store_true", help="размытие фильтр")
    parser.add_argument("--noise_photo", action="store_true", help="медианный фильтр")
    parser.add_argument("--border_photo", action="store_true", help="фильтр рамки")
    parser.add_argument("--sepia_photo", action="store_true", help="фильтр сепии")

    args = parser.parse_args() 
    print('Название файла:', args.file_name)
    original_photo = Image.open(f"{args.file_name}")
   
    if args.bw_photo:
        apply_bw_filter(original_photo)
    print(f"Использование черно-белого фильтра:  {args.bw_photo}")
   
    if args.contrast_photo:
        apply_contrast_filter(original_photo)
    print(f"Использование контрастного фильтра:  {args.contrast_photo}")
    
    if args.blur_photo:
        apply_blur_filter(original_photo)  
    print(f"Использование фильтра размытия:  {args.blur_photo}")
    
    if args.noise_photo:
        apply_noise_filter(original_photo)
    print(f"Использование медианного фильтра:  {args.noise_photo}")
    
    if args.border_photo:
        apply_border_filter(original_photo)
    print(f"Использование рамки:  {args.border_photo}")
    
    if args.sepia_photo:
        apply_sepia_filter(original_photo)
    print(f"Использование фильтра сепии:  {args.sepia_photo}")

     


if __name__ == "__main__":
    main()










