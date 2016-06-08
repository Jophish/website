import pystache
import markdown
import os
import random
from colour import Color

renderer = pystache.Renderer(search_dirs=["templates/", "assets/html/"], file_extension = None)
renderer.load_template('site_template')

files = os.listdir('./md') #list of md files to convert to html

postList = []

for file in files:
    with open('md/'+file, 'r') as myfile:
        postList.append(myfile.read())



class basicPage(object):
    def about(self):
        return 'a b o u t'
    def posts(self):
        return 'p o s t s'
    def projects(self):
        return 'p r o j e c t s'
    
def render_about():
    renderer.load_template('site_template')
    with open('assets/html/about.html', 'r') as myfile:
        about_template = myfile.read()
        
        class _siteTemplate(basicPage):
            def about(self):
                return '|a b o u t|'
            def siteBody(self):
                return str(about_template)
            
        rendered_about = open("about.html", "w+")
        rendered_about.write(renderer.render(_siteTemplate()))
        rendered_about.close()

def render_index():
    bodyString = ""
    renderer.load_template('post_entry')

    r = lambda: random.randint(0,255)
    init_col = Color(hsl=(0, .5, .7))
    inc = .05    
    for post in files:
        class _postEntry(object):
            def color(self):
                return init_col.hex
            def title(self):
                return post
        init_col = Color(hsl = (init_col.hsl[0]+ inc, .5,.7))
        bodyString += renderer.render(_postEntry())

    class _siteTemplate(basicPage):
            def posts(self):
                return '|p o s t s|'
            def siteBody(self):
                return bodyString
    renderer.load_template('site_template')
    rendered_about = open("index.html", "w+")
    rendered_about.write(renderer.render(_siteTemplate()))
    rendered_about.close()
            

    
    
render_about()
render_index()
