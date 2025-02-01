import pdf417gen as pdf417

data = "This is a PDF417 barcode exmaple. It supports encoding large amounts of data in a small space."

codes = pdf417.encode(data, columns=5, security_level=5)

pdf417_image = pdf417.render_image(codes, scale=3)

pdf417_image.save("pdf417_code.png")
print("PDF417 barcode saved as pdf417_code.png")

pdf417_image.show()