# hostinger_api.HostingFilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_upload_urlv1**](HostingFilesApi.md#generate_upload_urlv1) | **POST** /api/hosting/v1/files/upload-urls | Generate upload URL
[**get_website_file_content_v1**](HostingFilesApi.md#get_website_file_content_v1) | **GET** /api/hosting/v1/accounts/{username}/domains/{domain}/files/content | Get website file content
[**list_website_files_and_directories_v1**](HostingFilesApi.md#list_website_files_and_directories_v1) | **GET** /api/hosting/v1/accounts/{username}/domains/{domain}/files | List website files and directories


# **generate_upload_urlv1**
> HostingV1FilesUploadUrlResource generate_upload_urlv1(hosting_v1_files_generate_upload_url_request)

Generate upload URL

Generate a file browser upload URL with authentication credentials
for uploading files directly to a website's file storage.

Returns `url`, `auth_key` and `rest_auth_key`. Use these to upload a file to the
website's `public_html` directory via the TUS resumable upload protocol (TUS 1.0.0).
Send `X-Auth: {auth_key}` and `X-Auth-Rest: {rest_auth_key}` headers on every request
below.

1. Create the upload: `POST` to `{url}/{relative_file_path}?override=true` with headers
   `upload-length: {file size in bytes}` and `upload-offset: 0`. Expect `201 Created`.
2. Upload the file: send the file bytes to the same location (any TUS 1.0.0 client, or
   `PATCH` requests with an `upload-offset` header tracking progress) until complete.

`relative_file_path` is the destination path inside `public_html`, e.g. `app.zip`.

Instead of a TUS client, plain `curl` also works:
```
FILE=app.zip
SIZE=$(stat -f%z "$FILE")   # stat -c%s on Linux

curl -i -X POST "{url}/${FILE}?override=true" \
  -H "X-Auth: {auth_key}" \
  -H "X-Auth-Rest: {rest_auth_key}" \
  -H "Tus-Resumable: 1.0.0" \
  -H "Upload-Length: ${SIZE}" \
  -H "Upload-Offset: 0"
# -> 201 Created

curl -i -X PATCH "{url}/${FILE}?override=true" \
  -H "X-Auth: {auth_key}" \
  -H "X-Auth-Rest: {rest_auth_key}" \
  -H "Tus-Resumable: 1.0.0" \
  -H "Content-Type: application/offset+octet-stream" \
  -H "Upload-Offset: 0" \
  --data-binary "@${FILE}"
# -> 204 No Content, Upload-Offset response header equals SIZE when done
```

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_files_generate_upload_url_request import HostingV1FilesGenerateUploadUrlRequest
from hostinger_api.models.hosting_v1_files_upload_url_resource import HostingV1FilesUploadUrlResource
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
    hosting_v1_files_generate_upload_url_request = hostinger_api.HostingV1FilesGenerateUploadUrlRequest() # HostingV1FilesGenerateUploadUrlRequest | 

    try:
        # Generate upload URL
        api_response = api_instance.generate_upload_urlv1(hosting_v1_files_generate_upload_url_request)
        print("The response of HostingFilesApi->generate_upload_urlv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingFilesApi->generate_upload_urlv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosting_v1_files_generate_upload_url_request** | [**HostingV1FilesGenerateUploadUrlRequest**](HostingV1FilesGenerateUploadUrlRequest.md)|  | 

### Return type

[**HostingV1FilesUploadUrlResource**](HostingV1FilesUploadUrlResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    file_types = ['[\"file\",\"directory\"]'] # List[str] | Filter by entry type, e.g. file,directory. Omit for all types. (optional)

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
 **file_types** | [**List[str]**](str.md)| Filter by entry type, e.g. file,directory. Omit for all types. | [optional] 

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

