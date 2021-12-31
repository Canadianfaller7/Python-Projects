from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import djangoClasse
from .import views
from .forms import ClassForm

# Create your views here.

def admin_console(request):
    classes = djangoClasse.object.all()
    return render(request, 'classApp/class_page.html', {'classes': classes})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasse, pk=pk)
    form = ClassForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'classApp/present_classes.html', {'form': form})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasse, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {'item': item, }
    return render(request, 'classApp/confirmDelete.html', context)

def confirmed(request):
    if request.method == 'POST':
        form = ClassForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')

def createRecord(request):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ClassForm()
    context = {
        'form' : form,
    }
    return render(request, 'classApp/createRecord.html', context)