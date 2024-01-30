from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Booksavailable
from .forms import BooksavailableForm

def Hello(request):
    return HttpResponse("Hello world!") 

def bookstore(request):
  member_list = Booksavailable.objects.all().values()
  context = {
    'member_list':member_list
  }
  template = loader.get_template('bookstore.html')
  return HttpResponse(template.render(context, request))

def detail(request,id):
  mymember = Booksavailable.objects.get(id=id)
  context = {
    
    'mymember':mymember
  }
  template = loader.get_template('detail.html')
  return HttpResponse(template.render(context, request))


def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())


@csrf_exempt
def add_newbook(request):
   if request.method=='POST':
     bookname=request.POST.get('bookname',)
     authorname=request.POST.get('authorname',)
     booksavailable=Booksavailable(bookname=bookname,authorname=authorname)
     booksavailable.save()
   template = loader.get_template('add_newbook.html')
   return HttpResponse(template.render())

def update(request,id):
  booksavailabel=Booksavailable.objects.get(id=id)
  form=BooksavailableForm(request.POST,instance=booksavailabel)
  if form.is_valid():
     form.save()
     t1=loader.get_template('add_newbook.html')
     return HttpResponse(t1.render())
  return render(request,'update.html',{'form':form,'booksavailabel':booksavailabel})


@csrf_exempt
def delete(request,id):
  if request.method == 'POST':
    member=Booksavailable.objects.get(id=id)
    member.delete()
    t1=loader.get_template('bookstore.html')
    return HttpResponse(t1.render())
  return render(request,'delete.html')

@csrf_exempt
def availabel(request,id):
  if request.method == 'POST':
    member=Booksavailable.objects.get(id=id)
    member.availabel()
    t1=loader.get_template('bookstore.html')
    return HttpResponse(t1.render())
  return render(request,'availabel.html')

   
'''
def members(request):
  member_list = Member.objects.all().values()
  context = {
    'member_list':member_list
  }
  template = loader.get_template('members.html')
  return HttpResponse(template.render(context, request))


def detail(request,id):
  mymember = Member.objects.get(id=id)
  context = {
    
    'mymember':mymember
  }
  template = loader.get_template('detail.html')
  return HttpResponse(template.render(context, request))

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())


@csrf_exempt
def add_newmember(request):
  if request.method=='POST':
    firstname= request.POST.get('firstname',)
    lastname= request.POST.get('lastname',)
    rollno= request.POST.get('rollno',)
    phoneno= request.POST.get('phoneno',)
    image=request.FILES['image']
    member=Member(firstname=firstname,lastname=lastname,rollno=rollno,phoneno=phoneno,image=image)
    member.save()
  template = loader.get_template('add_newmember.html')
  return HttpResponse(template.render())

def update(request,id):
  member=Member.objects.get(id=id)
  form=MemberForm(request.POST,instance=member)
  if form.is_valid():
     form.save()
     t1=loader.get_template('add_newmember.html')
     return HttpResponse(t1.render())
  return render(request,'update.html',{'form':form,'member':member})

@csrf_exempt
def delete(request,id):
  if request.method == 'POST':
    member=Member.objects.get(id=id)
    member.delete()
    t1=loader.get_template('members.html')
    return HttpResponse(t1.render())
  return render(request,'delete.html')
'''