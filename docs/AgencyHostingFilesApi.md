# hostinger_api.AgencyHostingFilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_agency_plan_website_from_archive_v1**](AgencyHostingFilesApi.md#import_agency_plan_website_from_archive_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/files/import-archive | Import Agency Plan website from archive


# **import_agency_plan_website_from_archive_v1**
> CommonSuccessEmptyResource import_agency_plan_website_from_archive_v1(website_uid, agency_hosting_v1_files_import_archive_request)

Import Agency Plan website from archive

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
        # Import Agency Plan website from archive
        api_response = api_instance.import_agency_plan_website_from_archive_v1(website_uid, agency_hosting_v1_files_import_archive_request)
        print("The response of AgencyHostingFilesApi->import_agency_plan_website_from_archive_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingFilesApi->import_agency_plan_website_from_archive_v1: %s\n" % e)
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

