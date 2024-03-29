import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page

def populate():
    
    python_pages = [
        {'title' : 'Official Python Tutorial',
         'views' : 3, 
         'url' : 'http://docs.python.org/3/tutorial/'},
        
        {'title' : 'How to Think like a Computer Scientist',
         'views' : 10,
         'url' : 'http://www.greenteapress.com/thinkpython/'},
        
        {'title' : 'Learn Python in 10 Minutes',
         'views' : 12,
         'url':'http://www.korokithakis.net/tutorials/python/'}]
    
    django_pages = [
        
        {'title':'Official Django Tutorial',
         'views' : 9,
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        
        {'title':'Django Rocks',
         'views' : 54,
         'url':'http://www.djangorocks.com/'},
        
        {'title':'How to Tango with Django',
         'views' : 98,
         'url':'http://www.tangowithdjango.com/'} ]
    
    other_pages = [

        {'title':'Bottle',
         'views' : 8,
         'url':'http://bottlepy.org/docs/dev/'},
        
        {'title':'Flask',
         'views' : 18,
         'url':'http://flask.pocoo.org'} ]
    
    cats = {'Python': {
                "views": 8,
                "likes": 13,
                "pages": python_pages},
            
            'Django': {
                "views": 14,
                "likes": 5,
                "pages": django_pages},
            
            'Other Frameworks': {
                "views": 10,
                "likes": 2,
                "pages": other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('- {0} - {1}'.format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p


def add_cat(name, views, likes):
    print(name, views)
    c =  Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()



        
    

        
