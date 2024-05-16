from django.shortcuts import render
from .models import Teachers


def teacher(request):
    teachers = Teachers.objects.all().order_by('-id')
    context = {
        'teachers': teachers
    }
    return render(
        request=request,
        template_name='teacher.html',
        context=context
    )

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def review(request):
    return render(request, 'review.html')

def contact(request):
    return render(request, 'contact.html')
