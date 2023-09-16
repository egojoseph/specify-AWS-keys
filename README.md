# /usr/bin/python2.7
# written by Ego Joseph  on 29/09/2021 for Alfred and Victoria
# specify AWS keys

import boto.ec2
import sys

# specify AWS keys
auth = {"aws_access_key_id": "<key_id>", "aws_secret_access_key": "<access_key>"}

def main():
    # read arguments from the command line and 
    # check whether at least two elements were entered
    if len(sys.argv) < 2:
	print "Usage: python aws.py {start|stop}\n"
	sys.exit(0)
    else:
	action = sys.argv[1] 

    if action == "start":
	startInstance()
    elif action == "stop":
    	stopInstance()
    else:
    	print "Usage: python aws.py {start|stop}\n"

def startInstance():
    print "Starting the instance..."

    # change "eu-west-1" region if different
    try:
        ec2 = boto.ec2.connect_to_region("eu-west-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    # change instance ID appropriately  
    try:
         ec2.start_instances(instance_ids="i-12345678")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

def stopInstance():
    print "Stopping the instance..."

    try:
        ec2 = boto.ec2.connect_to_region("eu-west-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
         ec2.stop_instances(instance_ids="i-12345678")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

if __name__ == '__main__':
    main()
