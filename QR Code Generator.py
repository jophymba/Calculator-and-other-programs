import qrcode

url = input("Enter the URL: ").strip()
file_path = "/Users/jophymac/Desktop/Github/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated")

