from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf


def index(request, *args, **kwargs):
    return HttpResponse('hello world')

def year_archive(request, year, *args, **kwargs):
    return HttpResponse('hello, {} archive\n'.format(year))


def month_archive(request, year, month, *args, **kwargs):
    return HttpResponse('hello, month archive, year={}, moth={}!\n'.format(year, month))


def article_title(request, year, month, title, *args, **kwargs):
    return HttpResponse('hello, title archive, year={}, month={}, title={}!\n'.format(year, month, title))

# 表单
def form_get(request):
    return render(request, 'hello/form_get.html')


def search(request):
    global p
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        q = 'q的内容为: ' + request.GET['q']
        p = 'p的内容为: ' + request.GET['p']
    else:
        q = '你提交了空表单'
    return HttpResponse('hello, title archive, year={}, month={}\n'.format(q, p))


# 接收POST请求数据
def form_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "hello/form_post.html", ctx)



