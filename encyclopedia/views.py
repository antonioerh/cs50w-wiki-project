from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util
from markdown2 import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "active_page": 'home'
    })

def entry(request, title):
    # Initialize the entry content variable and get entries list
    entry_content = None
    entries_list = util.list_entries()

    # Loop through all entries in the database
    for entry in entries_list:
        # Check if user's entry exists in the database
        if entry.lower() == title.lower():
            # Retrieve entry content
            entry_content = util.get_entry(entry)

    if entry_content == None:
        # Return an error page if no match
        return HttpResponse("Error! Your requested page was not found")
    return render(request, "encyclopedia/entry.html", {
        "entry_content": markdown(entry_content), "title": title
    })

def search(request):
    if request.method == "POST":
        # Retrive user's input
        query = request.POST.get("q")

        # Initialize the entry content variable and get entries list
        entry_content = None
        entries_list = util.list_entries()

        # Loop through all entries in the database
        for entry in entries_list:
            # Check if user's entry exists in the database
            if entry.lower() == query.lower():
                # Retrieve entry content
                entry_content = util.get_entry(entry)

        # Initialize entries_sublist variable
        entries_sublist = []

        # If no exact match is found
        if entry_content == None:
            # Loop through all entries in the database
            for entry in entries_list:
                # Check if user's input is a substring of any entry in the database
                if query.lower() in entry.lower():
                    # Append entry that matches the query
                    entries_sublist.append(entry)
            # Check if entries_sublist is still empty
            if entries_sublist == []:
                # Return an error page if no match
                return HttpResponse("Error! Your requested page was not found")
            else:
                # Render page with all matching entries
                return render(request, "encyclopedia/sublist.html", {
                    "entries": entries_sublist
                })

        # Redirect to entry page
        return redirect("entry", title=query)

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "active_page": 'create'
        })
    else:
        # Retrieve user's input
        title = request.POST.get("createTitle")
        content = request.POST.get("createContent")

        # Check if entry already exists in the database
        if title in util.list_entries():
            return HttpResponse("Error! Entry title already exists")
        else:
            # Save new entry to the database and redirect to the new entry page
            util.save_entry(title, content)
            return redirect("entry", title=title)

def edit(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "entry_content": util.get_entry(title), "title": title,
        })
    else:
        # Retrieve user's input
        form_title = request.POST.get("editTitle")
        content = request.POST.get("editContent")

        # Check if entry title has changed
        if form_title.lower() != title.lower():
            return HttpResponse("Error! Cannot change entry name")
        else:
            # Save new entry to the database and redirect to the new entry page
            util.save_entry(title, content)
            return redirect("entry", title=title)

def random_page(request):
    # Select a random entry
    page = random.choice(util.list_entries())

    return redirect("entry", title=page)

