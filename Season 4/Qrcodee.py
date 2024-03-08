import qrcode

name = input('enter your name and family: ')
phune_n = input('enter your number: ')
qr_s = (name, phune_n)
img = qrcode.make(qr_s)
img.save("yourqrcode.png")