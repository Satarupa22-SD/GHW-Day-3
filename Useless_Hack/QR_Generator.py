import qrcode
import image

qr = qrcode.QRCode(
    version=16,
    box_size=12,
    border=5

)

data = "https://ghw.mlh.io/daily-challenges/create-a-useless-hack"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill = "black", back_color = "white")
img.save("useless_hack1.png")
