from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
 template_name = 'pages/about.html'

 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Mariana Valderrama",
    })
    return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact Us - Online Store",
            "email": "mari@gmail.com",
            "address": "EAFIT, Medellín, Colombia",
            "phone": "1234567",
        })
        return context
    
class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 150},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 200},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 30},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 15},
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        try:
            product = Product.products[int(id) - 1]
        except (IndexError, ValueError):
            # Si el ID no es válido, redireccionar a la página de inicio
            return HttpResponseRedirect(reverse('home'))
        viewData = {}
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)

from django import forms
from django.shortcuts import render, redirect

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Here you would normally save the product, but for now just redirect to products index
            return redirect('products_index')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)