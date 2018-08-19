from django.shortcuts import render, HttpResponse, redirect
# from django.utils import
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user == 'root' and pwd == '123':
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存到session中
            # 在随机字符串对应的字典中设置相关内容
            request.session['username'] = user
            request.session['is_login'] = True
            return redirect('/index/')
        else:
            return render(request, 'login.html')

def index(request):
    # 获取当前用户的随机字符串
    # 根据随机字符串获取对应信息
    if request.session['is_login'] == True:
        return HttpResponse(request.session['username'])
    else:
        return HttpResponse("Gone")