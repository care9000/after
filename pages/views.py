from django.shortcuts import render
import random
from datetime import datetime
import requests
# Create your views here.
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context={
        'name': name,
        'age': age, 
        'pick': pick
        }
    return render(request, 'hello.html', context)
#4-1 동적 라우팅을 이용하여 name과 age를 받아 자기소개 페이지 만들기
def myself(request, name, age):
    context = {
        'name':name,
        'age': age,
        }
    return render(request, 'myself.html', context)

#4-2 두개의 숫자를 인자로받아 num1, num2의 곱셈결과 출력
def mul(request, num1, num2):
    num3= num1*num2
    context={
        'num1':num1,
        'num2':num2,
        }

    return render(request,'mul.html',context)

#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle(request,r):
    area=r**2*3.14
    context={
        'r':r,
        'area': area,
    }
    return render(request,'circle.html',context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Too fast to live, Too young to die'
    messages=['apple', 'banana', 'cucumber', 'mango','b']
    datetimenow=datetime.now()
    empty_list= []
    context={
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':messages,
        'datetimenow':datetimenow,
        'empty_list':empty_list,
        }
    return render(request,'template_language.html', context)


def isbirth(request):
    today = datetime.now()
    day= today.day
    month = today.month
    
    if month == 9 and day == 28:
        result = True
    else:
        result = False
    context={
        'day':day,
        'month':month,
        'result':result
        
    }

    return render(request,'isbirth.html',context)


#6-2. 회문판별
def pal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result =False
    context ={
        'word':word,
        'result':result,
    }
    return render(request,'pal.html',context)


def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lotto = sorted(random.sample(range(1,46),6))
    if real_lottos == lotto:
        result = True
    else :
        result = False
    
    context ={
        'real_lottos':real_lottos,
        'lotto':lotto,
        'result':result,
    }
    return render(request,'lotto.html',context)

#7. Form -GET
def throw(request):
    return render(request,'throw.html')

def catch(request):
    name= request.GET.get('name')
    name2= request.GET.get('name2')

    context={
        'name':name,
        'name2':name2,
    }
    return render(request,'catch.html',context)

def ping(request):
    return render(request,'ping.html')

def pong(request):
    name =request.GET.get("name")
    name2 = request.GET.get("name2")
    context ={
        'name': name,
        'name2': name2,
    }
    return render(request,'pong.html',context)

def art(request):
    return render(request, 'art.html')
def result(request):
    word = request.GET.get('word')
    fonts =requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts.split('\n')
    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context={
        'result':result
    }
    return render(request,'result.html',context)

def user_new(request):
    return render(request,'user_new.html')

def user_create(request):
    name=request.POST.get("name")
    pwd=request.POST.get("pwd")
    context ={
        'name':name,
        'pwd':pwd,
    }
    return render(request,'user_create.html', context)
# homework !!!! workshop 1414141414141414!!!
def num_push(request):
    return render(request,'num_push.html')

def num_pull(request):
    num =request.GET.get('num')
    context ={
        'num':num
    }
    return render(request,'num_pull.html', context)