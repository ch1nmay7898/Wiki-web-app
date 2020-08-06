from django.shortcuts import render
from django.http import HttpResponse
from markdown import markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def fetch(request, fetch):
    return render(request, "encyclopedia/entry.html", {
        "entry_md": markdown(util.get_entry(fetch)),
        "current": fetch
    })

def search(request):
    query = request.POST['q']
    entries = util.list_entries()
    res_list = []
    for entry in entries:
        if (entry == query or entry == query.capitalize() or entry == query.upper() or entry == query.lower()):
            return render(request, "encyclopedia/entry.html", {
                "entry_md": markdown(util.get_entry(entry))
            })
        else:
            if (entry.find(query) != -1 or entry.find(query.capitalize()) != -1 or entry.find(query.upper()) != -1 or entry.find(query.lower()) != -1):
                res_list.append(entry)
    if res_list:
        return render(request, "encyclopedia/results.html", {
            "res_entries": res_list
        })
    else:
        return render(request, "encyclopedia/error.html")

def create(request):
    return render(request, "encyclopedia/create.html")

def new_entry(request):
    new_md = request.POST['t']
    lines = new_md.splitlines()
    title = lines[0]
    title = title[2:]
    entries = util.list_entries()
    error = "Error: Entry already exists"
    for entry in entries:
        if (title == entry or entry == title.capitalize() or entry == title.upper() or entry == title.lower()):
            return render(request, "encyclopedia/newentry.html", {
                "newent": error
            })
    new_entry = markdown(new_md)
    util.save_entry(title, new_md)
    return render(request, "encyclopedia/newentry.html", {
        "newent": new_entry
    })

def edit(request, page):
    current = util.get_entry(page)
    return render(request, "encyclopedia/editpage.html", {
        "unedited": current
    })

def save_edit(request):
    updated_md = request.POST['t']
    lines = updated_md.splitlines()
    title = lines[0]
    title = title[2:]
    util.save_entry(title, updated_md)
    entry = util.get_entry(title)
    return fetch(request, title)

def rand(request):
    entries = util.list_entries()
    title = random.choice(entries)
    print(title)
    return fetch(request, title)