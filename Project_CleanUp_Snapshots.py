from operator import itemgetter

import boto3

ec2_client = boto3.client('ec2', region_name='ap-south-1')

# accessing snapshots
snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
# sort the snapshots according to date
sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
print(sorted_by_date)

# # Fetch StartTime of snapshots
# for snap in snapshots['Snapshots']:
#     print(snap['StartTime'])
# print('########################')
#
# # Print StartTime in ascending order.
# for snap in sorted_by_date:
#     print(snap['StartTime'])
#
# # print the snapshots
# print(snapshots['Snapshots'])

for snap in sorted_by_date[1:]:
    response = ec2_client.delete_snapshot(SnapshotId = snap['SnapshotId'])
    print(response)
