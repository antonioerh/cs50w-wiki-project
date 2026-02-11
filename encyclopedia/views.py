from django.shortcuts import render
from django.http import HttpResponse
from . import util
from markdown2 import markdown



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entry_content = None
    entries_list = util.list_entries()

    for i in entries_list:
        if i.lower() == entry.lower():
            entry_content = util.get_entry(i)

    if entry_content == None:
        return HttpResponse("Error! Your requested page was not found")
    return render(request, "encyclopedia/entry.html", {
        "entry_content": markdown(entry_content)
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

        return render(request, "encyclopedia/entry.html", {
            "entry_content": markdown(entry_content)
        })  



