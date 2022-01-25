
# Set base image (host OS)
FROM --platform=linux/amd64 python:3.10.1
# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /main

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY tickers.csv .
COPY main.py .
COPY utilities.py .
COPY scrape_any_posts.py .
COPY scrape_hot_posts.py .
COPY scrape_new_posts.py .

# Specify the command to run on container start
CMD [ "python3", "./main.py" ]