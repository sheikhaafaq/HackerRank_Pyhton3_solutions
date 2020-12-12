######import qrcode
######data = "https://instagram.com/pure.python"
######filename = "web.png"
######img = qrcode.make(data)
######img.save(filename)
######
########Import QRCode from pyqrcode 
import pyqrcode 
import png 



##s = "SHEIKH AAFAQ RASHID  1665/17CSEA2  9596326322  sheikh.69-cse-17@mietjammu.in"
s="https://wa.me/qr/3DT5YH4KS4MXC1"
## Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("wtsapp.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('wtsapp.png', scale = 6)



##import qrcode
####
####img = qrcode.make('test text')
####
####print(type(img))
####print(img.size)
##### <class 'qrcode.image.pil.PilImage'>
##### (290, 290)
####
####img.save('data/dst/qrcode_test.png')
##qr = qrcode.QRCode()
##qr.add_data('test text')
##qr.make()
##img = qr.make_image()
##img.save('data/dst/qrcode_test2.png')
