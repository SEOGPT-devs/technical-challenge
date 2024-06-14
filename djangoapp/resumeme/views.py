from django.shortcuts import render, redirect
from resumeme.forms import UrlForm
from resumeme import langchain
from django.views import View
# Create your views here.


class Index(View):
    def get(self, request):
        urlform = UrlForm()
        scrapped_url = request.session.get('scrapped_url', '')

        context = {
            'resumed_content': scrapped_url,
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
            print('--------------AAAAAAAAA')
            print(valid_url)
            resume_response = langchain.scrapUrl(valid_url)
            request.session['scrapped_url'] = resume_response

        form = UrlForm()
        return redirect('/')
