import qrcode
qr= qrcode.QRCode(
    version=13,
    border=5,
    box_size=10,
)

data=input("Enter the data you want to make QR: ")
imgn=input("Enter the image name you want to save: ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fit_color='black', back_color='white')
img.save(f"{imgn}.png")

