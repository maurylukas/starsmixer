# start of imports
from sm import app

# end of imports

# running website
if __name__ == '__main__':
    app.run()

# before deploying use the following commands on terminal:
# 1) pip3 install pipreqs
# 2) pip3 install pip-tools
# 3) pipreqs --savepath=requirements.in
# 4) pip-compile
# they will create two requirements files needed for deployment
