from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import PromtForm
from huggingface_hub import InferenceClient
import time
API_KEY=os.environ['HUGGINGFACEWEBAPI']

# Create your views here.
def get_response(prompt):
    client=InferenceClient(api_key=API_KEY)
    messages=[
        {
        'role':'user',
        'content':prompt,
    },
    {'role':'system',
     'content':'your name is Jajoul.'
     }
    ]
    completion=client.chat.completions.create(messages=messages,model="katanemo/Arch-Function-3B",max_tokens=500)
    response=completion.choices[0].message
    return response.content
def index(request):
    #intro_prompt="interduce your self and what is your model?"
    #return HttpResponse(get_response(intro_prompt),)
    return render(request,'talk/index.html')
def talk(request):
    #Handle request

    if request.method=='POST':
        form=PromtForm(request.POST)
        if form.is_valid():
            prompt=form.cleaned_data['prompt_text']
            ai_response=get_response(prompt=prompt)
            print(type(ai_response))
            return render(request,'talk/talk.html',{'ai_response':ai_response,'form':form})
    else:
        form=PromtForm()
    return render (request,'talk/talk.html',{'form':form})
    