# hostinger_api.HostingGitApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_git_auto_deployment_settings_v1**](HostingGitApi.md#delete_git_auto_deployment_settings_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/git/auto-deployments/settings | Delete Git auto-deployment settings
[**get_git_auto_deployment_settings_v1**](HostingGitApi.md#get_git_auto_deployment_settings_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/git/auto-deployments/settings | Get Git auto-deployment settings
[**list_git_installation_repositories_v1**](HostingGitApi.md#list_git_installation_repositories_v1) | **GET** /api/hosting/v1/git/installations/{uuid}/repositories | List Git installation repositories
[**list_git_installations_v1**](HostingGitApi.md#list_git_installations_v1) | **GET** /api/hosting/v1/git/installations | List Git installations
[**update_git_auto_deployment_settings_v1**](HostingGitApi.md#update_git_auto_deployment_settings_v1) | **PUT** /api/hosting/v1/accounts/{username}/websites/{domain}/git/auto-deployments/settings | Update Git auto-deployment settings


# **delete_git_auto_deployment_settings_v1**
> CommonSuccessEmptyResource delete_git_auto_deployment_settings_v1(username, domain)

Delete Git auto-deployment settings

Removes the Git auto-deployment settings of the website. Files already deployed stay on the
website; pushes stop deploying until settings are saved again. Succeeds also when nothing is
configured.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
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
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Delete Git auto-deployment settings
        api_response = api_instance.delete_git_auto_deployment_settings_v1(username, domain)
        print("The response of HostingGitApi->delete_git_auto_deployment_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingGitApi->delete_git_auto_deployment_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_auto_deployment_settings_v1**
> HostingV1GitGitAutoDeploymentSettingsResource get_git_auto_deployment_settings_v1(username, domain)

Get Git auto-deployment settings

Returns the Git auto-deployment settings of the website: which repository and branch deploy
into which directory, and whether pushes trigger a deployment. `is_enabled` false keeps the
repository link but ignores pushes.

When the website has no auto-deployment configured every field is null. Save settings with
`Update Git auto-deployment settings`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_git_git_auto_deployment_settings_resource import HostingV1GitGitAutoDeploymentSettingsResource
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
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get Git auto-deployment settings
        api_response = api_instance.get_git_auto_deployment_settings_v1(username, domain)
        print("The response of HostingGitApi->get_git_auto_deployment_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingGitApi->get_git_auto_deployment_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1GitGitAutoDeploymentSettingsResource**](HostingV1GitGitAutoDeploymentSettingsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_git_installation_repositories_v1**
> List[HostingV1GitGitRepositoryResource] list_git_installation_repositories_v1(uuid)

List Git installation repositories

Lists the repositories the Git installation can access, read live from the provider. Works
for github and gitlab installations. Use an active installation: a suspended or pending one
is still queried and the call fails with whatever the provider answers. The list is cut at
the first 500 repositories in the order the provider returns them; when the account has
more, name the repository directly instead of searching this list.

`owner`, `name` and a branch (`default_branch` or another one) go into `source_options` of
`Start Node.js build` or into `Update Git auto-deployment settings`. Returns 404 when the
installation does not belong to the customer. Limited to 10 calls per minute per API client
(429 above that).

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
`status=pending` as well. If there is none at all, a Git provider (GitHub or GitLab) has to be
connected once in hPanel (Websites, Manage, Advanced, Git; or Add Website, Node.js Web App,
Import Git Repository); this endpoint then lists the new installation.

Use `uuid` as the path parameter of `List Git installation repositories`, and as
`installation_uuid` in `Start Node.js build` with `source_type` `git` and in
`Update Git auto-deployment settings`.

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

# **update_git_auto_deployment_settings_v1**
> CommonSuccessEmptyResource update_git_auto_deployment_settings_v1(username, domain, hosting_v1_git_update_git_auto_deployment_settings_request)

Update Git auto-deployment settings

Creates or replaces the Git auto-deployment settings of the website: repository, branch, the
directory under the document root to deploy into, and `is_enabled`. Send the full set;
`is_enabled` defaults to true and `directory` to the document root. `installation_uuid` must
be an installation from `List Git installations` that belongs to the same customer as the
website.

For PHP and static websites, saving with `is_enabled` true deploys the branch right away and
every later push to that branch deploys again. For Node.js and Website Builder websites saving
does not clone anything. On a Node.js website start the first deploy with
`Start Node.js build` using `source_type` `git`; pushes then trigger new builds with the build
settings stored for the website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_git_update_git_auto_deployment_settings_request import HostingV1GitUpdateGitAutoDeploymentSettingsRequest
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
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_git_update_git_auto_deployment_settings_request = hostinger_api.HostingV1GitUpdateGitAutoDeploymentSettingsRequest() # HostingV1GitUpdateGitAutoDeploymentSettingsRequest | 

    try:
        # Update Git auto-deployment settings
        api_response = api_instance.update_git_auto_deployment_settings_v1(username, domain, hosting_v1_git_update_git_auto_deployment_settings_request)
        print("The response of HostingGitApi->update_git_auto_deployment_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingGitApi->update_git_auto_deployment_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_git_update_git_auto_deployment_settings_request** | [**HostingV1GitUpdateGitAutoDeploymentSettingsRequest**](HostingV1GitUpdateGitAutoDeploymentSettingsRequest.md)|  | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

