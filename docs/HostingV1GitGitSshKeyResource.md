# HostingV1GitGitSshKeyResource

Public SSH key the hosting account uses to clone and pull Git repositories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | Public key to add as a deploy key on the Git host. Null when the account has no key yet. | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_ssh_key_resource import HostingV1GitGitSshKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitSshKeyResource from a JSON string
hosting_v1_git_git_ssh_key_resource_instance = HostingV1GitGitSshKeyResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitSshKeyResource.to_json())

# convert the object into a dict
hosting_v1_git_git_ssh_key_resource_dict = hosting_v1_git_git_ssh_key_resource_instance.to_dict()
# create an instance of HostingV1GitGitSshKeyResource from a dict
hosting_v1_git_git_ssh_key_resource_from_dict = HostingV1GitGitSshKeyResource.from_dict(hosting_v1_git_git_ssh_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


