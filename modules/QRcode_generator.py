# QR Code Generator

# 1. in terminal run: pip install qrcode[pil]
# 2. run this code
# 3. check your folder for the generated qrcode.png file

import qrcode

url = input("Enter the URL to encode in QR Code: ").strip()

myqr = qrcode.make(url)
myqr.save("qrcode.png")