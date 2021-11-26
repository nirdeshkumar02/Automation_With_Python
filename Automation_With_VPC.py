# Playing with vpc
import boto3

# Create new VPC and Subnets
ec2_resource = boto3.resource("ec2")

new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)
new_vpc.create_tags(
    Tags=[{
        "Key": "Name",
        "Value": "MyVPC"
    }]
)

# List of all VPC and Play with it

ec2_client = boto3.client("ec2", region_name="eu-central-1")
all_available_vpc = ec2_client.describe_vpcs()
# 1. Get list of vpc in region configure with cli
print(all_available_vpc)
# 2. Print vpc id, cidr block etc
vpcs = all_available_vpc["Vpcs"]
for vpc in vpcs:
    print(vpc["VpcId"])
    print(vpc["CidrBlockAssociationSet"])
    # Looping Inside CidrBlock
    cidr_block_set = vpc["CidrBlockAssociationSet"]
    for cidr_block in cidr_block_set:
        print(cidr_block["CidrBlockState"])

