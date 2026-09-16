# HostingV1GitGitAutoDeploymentSettingsResource

Every field is null when the website has no Git auto-deployment configured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_uuid** | **str** | Git installation the repository is accessed through | 
**is_enabled** | **bool** | Whether pushes to the branch deploy automatically | 
**owner** | **str** | Repository owner login | 
**repository** | **str** | Repository name | 
**branch** | **str** | Branch that is deployed | 
**directory** | **str** | Subdirectory under the website document root the repository deploys into. Empty means the document root. | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_auto_deployment_settings_resource import HostingV1GitGitAutoDeploymentSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitAutoDeploymentSettingsResource from a JSON string
hosting_v1_git_git_auto_deployment_settings_resource_instance = HostingV1GitGitAutoDeploymentSettingsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitAutoDeploymentSettingsResource.to_json())

# convert the object into a dict
hosting_v1_git_git_auto_deployment_settings_resource_dict = hosting_v1_git_git_auto_deployment_settings_resource_instance.to_dict()
# create an instance of HostingV1GitGitAutoDeploymentSettingsResource from a dict
hosting_v1_git_git_auto_deployment_settings_resource_from_dict = HostingV1GitGitAutoDeploymentSettingsResource.from_dict(hosting_v1_git_git_auto_deployment_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


