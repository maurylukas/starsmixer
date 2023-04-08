# start of imports
from sm import app
from flask import render_template, json, url_for
import os
import random

# end of imports

# getting folders
origin_path = 'sm/static/img/origin/'
stars = os.listdir(origin_path)
stars.sort()

mixed_path = 'sm/static/img/mixed/'
mixes = os.listdir(mixed_path)

# loading original images
adams = os.listdir(origin_path + stars[0])
amandas = os.listdir(origin_path + stars[1])
angelinas = os.listdir(origin_path + stars[2])
jesses = os.listdir(origin_path + stars[3])

# loading mixed images
mix_adam_amanda = os.listdir(mixed_path + mixes[0])
mix_adam_angelina = os.listdir(mixed_path + mixes[1])
mix_adam_jesse = os.listdir(mixed_path + mixes[2])
mix_amanda_angelina = os.listdir(mixed_path + mixes[3])
mix_amanda_jesse = os.listdir(mixed_path + mixes[4])
mix_angelina_jesse = os.listdir(mixed_path + mixes[5])


# homepage path
@app.route('/')
def home():
    # choosing one image randomly
    adam = random.choice(adams)
    amanda = random.choice(amandas)
    angelina = random.choice(angelinas)
    jesse = random.choice(jesses)

    # choosing 8 images randomly
    adam_amanda = random.sample(mix_adam_amanda, k=8)
    adam_angelina = random.sample(mix_adam_angelina, k=8)
    adam_jesse = random.sample(mix_adam_jesse, k=8)
    amanda_angelina = random.sample(mix_amanda_angelina, k=8)
    amanda_jesse = random.sample(mix_amanda_jesse, k=8)
    angelina_jesse = random.sample(mix_angelina_jesse, k=8)

    list_mixes = [adam_amanda, adam_angelina, adam_jesse, amanda_angelina, amanda_jesse, angelina_jesse]

    return render_template(
        'home.html', adam=adam, amanda=amanda, angelina=angelina, jesse=jesse, stars=stars, mixes=json.dumps(mixes),
        adam_amanda=adam_amanda, adam_angelina=adam_angelina, adam_jesse=adam_jesse, amanda_angelina=amanda_angelina,
        amanda_jesse=amanda_jesse, angelina_jesse=angelina_jesse, list_mixes=json.dumps(list_mixes)
    )
