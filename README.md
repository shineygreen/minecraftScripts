# minecraftScripts
Scripts to manage Minecraft servers in AWS. These are simple Boto3 scripts to start and stop a server in AWS. They depend on the awscli configuration file for access keys.
##
Tools needed on a Mac
* [Brew](https://brew.sh/) is a package manager for OSx. It is a wonder thing.
* A personal copy of Python. Never use the OSx version of Python. Install your own with
** brew install python
* The Brew python formulae should install pip. Use it to install the awscli
** pip install awscli
* At this point, an AWS account needs to be created. Use IAM to create an account and generate a pair of access keys for the account.
* Use "awscli configure" to create the aws configuration file. The default name for the profile in the scripts is jeanco. 
* Install boto3 with "pip install boto3"
* Clone the git repository
* Create a server in AWS. Be sure to tag it with a name. The default is jeanServer.
** I use a 
