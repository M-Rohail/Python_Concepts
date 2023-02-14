import pyqrcode
text = input("Enter the text to generate QR code: ")
Link_din = pyqrcode.create(text)
Link_din.svg("Link_din.svg", scale=8)
