# CA5

# How to Setup Jenkins Server for Multibranch Pipeline that Builds, Tags, and Pushes docker images to Docker Hub

# Build Jenkins_Docker Image
First, build the docker image using following command:

```
docker build -t custom-jenkins-docker .
```

# Run the Jenkins_Docker Container
Then, you have to run the container using the jenkins_docker image

```
docker run -it -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home custom-jenkins-docker
```

# Access Jenkins Server Dashboard to Create MultiBranch Pipeline
- Now, navigate to localhost:8080.
- Create a multibranch pipeline.
- Enter your github repository url and save.
- The Jenkins Server will can your repository and for each branch that it will find a Jenkinsfile, it will automatically schedule a build based on the Jenkinsfile in that repository.
