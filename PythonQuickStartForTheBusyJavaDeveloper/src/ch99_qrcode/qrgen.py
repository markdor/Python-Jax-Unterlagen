import treepoem

img = treepoem.generate_barcode(
    barcode_type='qrcode',
    data='https://github.com/Michaeli71/Python-For-Machine-Learning-2024/',
    options={"eclevel": "Q"})

img.convert('1').save('Python-For-Machine-Learning-2024.png')
