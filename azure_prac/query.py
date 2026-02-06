import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
sub_id = input("Provide your Sub ID")

Resource = ResourceManagementClient(credential, sub_id)


