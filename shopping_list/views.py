from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingItem
from .forms import ShoppingItemForm

# Create your views here.

def index(request):
    return render(request, 'home_shopping.html')

def add_item(request):
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ShoppingItemForm()
    return render(request, 'add_shopping.html', {'form': form})

def list_items(request):
    items = ShoppingItem.objects.all()
    return render(request, "list_shopping.html", {"items": items})

def purchased(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.purchased = not item.purchased 
    item.save()
    return redirect("list_items")

def delete_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.delete()
    return redirect("list_items")
    
def edit_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ShoppingItemForm(instance=item)
    return render(request, 'edit_shopping.html', {'form': form, 'item': item})
