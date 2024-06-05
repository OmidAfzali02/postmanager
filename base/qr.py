import qrcode
from django.conf import settings
from io import BytesIO
from django.core.files import File

def qr_encode(data, name):
    # Data to be encoded
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save it somewhere, change the path as needed
    # img_path = str(settings.MEDIA_ROOT) + '/' + data.get('id') + '.png'
    qr_io = BytesIO()
    img.save(qr_io, format='PNG')
    qr_io.seek(0)  # Go to the start of the BytesIO object

    # Create a Django File object
    filename = name + '.png'
    qr_file = File(qr_io, name=filename)

    return qr_file

