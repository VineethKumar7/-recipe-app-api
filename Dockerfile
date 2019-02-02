FROM python:3.7-alpine
MAINTAINER Geekay Ltd

#Next we are going to set up python unbuffered environment variable
#It tells the docker to run in unbuffered mode.
#This is recommended when running the python code.
#It does't allow the python to buffer the output, it prints directly.
ENV PYTHONUNBUFFERED 1

#Note the image specified below means docker image

#Here we copy the text file from prest directory to the rext file in docker image.
COPY ./requirements.txt ./requirements.txt
#it takes the the requirements.txt from image and isntalls it using pip
RUN pip install -r requirements.txt
#Now we make the directory in the image that we can use to store to store our application software code

# Creates an empty folder inside app folder
RUN mkdir /app
# Then switches to that default directory
WORKDIR /app
# Copies the app folder in local machine to app folder created on image.
COPY ./app /app

# This is done for sequrity purposes
# Creating a user to run our applicaion using the docker.
# -D means the user for running the applications only.
#  The username is user.
RUN adduser -D user
# Switching to that user.
USER user
