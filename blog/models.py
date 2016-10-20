from django.db import models

from redactor.fields import RedactorField
from taggit.managers import TaggableManager

import datetime

# The blog post model
class Post(models.Model):
	title = models.CharField(max_length=100, null=True)
	text = RedactorField(
		redactor_options={
		'autosave': '/blog/admincontent/saved/',
		'autosaveName': 'blog-text',
		'focus': True
		},
		upload_to='/blog/media/upload/',
		allow_file_upload=True,
		allow_image_upload=True)
	created_time = models.DateTimeField(default=datetime.datetime.now)
	last_modified_time = models.DateTimeField(default=datetime.datetime.now)
	published = models.BooleanField(default=False)
	category = models.ForeignKey(
		'Category',
		null=True,
		)
	slug = models.SlugField(allow_unicode=True, null=True)
	tags = TaggableManager()

	class Meta:
		ordering = ['-created_time']

# Post category
class Category(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'categories'

# Files associated with blog posts
# http://paltman.com/how-to-setup-upload-handler-for-redactor/
class File(models.Model):
	upload = models.FileField(upload_to='/blog/media/upload/')
	created_time = models.DateTimeField(default=datetime.datetime.now)
	is_image = models.BooleanField(default=True)