from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# models
from panel.models import Event, Event_Images, Product, Full_Sheet, Page_Handler
from vsg.models import VSG, VSG_Product



# < == Home ========================================================== >

def home(request):

    try :
        vsg = VSG.objects.get(is_default=True)
    except :
        messages.success(request, 'Visualization area not found')

        return redirect('error')

    try :
        page_handler = Page_Handler.objects.get(pk=2)
    except :
        page_handler = None

    events = Event.objects.all()


    products = Product.objects.all()


    send = {
        'page_handler': page_handler,
        'events': events,
        'vsg': vsg,
        'products': products,
    }

    return render(request, 'front/index.html', send)




# < == Products ========================================================== >

def products(request):

    try :
        page_handler = Page_Handler.objects.get(pk=3)
    except :
        page_handler = None

    products = Product.objects.all()

    events = Event.objects.all()

    send = {
        'page_handler': page_handler,
        'products': products,
        'events': events,
    }

    return render(request, 'front/products.html', send)




# < == Product Detail ========================================================== >

def product_detail(request, name_slug):

    try :
        page_handler = Page_Handler.objects.get(pk=3)
    except :
        page_handler = None

    events = Event.objects.all()

    try:
        product = Product.objects.get(name_slug=name_slug)
    except :
        messages.success(request, 'Something went wrong. It appears that the product is not discoverable. Try going back to home and give it one more try.')

        return redirect('error')

    sheets_all = Full_Sheet.objects.filter(fk=product)

    paginator = Paginator(sheets_all, 15)
    page = request.GET.get('page')

    try :
        sheets = paginator.page(page)
    except PageNotAnInteger :
        sheets = paginator.page(1)
    except EmptyPage :
        sheets = paginator.page(paginator.num_pages)
    
    send = {
        'page_handler': page_handler,
        'product': product,
        'sheets': sheets,
        'events': events,
    }

    return render(request, 'front/product_detail.html', send)


def product_detail_single(request, name_slug, sheet_number) :

    try :
        page_handler = Page_Handler.objects.get(pk=10)
    except :
        page_handler = None

    events = Event.objects.all()

    try:
        product = Product.objects.get(name_slug=name_slug)
    except :
        messages.success(request, 'Something went wrong. It appears that the product is not discoverable. Try going back to home and give it one more try.')

        return redirect('error')

    try:
        sheet = Full_Sheet.objects.get(fk=product, number=sheet_number)
    except :
        messages.success(request, 'Something went wrong. It appears that the product is not discoverable. Try going back to home and give it one more try.')

        return redirect('error')

    send = {
        'page_handler': page_handler,
        'product': product,
        'sheet': sheet,
        'events': events,
    }

    return render(request, 'front/product_detail_single.html', send)
    



# < == Product Search ========================================================== >

def product_search(request) :

    try :
        page_handler = Page_Handler.objects.get(pk=8)
    except :
        page_handler = None

    events = Event.objects.all()

    search = request.GET.get('search', '')

    sheets = Full_Sheet.objects.filter(number__contains=search).order_by('-index')

    paginator = Paginator(sheets, 12)
    page = request.GET.get('page')

    try :
        sheet = paginator.page(page)
    except PageNotAnInteger :
        sheet = paginator.page(1)
    except EmptyPage :
        sheet = paginator.page(paginator.num_pages)


    send = {
        'page_handler': page_handler,
        'sheets': sheets,
        'search': search,
        'sheet': sheet,
        'events': events,
    }

    return render(request, 'front/product_search.html', send)




# < == Catalogue ========================================================== >

def catalogues(request) :

    try :
        page_handler = Page_Handler.objects.get(pk=4)
    except :
        page_handler = None

    events = Event.objects.all()

    send = {
        'page_handler': page_handler,
        'events': events,
    }

    return render(request, 'front/catalogues.html', send)


def catalogue_1mm(request):
    return redirect("https://drive.google.com/file/d/1PHV-p9M2LlysIyKm9vzpaZy2c_7NmH2h/preview")


def catalogue_elite(request):
    return redirect("https://drive.google.com/file/d/1kA43qowB8PMKD3x_12vyjoxRAmoTk-Ca/preview")


def catalogue_lemore(request):
    return redirect("https://drive.google.com/file/d/1EryS9kkKtxfk2KJuHVfu04N-QeLUwIAo/preview")
    





# < == Events ========================================================== >

def events(request, name_slug):

    try :
        page_handler = Page_Handler.objects.get(pk=6)
    except :
        page_handler = None

    try :
        event = Event.objects.get(name_slug=name_slug)
    except :
        msg = "Something went wrong, go to home and try again !"
        messages.success(request, msg)

        return HttpResponse("Hehehe")

    event_images = Event_Images.objects.filter(fk=event)

    events = Event.objects.all()

    send = {
        'page_handler': page_handler,
        'event': event,
        'events': events,
        'event_images': event_images,
    }

    return render(request, 'front/events.html', send)




# < == Contact ========================================================== >

def contact(request):

    try :
        page_handler = Page_Handler.objects.get(pk=7)
    except :
        page_handler = None

    events = Event.objects.all()

    send = {
        'events': events,
        'page_handler': page_handler,
    }

    return render(request, 'front/contact.html', send)




# < == Privacy Policy ========================================================== >

def privacy_policy(request):

    try :
        page_handler = Page_Handler.objects.get(pk=9)
    except :
        page_handler = None

    events = Event.objects.all()

    
    send = {
        'page_handler': page_handler,
        'events': events,
    }

    return render(request, 'front/privacy_policy.html', send)




# < == Error ========================================================== >

def error(request) :

    return render(request, 'front/error.html')
