from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm
from home.models import Book,Author,Genre
from django.utils import timezone
from django.contrib import messages

#create your views here.


# def form_view(request):
#      form = CustomForms()
#      context = {
#           "head":"Custom form created here using python" ,
#           "forms":form
#      }
#     return render(request,'forms.html', context)


def form_view(request):
     msg=' '
     if request.method =='POST':
          form = BookForms(request.POST)
          if form.is_valid():
               book = Book(name=form.cleaned_data.get('name'),purchase_date=form.cleaned_data.get('pur_date'),genre=form.cleaned_data.get('genre'),author=form.cleaned_data.get('author'))
               #book = Book.objects.create(name=form.cleaned_data.get('name'),purchase_date=form.cleaned_data.get('pur_date'),genre=form.cleaned_data.get('genre'),author=form.cleaned_data.get('author'))
               book.save()
               msg='Book Added successfully!!!'
          else:
               msg = form.errors
     else:
          form = BookForms()
     return render(request,'form.html',{"msg":msg,"forms":form})


def model_form(request):
     msg=''
     if request.method =='POST':
          form = ModelBookForms(request.POST)
          if form.is_valid():
               form.save()
               msg='Book Added successfully!!!'
          else:
               msg = form.errors
     else:
          form = ModelBookForms()
     return render(request,'form.html',{"msg":msg,"forms":form})     

def html_form(request):
    value=''
    if request.method=='post':
         value = request.POST.get('name')
         print('name',value)
         return render(request,'value.html',{'value':value})
    else:
          return render(request,'design.html')          


def booksearch(request):
     if request.method =='POST':
         form = SearchForm(request.Post)
         if form.is_valid():
             q=form.cleaned_data.get('q')
             book = Book.objects.filter(name__contains=q)
             return render(request,'showtables.html',{'book':book,'form':SearchForm()})
     else:
        form=SearchForm()
        book=Book.objects.all()
        return render(request,'showtables.html',{'book':book,'form':form})   

def deletebook(request,id):
   book = Book.objects.get(id=id)
   book.delete()
   messages.warning(request,'Deleted'+str(id)+' successfully!!!')
   return redirect('/')               
         
