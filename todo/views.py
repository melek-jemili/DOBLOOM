from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/login.html', {'form': form})


from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirige vers la liste des todos après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'todo/register.html', {'form': form})



def home(request):
    return render(request, 'todo/index.html')

def about(request):
    return render(request, 'todo/about.html')

def contact(request):
    return render(request, 'todo/contact.html')


# ✅ Lister les todos
def todo_list(request):

    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    else:
        todos = Todo.objects.none()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# ✅ Ajouter un todo
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)  # ✅ Crée une instance de Todo sans la sauvegarder
            todo.user = request.user  # ✅ Associe l'utilisateur connecté au todo
            todo.save()
            return redirect('todo_list')  # ✅ Redirige vers la liste des todos
    else:
        form = TodoForm()
    return render(request, 'todo/todo_add.html', {'form': form})
# ✅ Modifier un todo
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # ✅ Redirige vers la liste des todos
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})

# ✅ Supprimer un todo
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')  # ✅ Redirige vers la liste des todos
    return render(request, 'todo/todo_delete.html', {'todo': todo})
