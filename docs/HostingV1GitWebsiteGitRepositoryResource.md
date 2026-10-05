# HostingV1GitWebsiteGitRepositoryResource

Git repository linked to a directory of the website. A repository whose clone failed stays listed; deploying it again retries the clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_url** | **str** | Clone URL of the repository. A username, password or token in an HTTP(S) URL, or a password in any URL, is shown as &#x60;***&#x60;. | 
**branch** | **str** | Branch that is cloned and pulled | 
**directory** | **str** | Directory under the website document root. Empty means the document root. | 
**webhook** | [**HostingV1GitWebsiteGitRepositoryWebhookResource**](HostingV1GitWebsiteGitRepositoryWebhookResource.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_git_website_git_repository_resource import HostingV1GitWebsiteGitRepositoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitWebsiteGitRepositoryResource from a JSON string
hosting_v1_git_website_git_repository_resource_instance = HostingV1GitWebsiteGitRepositoryResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitWebsiteGitRepositoryResource.to_json())

# convert the object into a dict
hosting_v1_git_website_git_repository_resource_dict = hosting_v1_git_website_git_repository_resource_instance.to_dict()
# create an instance of HostingV1GitWebsiteGitRepositoryResource from a dict
hosting_v1_git_website_git_repository_resource_from_dict = HostingV1GitWebsiteGitRepositoryResource.from_dict(hosting_v1_git_website_git_repository_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


