from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def index(request):
	""" Landing page """

	return render(request, 'blog/index.html')


def blog(request, category=None, page=1, post=None):
	""" List of all blog posts """

	post_filter = {
		"published": True
	}
	if category is not None:
		post_filter["category__slug"] = category
	if post is not None:
		post_filter["slug"] = post

	all_posts = Post.objects.filter(**post_filter).order_by('-created_time')
	post_paginator = Paginator(all_posts, 5)

	all_categories = Category.objects.all()

	page_range_start = max(1, page - 2)
	page_range_end = min(post_paginator.num_pages + 1, page + 3)
	page_range = range(page_range_start, page_range_end)

	try:
		post_list = post_paginator.page(page)
	except EmptyPage:
		post_list = post_paginator.page(1)

	context = {
		'post_list': post_list,
		'page_range': page_range,
		'category_list': all_categories
	}

	return render(request, 'blog/posts.html', context)


def about(request):
	""" About (resume) page """

	about_post = Post.objects.get(slug='about-page', published=False)
	resume_post = Post.objects.get(slug='resume-page', published=False)

	context = {
		'about_post': about_post,
		'resume_post': resume_post
	}

	return render(request, 'blog/about.html', context)


def contact(request):
	""" Contact page """

	return render(request, 'blog/contact.html')