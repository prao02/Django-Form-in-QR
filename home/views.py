from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import form_data
from qrcode import *

# Create your views here.
data = None

def index(request):
    return render(request, 'register.html')


def submit_form(request):
    global data
    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        mobile = request.POST['mobileno']
        mailid = request.POST['mailid']
        gender = request.POST['gender']
        print(fname, lname, gender, mobile, mailid)
        form_data(first_name = fname, last_name = lname, mobile = mobile, mailid = mailid, gender = gender).save()
        msg = "Form Submitted successfully"
        data = {'First Name':fname, 'Last Name':lname, 'Mobile No':mobile, 'Mail Id':mailid, 'Gender':gender}
        img = make(data)
        img.save("static/image/test.png")
        # return HttpResponseRedirect("/some/url/")
        return render(request,'register.html', {'msg': msg, 'data': data})
    else:
        return HttpResponse("<h2>404 not found</h2>")