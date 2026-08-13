# hostinger_api.HostingFilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_website_file_content_v1**](HostingFilesApi.md#get_website_file_content_v1) | **GET** /api/hosting/v1/accounts/{username}/domains/{domain}/files/content | Get website file content
[**list_website_files_and_directories_v1**](HostingFilesApi.md#list_website_files_and_directories_v1) | **GET** /api/hosting/v1/accounts/{username}/domains/{domain}/files | List website files and directories


# **get_website_file_content_v1**
> HostingV1FilesFileContentResource get_website_file_content_v1(username, domain, path, from_line=from_line, max_lines=max_lines)

Get website file content

Get a single file's content, relative to a website's document root.

Read-only; refuses symlinks, oversized files, non-text file types, and files identified as
containing secrets (e.g. credential files) — none of these are returned by this endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_files_file_content_resource import HostingV1FilesFileContentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingFilesApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    path = 'index.php' # str | File path, relative to the document root.
    from_line = 0 # int | Line offset to start reading from. (optional) (default to 0)
    max_lines = 5000 # int | Max number of lines to return. (optional) (default to 5000)

    try:
        # Get website file content
        api_response = api_instance.get_website_file_content_v1(username, domain, path, from_line=from_line, max_lines=max_lines)
        print("The response of HostingFilesApi->get_website_file_content_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingFilesApi->get_website_file_content_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **path** | **str**| File path, relative to the document root. | 
 **from_line** | **int**| Line offset to start reading from. | [optional] [default to 0]
 **max_lines** | **int**| Max number of lines to return. | [optional] [default to 5000]

### Return type

[**HostingV1FilesFileContentResource**](HostingV1FilesFileContentResource.md)

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

# **list_website_files_and_directories_v1**
> HostingV1FilesFilesResource list_website_files_and_directories_v1(username, domain, directory=directory, max_depth=max_depth, max_items=max_items, offset=offset, file_types=file_types)

List website files and directories

List files and directories under a website's document root.

Use `directory` to browse a subdirectory relative to the document root. Symlinked entries
are listed but never traversed into or resolved.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_files_files_resource import HostingV1FilesFilesResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingFilesApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    directory = '' # str | Directory path to check (optional) (default to '')
    max_depth = 5 # int | How many directory levels deep to recurse. (optional) (default to 5)
    max_items = 1000 # int | Max number of entries to return in this page. (optional) (default to 1000)
    offset = 0 # int | Number of entries to skip. Page with offset + item count until reaching total_items. (optional) (default to 0)
    file_types = hostinger_api.HostingListWebsiteFilesAndDirectoriesV1FileTypesParameter() # HostingListWebsiteFilesAndDirectoriesV1FileTypesParameter | Filter by entry type, e.g. file,directory. Array or comma-separated. Omit for all types. (optional)

    try:
        # List website files and directories
        api_response = api_instance.list_website_files_and_directories_v1(username, domain, directory=directory, max_depth=max_depth, max_items=max_items, offset=offset, file_types=file_types)
        print("The response of HostingFilesApi->list_website_files_and_directories_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingFilesApi->list_website_files_and_directories_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **directory** | **str**| Directory path to check | [optional] [default to &#39;&#39;]
 **max_depth** | **int**| How many directory levels deep to recurse. | [optional] [default to 5]
 **max_items** | **int**| Max number of entries to return in this page. | [optional] [default to 1000]
 **offset** | **int**| Number of entries to skip. Page with offset + item count until reaching total_items. | [optional] [default to 0]
 **file_types** | [**HostingListWebsiteFilesAndDirectoriesV1FileTypesParameter**](.md)| Filter by entry type, e.g. file,directory. Array or comma-separated. Omit for all types. | [optional] 

### Return type

[**HostingV1FilesFilesResource**](HostingV1FilesFilesResource.md)

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

