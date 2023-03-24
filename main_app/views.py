from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .forms import ItemForm
from .models import Item

# Create your views here.
def home(request):
  return render(request, 'home.html')

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', {
    'items': items
  })


class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/index'
  
class ItemDelete(DeleteView):
    model = Item
    success_url = '/index'
