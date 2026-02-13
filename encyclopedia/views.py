from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util
from markdown2 import markdown
import random

def index(request):
    # Render home page
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "active_page": 'home'
    })

def entry(request, title):
    # 
    entry_content = None
    entries_list = util.list_entries()

    for entry in entries_list:
        if entry.lower() == title.lower():
            entry_content = util.get_entry(entry)

    if entry_content == None:
        return HttpResponse("Error! Your requested page was not found")
    return render(request, "encyclopedia/entry.html", {
        "entry_content": markdown(entry_content), "title": title
    })

def search(request):
    if request.method == "POST":
        query = request.POST.get("q")

        entry_content = None
        entries_list = util.list_entries()

        for entry in entries_list:
            if entry.lower() == query.lower():
                entry_content = util.get_entry(entry)

        entries_sublist = []

        if entry_content == None:
            for entry in entries_list:
                if query.lower() in entry.lower():
                    entries_sublist.append(entry)
            if entries_sublist == None:
                return HttpResponse("Error! Your requested page was not found")
            else:
                return render(request, "encyclopedia/sublist.html", {
                    "entries": entries_sublist
                })

        return redirect("entry", title=query)

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "active_page": 'create'
        })
    else:
        title = request.POST.get("createTitle")
        content = request.POST.get("createContent")

        if title in util.list_entries():
            return HttpResponse("Error! Entry title already exists")
        else:
            util.save_entry(title, content)
            return redirect("entry", title=title)

def edit(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "entry_content": util.get_entry(title), "title": title,
        })
    else:
        form_title = request.POST.get("editTitle")
        content = request.POST.get("editContent")

        if form_title != title:
            return HttpResponse("Error! Cannot change entry name")
        else:
            util.save_entry(title, content)
            return redirect("entry", title=title)

def random_page(request):
    page = random.choice(util.list_entries())

    return redirect("entry", title=page)

