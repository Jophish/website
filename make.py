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
    cssString = ""
    
    renderer.load_template('post_entry')
    
    r = lambda: random.randint(0,255)
    init_col = Color(hsl=(0, .5, .7))
    inc = .05
    count = 1;
    for post in files:
        class _postEntry(object):

            def title(self):
                return post
            def number(self):
                return str(count)
        
        bodyString += renderer.render(_postEntry())
        

        renderer.load_template('custom_colors')

        class _customColors(object):
            def color(self):
                return  Color(hsl = (init_col.hsl[0], .9, .8)).hex
            def id(self):
                return str(count)
            def firstColor(self):
                return init_col.hex
            
                    
        cssString += renderer.render(_customColors())
                    
        count += 1;
        init_col = Color(hsl = (init_col.hsl[0]+ inc, .5,.7))

    class _siteTemplate(basicPage):
            def posts(self):
                return '|p o s t s|'
            def siteBody(self):
                return bodyString
    renderer.load_template('site_template')
    rendered_about = open("index.html", "w+")
    rendered_about.write(renderer.render(_siteTemplate()))
    rendered_about.close()
    rendered_customColors = open("assets/css/custom_colors.css", "w+")
    rendered_customColors.write(cssString)
    rendered_customColors.close()
            

    
    
render_about()
render_index()
