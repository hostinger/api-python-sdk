# HostingV1GitDeployWebsiteGitRepositoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | Clone URL of the repository on any Git host, SSH or HTTPS. Private repositories need an SSH URL and the account&#39;s Git SSH key added to the repository as a deploy key. An HTTP or HTTPS URL with a username or token, or any URL with a password, is rejected. | 
**branch** | **str** | Branch to clone and pull | 
**directory** | **str** | Directory under the website document root, exactly as &#x60;List website Git repositories&#x60; returns it for an existing repository. Empty, null or omitted means the document root. | [optional] [default to '']

## Example

```python
from hostinger_api.models.hosting_v1_git_deploy_website_git_repository_request import HostingV1GitDeployWebsiteGitRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitDeployWebsiteGitRepositoryRequest from a JSON string
hosting_v1_git_deploy_website_git_repository_request_instance = HostingV1GitDeployWebsiteGitRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitDeployWebsiteGitRepositoryRequest.to_json())

# convert the object into a dict
hosting_v1_git_deploy_website_git_repository_request_dict = hosting_v1_git_deploy_website_git_repository_request_instance.to_dict()
# create an instance of HostingV1GitDeployWebsiteGitRepositoryRequest from a dict
hosting_v1_git_deploy_website_git_repository_request_from_dict = HostingV1GitDeployWebsiteGitRepositoryRequest.from_dict(hosting_v1_git_deploy_website_git_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


