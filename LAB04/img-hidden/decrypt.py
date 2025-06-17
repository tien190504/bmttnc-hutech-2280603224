import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size

    # 1) Đọc hết LSB của tất cả pixel
    bits = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            bits.append(format(r, '08b')[-1])
            bits.append(format(g, '08b')[-1])
            bits.append(format(b, '08b')[-1])

    bit_str = ''.join(bits)

    # 2) Tìm marker 16-bit và cắt chuỗi trước marker
    marker = '1111111111111110'
    end = bit_str.find(marker)
    if end != -1:
        bit_str = bit_str[:end]

    # 3) Chuyển mỗi 8 bit thành ký tự
    message = ''
    for i in range(0, len(bit_str), 8):
        byte = bit_str[i:i+8]
        message += chr(int(byte, 2))

    return message


def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
