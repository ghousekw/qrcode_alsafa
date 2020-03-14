from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': "QRCode | Home"}
    return render(request, 'qrcode/index.html', context)