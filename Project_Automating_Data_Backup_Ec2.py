import boto3
import schedule

# Note :- Create Ec2 Instance

# Calling Client
ec2_client = boto3.client('ec2', region_name='ap-south-1')


def backup():
    # To Call Volume, use "describe_volumes" function. It will take backup of all ec2.
    # If u want to take backup specifically, Then use "Filter" in "describe_volumes()"
    # For Example - using Tag we can filter the ec2.
    volumes = ec2_client.describe_volumes()['Volumes']
    print(volumes)  # Print the volumes
    # To create back up, we need to take a snapshot of volumes
    for volume in volumes:
        snapshot = ec2_client.create_snapshot(VolumeId=volume['VolumeId'])
        print(snapshot)


# Taking Backup EveryDay
schedule.every().day.do(backup)
while True:
    schedule.run_pending()
