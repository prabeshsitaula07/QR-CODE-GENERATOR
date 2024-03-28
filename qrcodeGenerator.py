import qrcode

# Data to encode into the QR code
name = input("Name: ")
phone = input("Phone Number: ")
email = input("Email : ")
address = input("Address : ")

dataList = [name, phone, email, address]
combinedData = '\n'.join(dataList)

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(combinedData)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
imgName = input("save your QR image as: ")
img.save(f'{imgName}.png')

print("QR code generated successfully.")
