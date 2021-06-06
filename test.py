from qrcode import *
fname = "Prateek"
lname = "Rao"
mobile = 7507
mailid = "rao@gta.com"
gender = "male"
data = {'First Name':fname, 'Last Name':lname, 'Mobile No':mobile, 'Mail Id':mailid, 'Gender':gender}

img = make(data)
img.save("test.png")