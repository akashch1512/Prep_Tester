from django.shortcuts import render
from .models import Question
import random

def mcq_test(request):
    questions = Question.objects.all()
    if not questions.exists():
        return render(request, 'mcq/no_questions.html')
    
    random_question = random.choice(questions)
    
    if request.method == "POST":
        # Process answer submission
        return render(request, 'mcq/question.html', {
            'question': random_question,
        })
    
    return render(request, 'mcq/question.html', {
        'question': random_question,
    })