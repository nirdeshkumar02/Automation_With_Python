import boto3

# Note :- Create EKS Cluster Through TF

eks_client = boto3.client('eks', region_name='ap-south-1')

# printing list of eks clusters
clusters = eks_client.list_clusters()['clusters']
print(clusters)

# fetching info of each cluster
for cluster in clusters:
    # calling "describe_cluster" function which help in fetch info
    response = eks_client.describe_cluster(name=cluster)

    # cluster_status = response['cluster']['status']
    # cluster_endpoint = response['cluster']['endpoint']
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"cluster {cluster} status is {cluster_status}")
    print(f"cluster endpoint: {cluster_endpoint}")
    print(f"cluster version: {cluster_version}")
