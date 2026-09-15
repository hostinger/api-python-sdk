# HostingV1GitGitRepositoryResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Repository identifier assigned by the Git provider | 
**name** | **str** | Repository name without the .git suffix | 
**full_name** | **str** | Owner and repository name joined with a slash | 
**owner** | **str** | Repository owner login | 
**is_private** | **bool** | Whether the repository is private | 
**html_url** | **str** | Repository page URL | 
**clone_url** | **str** | HTTPS clone URL | 
**default_branch** | **str** | Default branch of the repository | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_repository_resource import HostingV1GitGitRepositoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitRepositoryResource from a JSON string
hosting_v1_git_git_repository_resource_instance = HostingV1GitGitRepositoryResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitRepositoryResource.to_json())

# convert the object into a dict
hosting_v1_git_git_repository_resource_dict = hosting_v1_git_git_repository_resource_instance.to_dict()
# create an instance of HostingV1GitGitRepositoryResource from a dict
hosting_v1_git_git_repository_resource_from_dict = HostingV1GitGitRepositoryResource.from_dict(hosting_v1_git_git_repository_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


