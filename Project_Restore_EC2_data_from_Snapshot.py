from operator import itemgetter

import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instance_id = ''  # provide an instance id here.

volumes = ec2_client.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])

instance_volumes = volumes['Volumes'][0]
print(instance_volumes)

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[{'Name': 'volume-id', 'Values': [instance_volumes['VolumeId']]}]
)
latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(latest_snapshot['StartTime'])

new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone='ap-south-1a',
    TagSpecification=[
        {'ResourceType': 'volume',
         'Tags':
             {'Name': 'volume-id',
              'Value': 'prod'
              }
         }
    ]
)
while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='/dev/xvdb'
        )



