from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def index(request):
	return render(request, 'blog/index.html')


def blog(request, page=1):
	all_posts = Post.objects.filter(published=True).order_by('-created_time')
	post_paginator = Paginator(all_posts, 5)

	page_range_start = max(1, page - 2)
	page_range_end = min(post_paginator.num_pages + 1, page + 3)
	page_range = range(page_range_start, page_range_end)

	try:
		post_list = post_paginator.page(page)
	except EmptyPage:
		post_list = post_paginator.page(1)

	context = {
		'post_list': post_list,
		'page_range': page_range
	}

	return render(request, 'blog/posts.html', context)