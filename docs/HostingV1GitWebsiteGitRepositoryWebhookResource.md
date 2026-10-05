# HostingV1GitWebsiteGitRepositoryWebhookResource

Auto-deployment webhook of the repository, the same one the Git section of hPanel shows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Webhook URL to add on the Git host for automatic deployment | 
**provider** | **str** | Git host detected from the repository URL. Null when it is not GitHub, GitLab or Bitbucket. | 
**setup_url** | **str** | Page on the Git host where the webhook is added. Null when the host is not detected. | 
**tutorial_url** | **str** | Git host guide for adding a webhook. Null when the host is not detected. | 

## Example

```python
from hostinger_api.models.hosting_v1_git_website_git_repository_webhook_resource import HostingV1GitWebsiteGitRepositoryWebhookResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1GitWebsiteGitRepositoryWebhookResource from a JSON string
hosting_v1_git_website_git_repository_webhook_resource_instance = HostingV1GitWebsiteGitRepositoryWebhookResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1GitWebsiteGitRepositoryWebhookResource.to_json())

# convert the object into a dict
hosting_v1_git_website_git_repository_webhook_resource_dict = hosting_v1_git_website_git_repository_webhook_resource_instance.to_dict()
# create an instance of HostingV1GitWebsiteGitRepositoryWebhookResource from a dict
hosting_v1_git_website_git_repository_webhook_resource_from_dict = HostingV1GitWebsiteGitRepositoryWebhookResource.from_dict(hosting_v1_git_website_git_repository_webhook_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


