from psdtoolsx import PSDImage
psd = PSDImage.open("test.psd")
psd.composite().save('test.png')

for layer in psd[::-1]:
    print(layer)
    image = layer.composite()
