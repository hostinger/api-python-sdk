# HostingV1GitGitCommitResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Full commit SHA | 
**message** | **str** | Commit message | 
**author** | [**HostingV1GitGitCommitAuthorResource**](HostingV1GitGitCommitAuthorResource.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_commit_resource import HostingV1GitGitCommitResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitCommitResource from a JSON string
hosting_v1_git_git_commit_resource_instance = HostingV1GitGitCommitResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitCommitResource.to_json())

# convert the object into a dict
hosting_v1_git_git_commit_resource_dict = hosting_v1_git_git_commit_resource_instance.to_dict()
# create an instance of HostingV1GitGitCommitResource from a dict
hosting_v1_git_git_commit_resource_from_dict = HostingV1GitGitCommitResource.from_dict(hosting_v1_git_git_commit_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


