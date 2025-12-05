from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingItem

# Create your views here. ADD SHOPPING AT THE END OF EVERY HTML. 

def index(request):
    return render(request, 'home_shopping.html')

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        priority = request.POST.get('priority')

        ShoppingItem.objects.create(
            name=name,
            description=description,
            priority=priority,
        )
        return redirect('list_items')

    return render(request, "add_shopping.html")

def list_items(request):
    items = ShoppingItem.objects.all()   # <--- fetch items
    return render(request, "list_shopping.html", {"items": items})

def purchased(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.purchased = not item.purchased   # Flip the boolean
    item.save()
    return redirect("list_items")

def delete_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.delete()
    return redirect("list_items")
    
