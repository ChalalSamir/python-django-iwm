from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect, redirect)

from .models import Question
from .forms import QuestionForm


def index(request):

    questions = Question.objects.all()
    context = {'questions': questions,}
    return render(request,'app1/index.html',context)

def create(request):

    questions = Question.objects.all()
    context = {'questions': questions,}

    form = QuestionForm(request.POST or None)
    
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "app1/create.html", context)



def detail_view(request, id):
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)
         
    return render(request, "app1/detail_view.html", context)

def update(request, id):

    questions = Question.objects.all()
    context = {'questions': questions,}
 
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/app1/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request,'app1/update.html',context)

def delete(request, id):

    questions = Question.objects.all()
    context = {'questions': questions,}
 
    obj = get_object_or_404(Question, id = id)
 
    if request.method =="POST":
        obj.delete()
        # home page
        return redirect("/app1/")
 
    return render(request,'app1/delete.html',context)


