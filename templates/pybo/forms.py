from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 question model

        fields = ['subject', 'content']  # QuestionForm사용할 question model의 속성
        widgets = {  # 속성 추가: class rows추가
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {  # subject->제목으로 변경
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
         model = Answer  # 사용할 Answer model
         fields = ['content']  # AnswerForm 사용할 Answer model 속성
         labels = {
                'content': '답변내용'

                }


