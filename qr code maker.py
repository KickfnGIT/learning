
import os
import qrcode
file_path = os.path.expandvars("%USERPROFILE%\\Downloads\\")
from qrcode.image.styledpil import StyledPilImage

link = input("Enter the text or URL: ").strip()
name = input("Enter the filename: ").strip()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage)
img.save(f"{file_path}{name}.png")
print("")
print(f"Qr code saved in {file_path} as {name}.png")