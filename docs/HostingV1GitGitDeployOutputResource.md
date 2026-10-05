# HostingV1GitGitDeployOutputResource

Result of cloning or pulling a Git repository into the website

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** | Whether the clone or pull, and composer install when it ran, finished without errors | 
**output** | **str** | Log of the deployment steps, and the Git or composer error when &#x60;is_success&#x60; is false | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_deploy_output_resource import HostingV1GitGitDeployOutputResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitDeployOutputResource from a JSON string
hosting_v1_git_git_deploy_output_resource_instance = HostingV1GitGitDeployOutputResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitDeployOutputResource.to_json())

# convert the object into a dict
hosting_v1_git_git_deploy_output_resource_dict = hosting_v1_git_git_deploy_output_resource_instance.to_dict()
# create an instance of HostingV1GitGitDeployOutputResource from a dict
hosting_v1_git_git_deploy_output_resource_from_dict = HostingV1GitGitDeployOutputResource.from_dict(hosting_v1_git_git_deploy_output_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


