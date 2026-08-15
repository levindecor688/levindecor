from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from decouple import config


def product_redirect(request):
    current_url = request.path
    product_number = current_url.split('/')[-1]
    
    cloud_name = config('CLOUDINARY_CLOUD_NAME', default='')
    if cloud_name:
        return redirect(f'https://res.cloudinary.com/{cloud_name}/image/upload/portfolio/full-sheet/{product_number}')

    return redirect('/media/portfolio/full-sheet/' + product_number)

