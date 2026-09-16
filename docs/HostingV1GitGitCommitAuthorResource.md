# HostingV1GitGitCommitAuthorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Author name as recorded in the commit | 
**avatar_url** | **str** | Avatar URL of the author on the Git provider | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_commit_author_resource import HostingV1GitGitCommitAuthorResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitCommitAuthorResource from a JSON string
hosting_v1_git_git_commit_author_resource_instance = HostingV1GitGitCommitAuthorResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitCommitAuthorResource.to_json())

# convert the object into a dict
hosting_v1_git_git_commit_author_resource_dict = hosting_v1_git_git_commit_author_resource_instance.to_dict()
# create an instance of HostingV1GitGitCommitAuthorResource from a dict
hosting_v1_git_git_commit_author_resource_from_dict = HostingV1GitGitCommitAuthorResource.from_dict(hosting_v1_git_git_commit_author_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


