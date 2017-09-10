from django.shortcuts import render, HttpResponse
from .forms import CdaForm
from .cDownloader import cDownloader


def cda(request):
    if request.method == 'POST':
        form = CdaForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            downloader = cDownloader()
            download_link = downloader.getCdaDownloadLink(url)

            context = {'download_link': download_link}
            return render(request, 'cda/download.html', context)

    else:
        form = CdaForm()

    context = {'form': form}
    return render(request, 'cda/cda.html', context)
