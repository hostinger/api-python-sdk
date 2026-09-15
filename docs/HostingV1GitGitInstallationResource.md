# HostingV1GitGitInstallationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Installation identifier. Use it as the path parameter of List Git installation repositories. | 
**provider** | **str** | Git provider the account belongs to | 
**account_login** | **str** | Login of the connected provider account (user or organization) | 
**account_type** | **str** | Whether the connected account is a user or an organization | 
**account_avatar_url** | **str** | Avatar URL of the connected provider account | 
**status** | **str** | Installation status. Only active installations are listed unless the status filter says otherwise. | 
**installed_at** | **datetime** | When the provider app was installed on the account | 
**created_at** | **datetime** | When the installation record was created | 
**has_oauth** | **bool** | True when the GitHub user account has a stored OAuth token whose refresh token is still valid, false when the token is missing or its refresh token expired. Null for organization accounts and for providers other than GitHub. | 

## Example

```python
from hostinger_api.models.hosting_v1_git_git_installation_resource import HostingV1GitGitInstallationResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitGitInstallationResource from a JSON string
hosting_v1_git_git_installation_resource_instance = HostingV1GitGitInstallationResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitGitInstallationResource.to_json())

# convert the object into a dict
hosting_v1_git_git_installation_resource_dict = hosting_v1_git_git_installation_resource_instance.to_dict()
# create an instance of HostingV1GitGitInstallationResource from a dict
hosting_v1_git_git_installation_resource_from_dict = HostingV1GitGitInstallationResource.from_dict(hosting_v1_git_git_installation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


