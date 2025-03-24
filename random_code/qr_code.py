import qrcode
from PIL import Image

# Define the URL for the QR Code
website_url = "https://drive.google.com/drive/folders/1-2ga6NN4WkqcHmn1TM5Gg5-Ftqs8bMvN"

# Create a QR Code instance with higher resolution settings
qr = qrcode.QRCode(
    version=None,  # Automatically adjusts size based on input data
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=50,  # Increased box size for higher resolution
    border=4,  # Standard border size
)

# Add data to the QR code
qr.add_data(website_url)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as a high-resolution PNG (e.g., 300 DPI for printing)
output_file = "banner_qr_code.png"
img = img.resize((img.width * 10, img.height * 10), Image.Resampling.LANCZOS)  # Scale up image
img.save(output_file, dpi=(300, 300))

print(f"High-resolution QR code saved as '{output_file}'.")
