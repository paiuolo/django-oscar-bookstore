from django import template

from apps.books.models import BookStore, Serie

register = template.Library()

@register.filter(name='modulo')
def modulo(num, val):
    return num % val

@register.assignment_tag(name='bookstores')
def bookstores():
    return BookStore.objects.all()

@register.assignment_tag(name="series")
def series():
    return Serie.objects.all()