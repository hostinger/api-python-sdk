# HostingV1GitUpdateGitAutoDeploymentSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_uuid** | **str** | Active Git installation from &#x60;List Git installations&#x60; | 
**owner** | **str** | Repository owner login, as returned by &#x60;List Git installation repositories&#x60;. GitLab group paths use slashes. | 
**repository** | **str** | Repository name without the .git suffix | 
**branch** | **str** | Branch to deploy | 
**directory** | **str** | Subdirectory under the website document root to deploy into. Empty, null or omitted means the document root. | [optional] [default to '']
**is_enabled** | **bool** | Whether pushes to the branch deploy automatically | [optional] [default to True]

## Example

```python
from hostinger_api.models.hosting_v1_git_update_git_auto_deployment_settings_request import HostingV1GitUpdateGitAutoDeploymentSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitUpdateGitAutoDeploymentSettingsRequest from a JSON string
hosting_v1_git_update_git_auto_deployment_settings_request_instance = HostingV1GitUpdateGitAutoDeploymentSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitUpdateGitAutoDeploymentSettingsRequest.to_json())

# convert the object into a dict
hosting_v1_git_update_git_auto_deployment_settings_request_dict = hosting_v1_git_update_git_auto_deployment_settings_request_instance.to_dict()
# create an instance of HostingV1GitUpdateGitAutoDeploymentSettingsRequest from a dict
hosting_v1_git_update_git_auto_deployment_settings_request_from_dict = HostingV1GitUpdateGitAutoDeploymentSettingsRequest.from_dict(hosting_v1_git_update_git_auto_deployment_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


