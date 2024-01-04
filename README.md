# PowerPoint generator with WatsonX.ai with Ansible

In this blog we are going to build a an application
to create PowerPoint slides in a EC2 instance, that is build
by using IBM watsonx Code Assistant for Red Hat Ansible Lightspeed

First we need to install Ansible VS Code extension [here](./ansible/README.md)

## Step 1 - Creation of a EC2 Instance on AWS
Here we arew going to build the AWS infrastructure by creating the yaml files to create the virtual machines.for more details go [here](./src/infra/README.md)

## Step 2 - Creation of the BackEnd
Here we are going to build the slide generator program [slide_generator.py](./src/backend/slide_generator.py) for more details go [here](./src/backend/README.md)


## Step 3- Creation of the FrontEnd
Here we create the React Application to the previous backend software.
for more details go [here](./src/frontend/README.md)