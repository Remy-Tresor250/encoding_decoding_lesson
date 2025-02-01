import barcode
from barcode.writer import ImageWriter

data = "https://benax.rw"

barcode_type = barcode.get_barcode_class("code128")
barcode_instance = barcode_type(data, writer=ImageWriter())

barcode_instance.save("barcode")

print(f"Barcode saved as barcode.png")
