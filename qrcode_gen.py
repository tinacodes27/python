import qrcode
name = input("Enter the name: ")
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
qr.add_data(name)
qr.make()
image=qr.make_image(fill='black',back_color='white')
image.save("1st_QR.png")


