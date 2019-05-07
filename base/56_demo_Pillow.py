from PIL import Image

def demo_pil_image():
    im = Image.open('../temp/test_picture.jpg')
    w, h = im.size
    print('Original image size: %sx%s' % (w,h))
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' %(w//2, h//2))
    im.save('../temp/thumbnail.jpg', 'jpeg')

if __name__ == '__main__':
    demo_pil_image()