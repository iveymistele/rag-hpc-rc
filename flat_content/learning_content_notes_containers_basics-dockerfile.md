In order to serve our own webapp in a container, we will need to build an image for it. There are many "blank" images like the nginx container we pulled earlier that we can use as a starting point. This is called a base image.

To create our image, we will first write a Dockerfile. A Dockerfile is a text file containing the commands we will use to build the environment we need for our app. These are very similar to commands we would use to install libraries and packages that we need locally.

Once complete, we will use the `docker build` and `docker push` commands to build our image and upload it to DockerHub.
