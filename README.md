# minecraftScripts
Scripts to manage Minecraft servers in AWS. These are simple Boto3 scripts to start and stop a server in AWS. They depend on the awscli configuration file for access keys.
##
Steps needed on a Mac
* [Brew](https://brew.sh/) is a package manager for OSx. It is a wonderful tool.
* Never use the OSx version of Python. Install your own with "brew install python"
* The Brew python formulae should install pip. Use it to install the Amazon's command line tool [awscli](https://aws.amazon.com/cli/), "pip install awscli"
* At this point, an AWS account needs to be created. After creating the master account, use IAM to create an admin account and generate a pair of access keys for that account.
* Use "awscli configure" to create the aws configuration file. The default name for the profile in the scripts is jeanco. 
* Install boto3 with "pip install boto3"
* Clone the git repository, "git clone git@github.com:shineygreen/minecraftScripts.git"
* Create a server in AWS. Be sure to tag it with a name. The default is jeanServer.
* I have provided a systemd script to manage the minecraft server, so pick "Amazon Linux 2 AMI" for the operating system. Select a t2.small instance type. Use the default setting of 8GB for the EBS volume setting. On the "Add Tags" page, note the "click to add a Name tag" link. Use it to create a name tag. jeanServer is the default. On the "Configure Security Group" page, add a "Custom TCP rule" with the "Port Range" 25565. The "Source" should be Anywhere. Give it the description Minecraft. When the instance is created, download the private key somewhere safe. Change the permissions on the key with "chmod 0600 mykey.pem".
* Run the startServer.py script to get the IP address of the server. (Don't worry that the server is already running.)
* Login to the server with "ssh -i mykey.pem ec2-user@IP_ADDRESS"
* From the repository, copy the minecraft.service file to the new server, "scp -i minecraft.service ec2-user@IP_ADDRESS:/tmp"
* On the server, copy the service file to the correct location, "sudo cp /tmp/minecraft.service /etc/systemd/system"
* Enable the service "systemd enable minecraft.service"
* Create a directory called minecraft, "mkdir /usr/local/games/minecraft"
* Download the [Minecraft jar file](https://minecraft.net/en-us/download/server) and put it in the minecraft directory.
* Create a minecraft user: adduser -c "Minecraft Server" -s /sbin/nologin minecraft
* Change ownership of the minecraft directory, "chown -R minecraft.minecraft /usr/local/games/minecraft"
* Drop the Minecraft configuration files into /usr/local/games/minecraft, make sure they are owned by minecraft.
* Try to start the server with "systemctl start minecraft"