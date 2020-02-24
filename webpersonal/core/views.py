from django.shortcuts import render, HttpResponse

# Create your views here.


html_base = """
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
        <li><a href="/contact/">Contact</a></li>"""



#def home(request):
#    return HttpResponse(html_base + "<h1>Mi web personal</h1><h2>Portada</h2>")

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def contact(request):
    return render(request, 'core/contact.html')