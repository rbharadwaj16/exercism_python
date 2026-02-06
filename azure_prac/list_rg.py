import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
sub_id = input("Provide your Sub ID")

resource_client = ResourceManagementClient(credential, sub_id)

rg_result = resource_client.resource_groups.list()

for rg in rg_result:
    print(f'Name is: {rg.name}, Location is: {rg.location}')