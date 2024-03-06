from django.shortcuts import render, redirect

from hospitalapp.forms import ImageUploadForm
from hospitalapp.models import Member, Products, Appointment, ImageModel


# Create your views here.
def index(request):
    if request.method == 'POST':
        message = contacts(name=request.POST['name'],
                           email=request.POST['email'],
                           subject=request.POST['subject'],
                           message=request.POST['message'])
        message.save()
        return redirect('/index')

    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Member(username=request.POST['username'],
                         email=request.POST['email'],
                         Password=request.POST['password'])
        members.save()
        return redirect('/login')
    else:
        return render(request, 'Register.html')


def login(request):
    return render(request, 'Log in.html')


def details(request):
    messages = contacts.objects.all()
    return render(request, 'details.html', {'messages': messages})


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 Password=request.POST['password']).exists():

            members = Member.objects.get(username=request.POST['username'],
                                         Password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'Log in.html')
    else:
        return render(request, 'Log in.html')


def uploadimage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/show image')


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show images.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")