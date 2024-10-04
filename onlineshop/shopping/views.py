from django.shortcuts import render,HttpResponse
from .models import *
from django.template import loader
# Create your views here.

def main(request):
    catigory = Catigories.objects.all().values()
    manfashion = Manfashion.objects.all()
    manfashionSub = ManfashionBestSeller.objects.all()
    womanfashion = Womenfashion.objects.all()
    womanfashionSub = WomenfashionBestSeller.objects.all()
    computers = Computer.objects.all().values()
    laptops = Laptop.objects.all().values()
    mobile = Mobile.objects.all().values()
    necklace = Neklace.objects.all()
    rings = Ring.objects.all()
    earRings = EarRing.objects.all()
    context = {'catigory': catigory,
               'computers':computers,
               'laptops':laptops,
               'mobile':mobile,
               'manfashion':manfashion,
               'manfashionSub':manfashionSub,
               'womanfashion':womanfashion,
               'womanfashionSub':womanfashionSub,
               'catigory':catigory,
               'necklace':necklace,
               'rings':rings,
               'earRings':earRings,
               
               }
    return render(request, 'shopping/index.html', context)
def addOn(request):
    catigory = Catigories.objects.all().values()
    context = {'catigory': catigory}
    return render(request, 'shopping/addon.html', context)
def electronic(request):
    catigory = Catigories.objects.all().values()
    computers = Computer.objects.all().values()
    laptops = Laptop.objects.all().values()
    mobile = Mobile.objects.all().values()
    context = {'catigory':catigory,
               'computers':computers,
               'laptops':laptops,
               'mobile':mobile}
    return render(request,'shopping/electronic.html', context)

def fashion(request):
    catigory = Catigories.objects.all().values()
    manfashion = Manfashion.objects.all()
    manfashionSub = ManfashionBestSeller.objects.all()
    womanfashion = Womenfashion.objects.all()
    womanfashionSub = WomenfashionBestSeller.objects.all()
    context = {'catigory': catigory,
               'manfashion':manfashion,
               'manfashionSub':manfashionSub,
               'womanfashion':womanfashion,
               'womanfashionSub':womanfashionSub}
    return render(request,'shopping/fashion.html', context)

def jewellery(request):
    catigory = Catigories.objects.all().values()
    necklace = Neklace.objects.all()
    rings = Ring.objects.all()
    earRings = EarRing.objects.all()
    context = {'catigory':catigory,
               'necklace':necklace,
               'rings':rings,
               'earRings':earRings}
    return render(request,'shopping/jewellery.html', context) 


def details(request, id):
    catigory = Catigories.objects.get(id=id)
    viewComputers =  Computer.objects.get(id=id)
    viewMobile = Mobile.objects.get(id=id)
    viewLaptops = Laptop.objects.get(id=id)
    # template = loader.get_template('details.html')
    
    context = {'catigory':catigory,
               'viewComputers':viewComputers,
               'viewLaptops':viewLaptops,
               'viewMobile':viewMobile}
    return render(context, request)