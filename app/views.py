from django.shortcuts import render
import wikipedia
# Create your views here.


def wiki(request):
    if request.method=='POST':
        search=request.POST['search']
        print(search)
        search_results = wikipedia.search(search)
        if search_results:
            article_summary=wikipedia.summary(search)
            print(article_summary)
            return render(request,'wiki.html',{'data':article_summary})
        else:
           print("No search results found.")
    return render(request,'wiki.html')

