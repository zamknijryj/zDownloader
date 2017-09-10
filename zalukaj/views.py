from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ZalukajForm
from .guess import zDownloader


def zalukaj(request):
    if request.method == 'POST':
        form = ZalukajForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            downloader = zDownloader()
            download_link = downloader.getDownloadLink(url)

            context = {'download_link': download_link}
            return render(request, 'zalukaj/download.html', context)

    else:
        form = ZalukajForm()

    context = {'form': form}
    return render(request, 'zalukaj/zalukaj.html', context)
