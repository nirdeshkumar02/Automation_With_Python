import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='azure_services_regions_matrix',
    KeySchema=[
        {
            'AttributeName': 'region',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'region',
            'AttributeType': 'S',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Creating Table........")

table.meta.client.get_waiter('table_exists').wait(TableName='users')

print(table.item_count)


table = dynamodb.Table('users')
print(table.creation_date_time)


