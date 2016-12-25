# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from models import *
from forms import ContactForm
from django.db.models import Q
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage,EmailMultiAlternatives

def index(request):
    context = RequestContext(request)
    allEntries_list = Entry.objects.filter(publish=True).order_by('-dateEntry')
    latestEntries=allEntries_list[:5]
    social = Social.objects.filter(show=True)

    paginator = Paginator(allEntries_list, 6)
    print paginator.count
    page = request.GET.get('page')
    try:
        allEntries = paginator.page(page)
    except PageNotAnInteger:
        allEntries = paginator.page(1)
    except EmptyPage:
        allEntries = paginator.page(paginator.num_pages)

    allTags = Tag.objects.all().order_by('name')
    allCategories = Category.objects.all().order_by('name')
    return render_to_response('index.html', {'entradas': allEntries, 'tags':allTags, 'latests': latestEntries, 'categories': allCategories, 'social': social}, context)

def searcher(request):
    context = RequestContext(request)
    allTags = Tag.objects.all().order_by('name')
    allCategories = Category.objects.all().order_by('name')
    allEntries_list = Entry.objects.filter(publish=True).order_by('-dateEntry')
    social = Social.objects.filter(show=True)
    if request.method == "GET":
        keyword = request.GET.get("keyword").encode('utf-8')
        tipo = request.GET.get("type")
        allEntries_list = Entry.objects.filter(Q(title__contains=str(keyword)) | Q(idTags__name__contains=str(keyword))| Q(idCategory__name__contains=str(keyword))).order_by('-dateEntry')
        results = keyword
        msg = None
        if tipo == 'category':
            allEntries_list = Entry.objects.filter(Q(idCategory__name__contains=str(keyword))).order_by('-dateEntry')
            msg = keyword
        if tipo == 'tag':
            allEntries_list = Entry.objects.filter(Q(idTags__name__contains=str(keyword))).order_by('-dateEntry')
            msg = 'Tag: '+keyword
        if not allEntries_list:
            return render_to_response('nope.html',{'tags':allTags, 'categories': allCategories, 'social': social}, context)
        paginator = Paginator(allEntries_list, 6)
        print paginator.count
        page = request.GET.get('page')
        try:
            allEntries = paginator.page(page)
        except PageNotAnInteger:
            allEntries = paginator.page(1)
        except EmptyPage:
            allEntries = paginator.page(paginator.num_pages)
        return render_to_response('entries.html', {'entradas': allEntries, 'tags':allTags, 'categories': allCategories, 'msg':msg, 'results':results ,'keyword':keyword,'type':tipo,'social': social}, context)


def seeEntry(request, id_entry):
    context = RequestContext(request)
    entrada = Entry.objects.get(idEntry=id_entry)
    allTags = Tag.objects.all().order_by('name')
    allCategories = Category.objects.all().order_by('name')
    social = Social.objects.filter(show=True)
    return render_to_response('entry.html', {'entrada': entrada, 'tags':allTags, 'categories': allCategories, 'social': social}, context)

def portfolio(request):
    context = RequestContext(request)
    allGallery = Entry.objects.annotate(num__idLinks=Count('idLinks')).filter(num__idLinks__gt=3)
    social = Social.objects.filter(show=True)
    return render_to_response('portfolio.html', {'entradas': allGallery, 'social': social}, context)

def gallery(request):
    context = RequestContext(request)
    allPort = Entry.objects.annotate(num__idLinks=Count('idLinks')).filter(num__idLinks=1)
    social = Social.objects.filter(show=True)
    return render_to_response('galeria.html', {'entradas': allPort, 'social': social}, context)

def indexation(request):
    context = RequestContext(request)
    return render_to_response('googled7cdce528f07c7ad.html', context)

def contact(request):
    social = Social.objects.filter(show=True)
    context = RequestContext(request)
    msg = False
    if request.method == 'POST':
        form_class = ContactForm(request.POST)
        if form_class.is_valid():
            contact_name = request.POST.get('contact_name', '').encode('utf-8')
            contact_email = request.POST.get('contact_email', '').encode('utf-8')
            form_content = request.POST.get('content', '').encode('utf-8')
            print (contact_name+'###'+contact_email+'###'+form_content)

            form_content_html = '''<p><strong>'''+contact_name+''' dice:</strong> '''+form_content+'''</p>'''
            contact_name = 'Adriex Designs: Mensaje de '+contact_name

            email = EmailMultiAlternatives(str(contact_name), str(form_content),str(contact_email),['adrielchagay@gmail.com'],reply_to=[str(contact_email)])
            email.attach_alternative(form_content_html, "text/html")
            email.send()
            form_class = ContactForm(auto_id=False)
            msg = 'Se ha enviado correctamente'
            return render_to_response('contacto.html',{'form': form_class, 'msg':msg, 'social': social}, context)
    else:
        form_class = ContactForm(auto_id=False)

    return render_to_response('contacto.html',{'form': form_class,'msg':msg ,'social': social}, context)
