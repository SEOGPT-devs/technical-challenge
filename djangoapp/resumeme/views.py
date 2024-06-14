from django.shortcuts import render, redirect
from resumeme.forms import UrlForm
from django.views import View
# Create your views here.


class Index(View):
    def get(self, request):
        urlform = UrlForm()
        context = {
            'form': urlform,
        }

        return render(
            request,
            'resumeme/pages/index.html',
            context
        )

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            valid_url = form.cleaned_data['to_be_scrapped']
            print(valid_url)

        form = UrlForm()

        context = {
            'form': form
        }

        return redirect(
            '/',
        )
