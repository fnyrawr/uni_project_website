from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .forms import BlogForm, SearchForm
from .models import Blog, BlogImage


def blogpost_list(request):
    all_blogposts = None
    blogposts_found = None
    search = False
    searchForm = SearchForm
    if request.method == "POST":
        search = True
        searchForm = SearchForm(request.POST)
        data = searchForm.data
        title = data['title']
        content = data['content']
        if title or content:
            blogposts_found = Blog.objects
            if title:
                blogposts_found = blogposts_found.filter(title__contains=title)
            if content:
                blogposts_found = blogposts_found.filter(content__contains=content)
    else:
        all_blogposts = Blog.objects.all()

    context = {'all_blogposts': all_blogposts,
               'blogposts_found': blogposts_found,
               'search': search,
               'form': searchForm, }
    return render(request, 'blogpost-list.html', context)


class BlogpostCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogpost-create.html'

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            images = request.FILES.getlist('images')

            for image in images:
                BlogImage.objects.create(blogpost=blogpost, image=image)

            return redirect('blogpost-detail', pk=blogpost.id)

    def form_valid(self, form):
        return super().form_valid(form)


class BlogpostDeleteView(DeleteView):
    model = Blog
    context_object_name = 'that_one_blogpost'
    template_name = 'blogpost-delete.html'
    success_url = reverse_lazy('blogpost-list')

    def post(self, request, **kwargs):
        blogpost_id = kwargs['pk']
        blogpost = Blog.objects.get(id=blogpost_id)
        blogpost.delete()
        return redirect('blogpost-list')


def blogpost_detail(request, **kwargs):
    blogpost_id = kwargs['pk']
    blogpost = Blog.objects.get(id=blogpost_id)
    is_authorized = False
    user = request.user
    images = BlogImage.objects.filter(blogpost=blogpost)
    if not user.is_anonymous:
        is_authorized = user.is_authorized()
    context = {
        'that_one_blogpost': blogpost,
        'blogpost_images': images,
        'is_authorized': is_authorized, }
    return render(request, 'blogpost-detail.html', context)


def blogpost_edit(request, **kwargs):
    blogpost_id = kwargs['pk']
    blogpost = Blog.objects.get(id=blogpost_id)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        data = form.data
        images = request.FILES.getlist('images')
        Blog.objects.filter(
            id=blogpost_id).update(title=data['title'], content=data['content'])
        for image in images:
            BlogImage.objects.create(blogpost=blogpost, image=image)
        return redirect('blogpost-detail', pk=kwargs['pk'])
    else:  # request.method == 'GET'
        form = BlogForm()
        images = BlogImage.objects.filter(blogpost=blogpost)
        context = {'form': form,
                   'blogpost': blogpost,
                   'images': images}
        return render(request, 'blogpost-edit.html', context)


def image_delete(request, **kwargs):
    image_id = kwargs['id']
    image = BlogImage.objects.get(id=image_id)
    image.image.delete()
    image.delete()
    return redirect('blogpost-edit', pk=kwargs['pk'])
