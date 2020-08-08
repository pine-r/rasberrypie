from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class BlogIndexView(View):
    def get(self, request):
        return render(request, "blog_index.html", {})
