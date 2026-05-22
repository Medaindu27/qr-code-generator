import qrcode 
data="""
Name:  prakasam
Course : BTECH
Progect: Fraud transaction detection
Email : prakasam@gmail.com
"""
qr=qrcode.QRCode(
     version=1,
     error_correction=qrcode.constants.ERROR_CORRECT_L,
     box_size=10,
     border=4,
)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
image.save("my_details_qr.png")
print("QR code generated successfully as my_details_qr.png")
