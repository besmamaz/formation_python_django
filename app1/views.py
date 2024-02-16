from django.shortcuts import render
from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')  
# Create your views here.
def v_add_numbers(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2
    else:
        result = None

    return render(request, 'index.html', {'result': result})


from .models import CalculatedResult


def v_add_numbers2(request):
    result = None  # Définir la variable result en dehors de la logique de POST

    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2

        # Enregistrer les valeurs dans la base de données
        CalculatedResult.objects.create(
            num1=num1,
            num2=num2,
            result=result
        )

    # Récupérer l'historique des calculs depuis la base de données
    history = CalculatedResult.objects.all().order_by('-id')

    return render(request, 'index2.html', {'history': history, 'result': result})
from .models import Student

def add_student(request):
     if request.method == 'POST':
        nom = request.POST.get('nom', 0)
        prenom = request.POST.get('prenom', 0)
        matricule = request.POST.get('matricule', 0)

        Student.objects.create(
            nom=nom,
            prenom=prenom,
            matricule=matricule
        )
        return redirect('home') 
                
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})