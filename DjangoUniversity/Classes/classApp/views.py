from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import djangoClasse
from .import views
from .forms import ClassForm

# Create your views here.
# this is where we associate all of the instructions

def admin_console(request):
    classes = djangoClasse.object.all()
    return render(request, 'classApp/class_page.html', {'classes': classes})

def details(request, pk):
    pk = int(pk)  # we are converting the primary key string into a number here
    item = get_object_or_404(djangoClasse, pk=pk) # this is to go check for an item in the database and if it isn't there
    # don't crash and just give a 404 error saying nothing is there or page not found. then user can hit back move on
    """ then the class is looked at then use the dictionary object of pk which is the key word and also the value 
    which is converted into a number and so it will then take the pk and say look at item number 6 or 4 or whatever
    and then we query the database and whatever item that is associated with that particular number will then be stored
    in the item variable"""
    form = ClassForm(data=request.POST or None, instance=item)
    """ here we invoke the class form and say that the 
    post from the request, .post means if the method is the post and the method is post from our class page.html
    so if they give info and send it to us no one can see it because they used post and so the .post is saying try to
    get info from the post the user delivered to us but if you can't provide a none value but if you do have something
    the instance will be the item we grab. """
    if request.method == 'POST':
        """ this is saying if the request method is POST then check the form and make sure everything is valid
        and if it is then we will save all the info the user put in into our database."""
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'classApp/present_classes.html', {'form': form}) # this will take the user to another
    # page where they can edit the info if needed and then if they do we will get a new post and save the new info
    # that is why there is 2 saves above and then after that it will take the user and redirect them back to the
    # admin_console page which will be the original products page, and if the form isn't valid then we will tell the
    # user what still needs to be filled out.

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