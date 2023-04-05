# start of imports
from sm import app
from flask import render_template, url_for
# end of imports

# homepage path
@app.route ('/')
def home ():
    return render_template ('home.html')
