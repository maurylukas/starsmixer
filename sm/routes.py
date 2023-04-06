# start of imports
from sm import app
from flask import render_template, request, json, url_for
import os
import random

# end of imports

# getting folders
origin_path = 'sm/static/img/origin/'
stars = os.listdir(origin_path)

mixed_path = 'sm/static/img/mixed/'
mixes = os.listdir(mixed_path)

# loading images
adams = os.listdir(origin_path + stars[0])
amandas = os.listdir(origin_path + stars[1])
angelinas = os.listdir(origin_path + stars[2])
jesses = os.listdir(origin_path + stars[3])

mix_adam_amanda = os.listdir(mixed_path + mixes[0])
mix_adam_angelina = os.listdir(mixed_path + mixes[1])
mix_adam_jesse = os.listdir(mixed_path + mixes[2])
mix_amanda_angelina = os.listdir(mixed_path + mixes[3])
mix_amanda_jesse = os.listdir(mixed_path + mixes[4])
mix_angelina_jesse = os.listdir(mixed_path + mixes[5])


# defining function
def mix_images(star1, star2):
    for name in mixes:
        if star1 in name:
            if star2 in name:
                results = os.listdir(mixed_path + mixes[name])
    return random.sample(results, k=8)


# print(adam, amanda, angelina, jesse)
# adam = ['img/' + file for file in imgs]

# homepage path
@app.route('/')
def home():
    adam = random.choice(adams)
    amanda = random.choice(amandas)
    angelina = random.choice(angelinas)
    jesse = random.choice(jesses)

    adam_amanda = random.sample(mix_adam_amanda, k=8)
    adam_angelina = random.sample(mix_adam_angelina, k=8)
    adam_jesse = random.sample(mix_adam_jesse, k=8)
    amanda_angelina = random.sample(mix_amanda_angelina, k=8)
    amanda_jesse = random.sample(mix_amanda_jesse, k=8)
    angelina_jesse = random.sample(mix_angelina_jesse, k=8)

    list_mixes = [adam_amanda, adam_angelina, adam_jesse, amanda_angelina, amanda_jesse, angelina_jesse]

    return render_template(
        'home.html', adam=adam, amanda=amanda, angelina=angelina, jesse=jesse, stars=stars,
        mixes=json.dumps(mixes), adam_amanda=adam_amanda, adam_angelina=adam_angelina, adam_jesse=adam_jesse,
        amanda_angelina=amanda_angelina, amanda_jesse=amanda_jesse, angelina_jesse=angelina_jesse,
        list_mixes=json.dumps(list_mixes)
    )


# returning images
@app.route('/get_mix', methods=['POST'])
def get_mix():
    star1 = request.form['star1']
    star2 = request.form['star2']

    # Load and mix the images
    mixed_images = mix_images(star1, star2)
    mixed_images = ["/static/img/mixed/" + filename for filename in mixed_images]

    # Return the filenames of the mixed images as a JSON string
    return json.dumps(mixed_images)
