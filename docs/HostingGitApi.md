# hostinger_api.HostingGitApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_git_installation_repositories_v1**](HostingGitApi.md#list_git_installation_repositories_v1) | **GET** /api/hosting/v1/git/installations/{uuid}/repositories | List Git installation repositories
[**list_git_installations_v1**](HostingGitApi.md#list_git_installations_v1) | **GET** /api/hosting/v1/git/installations | List Git installations


# **list_git_installation_repositories_v1**
> List[HostingV1GitGitRepositoryResource] list_git_installation_repositories_v1(uuid)

List Git installation repositories

Lists the repositories the Git installation can access, read live from the provider. Works
for github and gitlab installations. Use an active installation: a suspended or pending one
is still queried and the call fails with whatever the provider answers. The list is cut at
the first 500 repositories in the order the provider returns them; when the account has
more, name the repository directly instead of searching this list.

`owner`, `name` and `default_branch` identify a repository and a branch to deploy. Returns
404 when the installation does not belong to the customer. Limited to 10 calls per minute
per API client (429 above that).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_git_git_repository_resource import HostingV1GitGitRepositoryResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingGitApi(api_client)
    uuid = '018f5e2a-1234-7890-abcd-1234567890ab' # str | Git installation UUID from the List Git installations endpoint

    try:
        # List Git installation repositories
        api_response = api_instance.list_git_installation_repositories_v1(uuid)
        print("The response of HostingGitApi->list_git_installation_repositories_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingGitApi->list_git_installation_repositories_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Git installation UUID from the List Git installations endpoint | 

### Return type

[**List[HostingV1GitGitRepositoryResource]**](HostingV1GitGitRepositoryResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_installations_v1**
> List[HostingV1GitGitInstallationResource] list_git_installations_v1(provider=provider, status=status)

List Git installations

Lists the Git provider accounts the customer has connected. Only installations with status
`active` are returned unless the `status` filter says otherwise.

An empty list means the customer has no active installation. Check `status=suspended` and
`status=pending` as well. If there is none at all, GitHub has to be connected once in hPanel
(Websites, Manage, Advanced, Git, Connect GitHub; or Add Website, Node.js Web App, Import Git
Repository, Continue with GitHub); this endpoint then lists the new installation.

Use `uuid` as the path parameter of `List Git installation repositories`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_git_git_installation_resource import HostingV1GitGitInstallationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingGitApi(api_client)
    provider = 'github' # str | Filter by Git provider (optional)
    status = active # str | Filter by installation status (optional) (default to active)

    try:
        # List Git installations
        api_response = api_instance.list_git_installations_v1(provider=provider, status=status)
        print("The response of HostingGitApi->list_git_installations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingGitApi->list_git_installations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Filter by Git provider | [optional] 
 **status** | **str**| Filter by installation status | [optional] [default to active]

### Return type

[**List[HostingV1GitGitInstallationResource]**](HostingV1GitGitInstallationResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

