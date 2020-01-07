from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from .models import *
from keys import cnv_id, cnv_key
import random


id = cnv_id
key = cnv_key
headers = {
    'Accept': 'application/json',
}
params = (
    ('app_id', id),
    ('app_key', key),
)

def index(request):
    return render(request, "nonprofit_search/index1.html")

def main(request):
    return redirect("/search")

def details (request,nonprofit_id):
    response = requests.get(f'https://api.data.charitynavigator.org/v2/Organizations/{nonprofit_id}?', headers = headers, params = params)
    pro_response = requests.get(f'https://projects.propublica.org/nonprofits/api/v2/organizations/{nonprofit_id}.json')
    this_user = User.objects.get(id = request.session["user_id"])
    pro_nonprofit = pro_response.json()
    year1rev = pro_nonprofit['filings_with_data'][0]['totrevenue']
    year2rev = pro_nonprofit['filings_with_data'][1]['totrevenue']
    year3rev = pro_nonprofit['filings_with_data'][2]['totrevenue']
    year1exp = pro_nonprofit['filings_with_data'][0]['totfuncexpns']
    year2exp = pro_nonprofit['filings_with_data'][1]['totfuncexpns']
    year3exp = pro_nonprofit['filings_with_data'][2]['totfuncexpns']
    context = {
        "c_nav_nonprofit" : response.json(),
        "pro_nonprofit" : pro_response.json(),
        "np_ein": nonprofit_id,
        "user" : this_user,
        "year1final" : year1rev - year1exp,
        "year2final" : year2rev - year2exp,
        "year3final" : year3rev - year3exp,
        }
    return render(request, "nonprofit_search/template_details.html", context)

def account(request):
    user_id = request.session["user_id"]
    this_user = User.objects.get(id = user_id)
    context = {
        "my_nonprofits": this_user.nonprofits.all(),
        "user": this_user

    }
    return render(request, "nonprofit_search/template_account.html", context)

def search(request):
    cnav_response = requests.get('https://api.data.charitynavigator.org/v2/Categories', headers=headers, params=params)
    random_bank = requests.get('https://api.data.charitynavigator.org/v2/Organizations?pageSize=200&rated=true&state=CA', headers = headers, params = params)
    rd_list = random_bank.json()
    num = random.randint(0,199)
    random_np_selected = rd_list[num]            
    context = {
        "categories" : cnav_response.json(),
        "random_npo" : random_np_selected,
        "user" : User.objects.get(id = request.session["user_id"])
    }
    return render(request, "nonprofit_search/template_search.html", context)

def search_results(request):
    form = request.GET
    name = form["name"]
    state = form["state"]
    city = form["city"]
    category = form["category"]
    response = requests.get(f'https://api.data.charitynavigator.org/v2/Organizations?pageSize=40&search={name}&categoryID={category}&state={state}&city={city}', headers=headers, params=params)
    charity_list = response.json()
    new_list = []
    count = 0
    if 'errorMessage' in charity_list:
        context = {
            "message":"No results for your search. Please try again"
        }
        return render(request, "nonprofit_search/template_search_results.html", context)
    else:
        for charity in charity_list:
            if charity["irsClassification"]["subsection"] == "501(c)(3)":
                count +=1
                new_list.append(charity)
            if count == 20:
                break
    context = {
        "nonprofit_list": new_list
        }
    return render(request, "nonprofit_search/template_search_results.html", context)

def add_list(request, nonprofit_id):
    response = requests.get(f'https://api.data.charitynavigator.org/v2/Organizations/{nonprofit_id}?', headers = headers, params = params)
    user = User.objects.get(id = request.session["user_id"])
    cnav = response.json()
    np_name = cnav["charityName"]
    if "category" in cnav:
        np_cat = cnav['category']['categoryName'] 
    else:
        np_cat = "Other"
    if cnav['websiteURL'] == None:
        np_site = f"http://www.google.com/search?q={np_name}"
    else: 
        np_site = cnav['websiteURL']
    this_nonprofit = Nonprofit.objects.create(name = np_name, ein = nonprofit_id, city = cnav["mailingAddress"]["city"], state = cnav["mailingAddress"]["stateOrProvince"], impact = np_cat, website = np_site)
    user.nonprofits.add(this_nonprofit)
    return redirect ("/account")

def remove_list(request, nonprofit_id):
    this_user = User.objects.get(id = request.session["user_id"])
    this_nonprofit = Nonprofit.objects.get(ein = nonprofit_id)
    this_user.nonprofits.remove(this_nonprofit)
    return redirect ("/account")

def remove_list_details(request, nonprofit_id):
    this_user = User.objects.get(id = request.session["user_id"])
    this_nonprofit = Nonprofit.objects.get(ein = nonprofit_id)
    this_user.nonprofits.remove(this_nonprofit)
    return redirect (f"/details/{nonprofit_id}")