# Case: We created 100 of EC2 Servers with Terraform and Autoscaling is configured
# Now, Write a program to check Which Instance are in which state (Running, Stopping, Terminated)?

# Create 3 EC2 Instances with Terraform
import boto3

ec2_client = boto3.client("ec2", region_name="ap-south-1")
ec2_resource = boto3.resource("ec2", region_name="ap-south-1")

# # Fetching all data from Ec2 instances running on this region
# reservations = ec2_client.describe_instances()
# print(reservations)  # Print all the details of EC2 Instances running on this region.
#
#
# # Grabbing reservation value from reservations because its a dictionary.
# # This can be execute in any state of Instance
#
# for reservation in reservations['Reservations']:
#     print(reservation["Instances"])  # Printing details of all EC2 Instances.
#     instances = reservation["Instances"]
#     for instance in instances:
#         print(instance['InstanceId'])  # Fetch Instance Id of all EC2 Instances.
#         print(instance['State'])  # Fetch State of all EC2 Instance.
#         print(instance['State']['Name'])  # Fetch Name of State of all EC2 Instance.
#         # Fetch Instance name with state-name for all instances
#         print(f"Status of Instance {instance['KeyName']} is {instance['State']['Name']}")


# Fetching Status_check and Instance State in 1 AWS API Call for Ec2 instance
# By Default, This will run only when "Instance are running"
# To run in every state of Instance, use "statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)"
statuses = ec2_client.describe_instance_status()
for status in statuses["InstanceStatuses"]:
    ins_status = status["InstanceStatus"]["Status"]
    sys_status = status["SystemStatus"]["Status"]
    state = status["InstanceState"]
    print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")


