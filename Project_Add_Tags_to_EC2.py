import boto3

# for another region please change region name and tags name, you want and run
ec2_client_mumbai = boto3.client("ec2", region_name="ap-south-1")
ec2_resource_mumbai = boto3.resource("ec2", region_name="ap-south-1")

# Creating a empty list to store instance id's
instances_id_mumbai = []

# Get Reservations Data from the instance
reservation_mumbai = ec2_client_mumbai.describe_instances()['Reservations']

for res in reservation_mumbai:
    instances = res['Instances']
    for ins in instances:
        # append instance id's in list
        instances_id_mumbai.append(ins['InstanceId'])

# For providing tags to instances
response = ec2_resource_mumbai.create_tags(
    Resources=instances_id_mumbai,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)
