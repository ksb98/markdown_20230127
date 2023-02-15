from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from templates.pybo.forms import QuestionForm
from .models import Question
from .models import Question
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   # list order create_date desc
   print('index 레벨로 출력')
   question_list = Question.objects.order_by('-create_date')  # order_by('-필드') desc, asc order_by('필드')
   # question_list = Question.objects.filter(id=99)  # order_by('-필드') desc, asc order_by('필드')
   context = {'question_list': question_list}
   print('question_list:{}'.format(question_list))
   return render(request, 'pybo/question_list.html', context)
def detail(request,question_id):
   '''question 상세'''
   print('1.question_id:{}'.format(question_id))
   #question=Question.objects.get(id=question_id)
   question = get_object_or_404(Question,pk=question_id)
   print('2.question:{}'.format(question))
   context = {'question':question}
   return render(request,'pybo/question_detail.html',context)
def answer_create(request, question_id):
   print('answer_create question_id:{}'.format(question_id))
   question = get_object_or_404(Question,pk=question_id)
   #Questionr과 Answer  처럼 서로 연결되어 있는 경우
   #연결모델명_set 연결데이터를 조회 할수 있다.
   question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
   return redirect('pybo:detail',question_id=question.id)
def boot_reg(request):
   '''bootstrap reg'''
   return render(request, 'pybo/reg.html')
def boot_list(request):
   '''bootstrap list'''
   return render(request, 'pybo/list.html')
def question_create(request):
   '''질문등록'''
   print('1.request.method:{}'.format(request.method))
   if request.method == 'POST':
      print('2.question_create post')
      #저장
      form = QuestionForm(request.POST)  #request.POST 데이터 (subject,content 자동 생성)
      print('3.question_create post')
      # form(질문등록)이 유효하면
      if form.is_valid():
         print('4.form.is_valid():{}'.format(form.is_valid()))
         question=form.save(commit=False) # subject, content만 저장(commit은 하지 않음)
         question.create_date = timezone.now()
         question.save() #날짜 까지 생성해서 저장(Commit)
         return redirect("pybo:index")
   else:
      form = QuestionForm()
   context = {'form': form}
   return render(request,'pybo/question_form.html',context)
