from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .pars import Pars
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login
from .models import *
from .forms import *
from django.db.models import Q

@staff_member_required
def set_grants(request):
    pars = Pars()
    pars.do_pars()
    return HttpResponse("success")

def index( request, result = None,):
    universities = University.objects
    form2 = GrantChance()
    if request.method == "POST":
        form1 = FilterForm(request.POST)
        if form1.is_valid():
            country = form1.cleaned_data["country"]
            city = form1.cleaned_data["city"]
            type = form1.cleaned_data["type"]
            dormitary = "yes" == form1.cleaned_data["dormitary"]
            if country:
                universities = universities.filter(address__icontains=country)
            if city:
                universities = universities.filter(address__icontains =city)
            if type:
                universities = universities.filter(type = type)
            if dormitary != None:
                universities = universities.filter(dormitary = dormitary)
            universities = universities.all()
            return render(request, "guide/index.html", {"universities": universities, "form1": form1, "form2": form2, "result": result})
    universities = universities.all()
    result = request.GET.get("result")
    max = request.GET.get("max")
    min = request.GET.get("min")
    if universities:
        form1 = FilterForm()
        return render(request, "guide/index.html", {"universities": universities, "form1": form1, "form2": form2, "result": result, "max": max, "min": min})

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("guide:index"))
    else:
        form = SignUpForm()
    
    return render(request, "registration/sign_up.html", {"form": form})

def grant_chance(request):
    if request.method == "POST":
        form2 = GrantChance(request.POST)
        if form2.is_valid():
            program_code = form2.cleaned_data["program_code"]
            user_points = form2.cleaned_data["number_of_points"]
            grant = get_object_or_404(Grant, pk = program_code)
            if user_points < 0 or user_points > 140:
                result = "Bad request"
                return HttpResponseRedirect(reverse("guide:index") + f"?result={result}&max={grant.max}&min={grant.min}")
            chance = ((user_points - grant.min) / ((grant.max+grant.min)/2 - grant.min - 5)) * 100
            result = ""
            if chance >= 85:
                result = "100%. Excellent, you have very strong chances of receiving a grant."
            elif chance >= 65:
                result = str(chance)[:2] + "%. Good, you have a high chance of getting a grant."
            elif chance >= 40:
                result = str(chance)[:2] + "%. You have moderate chances of receiving a grant, but they are not small either."
            elif chance > 0:
                result = str(chance)[:2] + "%. You have low chances of receiving a scholarship, but there is still a chance."
            else:
                result = "You have very slim chances of receiving a grant, but don't get discouraged and keep trying. Luck will smile upon you."
            return HttpResponseRedirect(reverse("guide:index") + f"?result={result}&max={grant.max}&min={grant.min}")

    else:
        return HttpResponse("Bad Request", status = 404)
    
def detail(request, univ_id:int):
    if request.method == "GET":
        university = get_object_or_404(University, pk=univ_id)
        faculties = Faculty.objects.filter(univ_id = univ_id).all()
        return render(request, "guide/detail.html", {"university": university, "faculties": faculties})
    else:
        return HttpResponse("Bad request")
    
def faculty_detail(request, faculty_id: int):
    if request.method == "GET":
        faculty = get_object_or_404(Faculty, pk = faculty_id)
        programs = get_list_or_404(Program, faculty_id = faculty_id)
        return render(request, "guide/faculty_detail.html", {"faculty": faculty, "programs": programs})
    else:
        return HttpResponse("Bad request")
    
def program_detail(request, program_id: int):
    if request.method == "GET":
        program = get_object_or_404(Program, pk = program_id)
        return render(request, "guide/program_detail.html", {"program": program})
    else:
        return HttpResponse("Bad request")
login_required(login_url="/login/")
def add_favorit(request, id:int):
    if request.method == "POST":
        user = request.user
        if "add university to favorites" == request.POST.get('add to list', None):
            fav_list = FavoriteUnivList.objects.filter(user_id=user).first()
            if fav_list == None:
                fav_list = FavoriteUnivList(user_id = user)
                data = fav_list.list
                var = 0
                data[var] = id
                fav_list.list = data
                fav_list.save()
            else:
                for key, value in fav_list.list.items():
                    if value == id:
                        return HttpResponseRedirect(reverse("guide:index"))
                data = fav_list.list
                var = len(data)
                data[var] = id
                fav_list.list = data
                fav_list.save()
            return HttpResponseRedirect(reverse("guide:index"))
        if request.POST.get('add to list', None) == "add program to favorites":
            fav_list = FavoriteProgList.objects.filter(user_id=user).first()
            if fav_list == None:
                fav_list = FavoriteProgList(user_id = user)
                data = fav_list.list
                var = 0
                data[var] = id
                fav_list.list = data
                fav_list.save()
            else:
                for key, value in fav_list.list.items():
                    if value == id:
                        return HttpResponseRedirect(reverse("guide:index"))
                data = fav_list.list
                var = len(data)
                data[var] = id
                fav_list.list = data
                fav_list.save()
            return HttpResponseRedirect(reverse("guide:index"))
    else:
        return HttpResponse("Bad request")

login_required(login_url="/login/")    
def fav_univ_index(request):
    if request.method == "GET":
        user = request.user
        fav_list = get_object_or_404(FavoriteUnivList, user_id = user)
        universities = []
        for value in fav_list.list.values():
            university = University.objects.filter(pk = value).first()
            if university:
                universities.append(university)
        form = Compare()
        return render(request, "guide/fav_univ_index.html", {"universities": universities, "form": form})
    else:
        return HttpResponse("Bad request")

login_required(login_url="/login/")
def fav_prog_index(request):
    if request.method == "GET":
        user = request.user
        fav_list = get_object_or_404(FavoriteProgList, user_id = user)
        programs = []
        for value in fav_list.list.values():
            program = Program.objects.filter(pk = value).first()
            if program:
                programs.append(program)
        form = Compare()
        return render(request, "guide/fav_prog_index.html", {"programs": programs, "form": form})
    else:
        return HttpResponse("Bad request")
    
def compare(request):
    if request.method == "POST":
        form = Compare(request.POST)
        if "compare universities" == request.POST.get('compare', None):
            if form.is_valid():
                id_1 = form.cleaned_data["first_id"]
                id_2 = form.cleaned_data["second_id"]
                university_1 = get_object_or_404(University, pk = id_1)
                university_2 = get_object_or_404(University, pk = id_2)
                return render(request, "guide/compare_univ.html", {"university1": university_1, "university2": university_2})
            return HttpResponseRedirect(reverse("guide:fav_univ_index"))
        if "compare programs" == request.POST.get('compare', None):
            if form.is_valid():
                id_1 = form.cleaned_data["first_id"]
                id_2 = form.cleaned_data["second_id"]
                program_1 = get_object_or_404(Program, pk = id_1)
                program_2 = get_object_or_404(Program, pk = id_2)
                return render(request, "guide/compare_prog.html", {"program1": program_1, "program2": program_2})
            return HttpResponseRedirect(reverse("guide:fav_prog_index"))
    return HttpResponse("Bad request")