# Install required library
# pip install qrcode

import qrcode
from PIL import Image

# Get user input for QR code content
data = input("Enter anything to generate QR: ")

# Create QR code with specific settings
qr = qrcode.QRCode(version=3, box_size=8, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image with custom colors
image = qr.make_image(fill="Black", back_color="aqua")

# Save and open the generated QR code
image.save("qr_code.png")
Image.open("qr_code.png")
