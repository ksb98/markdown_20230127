from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from pybo.models import Question
from templates.pybo.forms import AnswerForm


def answer_create(request, question_id):
   '''답변등록'''
   print('answer_create question_id:{}'.format(question_id))
   question = get_object_or_404(Question,pk=question_id)
   if request.method == 'POST':
      form = AnswerForm(request.POST)
      print('1.request.method:{}'.format(request.method))
      if form.is_valid():
         print('2.form.is_valid():{}'.format(form.is_valid()))
         answer = form.save(commit=False)# content만 저장(commit은 하지 않음)
         answer.create_date = timezone.now()
         answer.question    = question
         answer.save() #최종 저장
         return redirect('pybo:detail',question_id=question.id)
   else:
      return HttpResponseNotAllowed('Post만 가능 합니다.')
   #form validation
   context = {'question':question,'form':form}
   return render(request,'pybo/question_detail.html',context)
