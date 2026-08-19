# hostinger_api.AgencyHostingFilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_upload_urlv1**](AgencyHostingFilesApi.md#generate_upload_urlv1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/files/upload-urls | Generate upload URL
[**import_website_from_archive_v1**](AgencyHostingFilesApi.md#import_website_from_archive_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/files/import-archive | Import website from archive


# **generate_upload_urlv1**
> AgencyHostingV1FilesUploadUrlResource generate_upload_urlv1(website_uid)

Generate upload URL

Generate a file browser upload URL with authentication credentials for uploading files
to an Agency Plan website's file storage.

Returns `url`, `auth_key` and `rest_auth_key`. Use these to upload a file to the
website's file storage via the TUS resumable upload protocol (TUS 1.0.0). Send
`X-Auth: {auth_key}` and `X-Auth-Rest: {rest_auth_key}` headers on every request below.

1. Create the upload: `POST` to `{url}/{relative_file_path}?override=true` with headers
   `upload-length: {file size in bytes}` and `upload-offset: 0`. Expect `201 Created`.
2. Upload the file: send the file bytes to the same location (any TUS 1.0.0 client, or
   `PATCH` requests with an `upload-offset` header tracking progress) until complete.

`relative_file_path` is the destination path inside the website's file storage, e.g.
`app.zip`.

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
from hostinger_api.models.agency_hosting_v1_files_upload_url_resource import AgencyHostingV1FilesUploadUrlResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingFilesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # Generate upload URL
        api_response = api_instance.generate_upload_urlv1(website_uid)
        print("The response of AgencyHostingFilesApi->generate_upload_urlv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingFilesApi->generate_upload_urlv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**AgencyHostingV1FilesUploadUrlResource**](AgencyHostingV1FilesUploadUrlResource.md)

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

# **import_website_from_archive_v1**
> CommonSuccessEmptyResource import_website_from_archive_v1(website_uid, agency_hosting_v1_files_import_archive_request)

Import website from archive

Imports an Agency Plan website from an already-uploaded archive.

Upload the archive to the website's root directory via file browser first, then provide its
filename in this request. Website contents are overwritten by the archive contents. Supported
archive types: .zip, .tar, .tar.gz, .tgz.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_files_import_archive_request import AgencyHostingV1FilesImportArchiveRequest
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
    api_instance = hostinger_api.AgencyHostingFilesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_files_import_archive_request = hostinger_api.AgencyHostingV1FilesImportArchiveRequest() # AgencyHostingV1FilesImportArchiveRequest | 

    try:
        # Import website from archive
        api_response = api_instance.import_website_from_archive_v1(website_uid, agency_hosting_v1_files_import_archive_request)
        print("The response of AgencyHostingFilesApi->import_website_from_archive_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingFilesApi->import_website_from_archive_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_files_import_archive_request** | [**AgencyHostingV1FilesImportArchiveRequest**](AgencyHostingV1FilesImportArchiveRequest.md)|  | 

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

