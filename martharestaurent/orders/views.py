from datetime import datetime
from django.shortcuts import render, redirect
# from sympy import content
# from .forms import MainOrderForm
from .models import Maindishes
from .models import Sidedishes
from .models import Desserts
from .models import revenue
from django.db.models import Count

# Create your views here.
def order_form(request):
    if request.method == 'GET':
        return render(request, 'orders/orderform.html')
    else:
        totalAmount = 0
        choosedmaindish = request.POST.get('maindeshes')
        choosedsidedish = request.POST.getlist('sidedishes[]')
        chooseddesserts = request.POST.getlist('desserts[]')
        maindish = Maindishes(foodname = choosedmaindish)
        maindish.save()
        
        if choosedmaindish == 'rice':
            totalAmount += 100
        elif choosedmaindish == 'rotty':
            totalAmount += 20
        else:
            totalAmount += 150 
        
        for i in choosedsidedish:
            if i == 'wadai':
                totalAmount += 45
            elif i == 'dhal_curry':
                totalAmount += 75
            else:
                totalAmount += 120
            sidedish = Sidedishes(foodname = i, maindishes = maindish)
            sidedish.save()
            
        if len(chooseddesserts) > 0:
            for i in chooseddesserts:
                if i == 'wtalappam':
                    totalAmount += 40
                elif i == 'jelly':
                    totalAmount += 20
                else:
                    totalAmount += 25
                dessert = Desserts(foodname = i, maindishes = maindish)
                dessert.save()
                
        currentDate = datetime.today()      
        billamount = revenue(date=currentDate, amount=totalAmount, maindishes = maindish)
        billamount.save()
        
        return redirect('/orders')

def more_info(request):
    currentDate = datetime.today()
    allincome = revenue.objects.filter(date=currentDate)
    
    totalIncome = 0
    for i in allincome:
        totalIncome += i.amount
        
    resultOne = Maindishes.objects.values('foodname').order_by('-foodname__count').annotate(Count('foodname')).first()
    famousmain = resultOne['foodname'].capitalize()
    print(resultOne['foodname'])
    
    resultTwo = Sidedishes.objects.values('foodname').order_by('-foodname__count').annotate(Count('foodname')).first()
    if resultTwo['foodname'] == 'dhal_curry':
        famousside = 'Dhal Curry'
    elif resultTwo['foodname'] == 'fish_curry':
        famousside = 'Fish Curry'
    else:
        famousside = 'Wadai'
        
    context = {'income': totalIncome, 'famousMaindish':famousmain, 'famousSidedish': famousside}
    return render(request, 'orders/moredetails.html', context)