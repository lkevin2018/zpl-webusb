from zebrafy import ZebrafyImage

with open("/Users/kevin/Desktop/processed_kevin@thekevinjoseph.com_71116304-2220-452f-bd69-9b8a09876f11_label0.png", "rb") as image:
    zpl_string = ZebrafyImage(image.read(), invert=True).to_zpl()

with open("output.zpl", "w") as zpl:
    zpl.write(zpl_string)