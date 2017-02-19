from django.shortcuts import render,get_object_or_404
from .models import Exam ,Quiz,Choice
from django.http import HttpResponse

def index(request):
    # get all published exams
    exam_pub = Exam.objects.filter(published=True)
    context = {'exam_pub':exam_pub}
    
    
    return render(request, 'index.html', context)



def detail(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
    except Exam.DoesNotExist:
        raise Http404("Exam does not exist")
    return render(request, 'detail.html', {'exam': exam})
