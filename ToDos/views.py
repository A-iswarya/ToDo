from django.shortcuts import render, redirect

from .models import ToDo

from django.views.decorators.http import require_POST

from .forms import ToDoForm


def index(request):
    todo_items = ToDo.objects.order_by('id');
    form = ToDoForm()
    context = {'todo_items' : todo_items, 'form' : form};
    return render(request,'ToDos/index.html',context);

#To add a ToDo into the list
@require_POST
def addToDoItem(request):
    form = ToDoForm(request.POST);
    if form.is_valid():
        new_todo = ToDo(text=request.POST['text']);
        new_todo.save();
    return redirect('index');


#Marking a ToDo as completed
def completedTodo(request,todo_id):
    todo = ToDo.objects.get(pk=todo_id);
    todo.completed = True;
    todo.save();
    return redirect('index');

#Deleting all the completed items
def deleteCompleted(request):
    ToDo.objects.filter(completed__exact = True).delete();
    return redirect('index');

#Deleting all the ToDo items
def deleteAll(request):
    ToDo.objects.all().delete();
    return redirect('index');
