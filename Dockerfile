# Use an official Python runtime as a base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define the command to run your application
CMD ["python", "app.py"]