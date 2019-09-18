from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.hunter = request.user
            product.save()

            return redirect('/product/' + str(product.id))

        else:
            return render(request, 'product/create.html', {'error': 'All fields need to be filled!'})

    else:
        return render(request, 'product/create.html')


@login_required(login_url="/account/signup")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/product/' + str(product.id))
