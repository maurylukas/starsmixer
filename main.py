# start of imports
from sm import app

# end of imports

# running website
if __name__ == '__main__':
    app.run()

# before deploying use the following commands on terminal:
# 1) pip3 install gunicorn
# 2) pip3 install pipreqs
# 3) pip3 install pip-tools
# 4) pipreqs --savepath=requirements.in
# 5) pip-compile
# they will create two requirements files needed for deployment
# in the end of the requirements.txt file add this:
# gunicorn==20.1.0
# create a new file called Procfile and write within it:
# web: gunicorn main:app
