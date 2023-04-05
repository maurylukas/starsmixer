# start of imports
from sm import app
from flask import render_template, url_for
import os
import random
# end of imports

# loading images
path = 'sm/static/img/'
stars = os.listdir(path)
#print(stars)
#for dirpath, dirnames, filenames in os.walk('static/img'):
#    for file in filenames:
#        print(dirpath)
adams = os.listdir(path + stars[0])
amandas = os.listdir(path + stars[1])
angelinas = os.listdir(path + stars[2])
jesses = os.listdir(path + stars[3])
#random.sample(conjuntodefotos, k=numerodefotos)

#print(adam, amanda, angelina, jesse)
#adam = ['img/' + file for file in imgs]

# homepage path
@app.route ('/')
def home ():
    adam = random.choice(adams)
    amanda = random.choice(amandas)
    angelina = random.choice(angelinas)
    jesse = random.choice(jesses)
    return render_template ('home.html', adam=adam, amanda=amanda, angelina=angelina, jesse=jesse, stars=stars)
