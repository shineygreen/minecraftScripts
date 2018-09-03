# minecraftScripts
Scripts to manage Minecraft servers in AWS. These are simple Boto3 scripts to start and stop a server in AWS. They depend on the awscli configuration file for access keys.
##
Tools needed on a Mac
* [Brew](https://brew.sh/) is a package manager for OSx. It is a wonderful tool.
* A personal copy of Python. Never use the OSx version of Python. Install your own with "brew install python"
* The Brew python formulae should install pip. Use it to install the Amazon's command line tool [awscli](https://aws.amazon.com/cli/) "pip install awscli"
* At this point, an AWS account needs to be created. After creating the master account, use IAM to create an admin account and generate a pair of access keys for that account.
* Use "awscli configure" to create the aws configuration file. The default name for the profile in the scripts is jeanco. 
* Install boto3 with "pip install boto3"
* Clone the git repository, "git clone git@github.com:shineygreen/minecraftScripts.git"
* Create a server in AWS. Be sure to tag it with a name. The default is jeanServer.
* I have provided a systemd script to manage the minecraft server, so pick "Amazon Linux 2 AMI" for the operating system. Select a t2.small instance type. Use the default setting of 8GB for the EBS volume setting. On the "Add Tags" page, note the "click to add a Name tag" link. Use it to create a name tag. jeanServer is the default. On the "Configure Security Group" page, add a "Custom TCP rule" with the "Port Range" 25565. The "Source" should be Anywhere. Give it the description Minecraft.