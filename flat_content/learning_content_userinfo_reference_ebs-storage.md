<p class=lead>How to add additional EBS storage to an existing EC2 instance. The following instructions can be performed in either the AWS web interface or the AWS command-line tools,</p>

# Create the EBS volume

Create the EBS volume of the appropriate size and type. Make sure you create it in the same availability zone as the instance you want to attach it to. For instance, if you have a Linux instance running in US-East-1c, then make sure to create your EBS volume in that zone.

# Attach the EBS volume

Attach your new EBS volume to your EC2 instance. You will be asked for a mount point.

# Format the EBS volume


