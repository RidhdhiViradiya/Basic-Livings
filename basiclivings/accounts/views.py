from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import City, Area, User
from django.contrib.auth.models import auth
import json
# Create your views here.

# json_data = json.dumps(cities)
#
# print(json_data[:4])


def convert_cities_to_json():
    cities = City.objects.all()

    # cities = City.objects.all()

    myList = []
    for city in cities:
        tup = (city.city_id, city.city_name)
        myList.append(tup)

    json_data = json.dumps(myList)
    with open('accounts/cities_list.json', 'w') as fh:
        fh.write(json_data)

    # print(json_data)


def convert_areas_to_json():
    areas = Area.objects.all()

    # cities = City.objects.all()

    myList = []
    for area in areas:
        tup = (area.area_id, area.area_name, area.city_id)
        myList.append(tup)

    json_data = json.dumps(myList)
    with open('accounts/areas_list.json', 'w') as fh:
        fh.write(json_data)

    # print(json_data)


def index(request):
    cities = City.objects.all()
    # convert_cities_to_json()
    # convert_areas_to_json()

    return render(request, 'accounts/index.html', {'cities': cities})


def register(request):
    print('Ntredddddd Mthod')
    cities = City.objects.all()
    if request.method == 'POST':
        print('Ntre Mthod')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        usertype = request.POST['usertype']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        city = int(request.POST['city'])
        area = int(request.POST['area'])
        is_student = 1
        is_foodVendor = 0
        is_pgVendor = 0
        if usertype == 1:
            is_student = 1
            is_foodVendor = 0
            is_pgVendor = 0
        elif usertype == 2:
            is_foodVendor = 1
            is_student = 0
            is_pgVendor = 0
        elif usertype == 3:
            is_pgVendor = 1
            is_student = 0
            is_foodVendor = 0
        myDict = {'message': "Email Already Exists!!", 'cities': cities, 'first_name': first_name, 'last_name': last_name, 'usertype': usertype, 'gender': gender, 'phone': phone, 'address': address, 'city': city, 'area': area}
        if User.object.filter(email=email).exists():
            print("Exists")
            return render(request, 'accounts/index.html', myDict)
        else:
            areas = Area.objects.get(area_id=area)
            user = User.object.create_user(first_name, last_name, email, password, gender, address, phone, is_pgVendor, is_foodVendor, is_student, areas)
            user.save()
            print("User Created")
            return redirect('/accounts/')

        return redirect('/accounts/')

    else:
        return redirect('/accounts/')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            next = request.POST.get('next', '/')
            return redirect(next)
        else:
            messages.info(request, 'Invalid Credentials!!')
            return redirect('/accounts/')
    else:
        return render(request, 'accounts/index.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/accounts/')


def area_handle(request):
    print("mthod alled")
    areas = int(request.POST['id'])
    print(areas)
    areas_list = Area.objects.filter(city_id=areas)
    print("Gathered")
    print(areas_list)
    myList = []
    for area in areas_list:
        tup = (area.area_id, area.area_name)
        myList.append(tup)

    print(myList)
    json_data = json.dumps(myList)
    print(json_data)
    return HttpResponse(json_data)


