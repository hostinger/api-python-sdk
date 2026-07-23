# hostinger_api.AgencyHostingWordPressApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_agency_plan_website_word_press_core_version_v1**](AgencyHostingWordPressApi.md#change_agency_plan_website_word_press_core_version_v1) | **PATCH** /api/agency-hosting/v1/websites/{website_uid}/wordpress/settings/version | Change Agency Plan website WordPress core version
[**get_agency_plan_website_word_press_settings_v1**](AgencyHostingWordPressApi.md#get_agency_plan_website_word_press_settings_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/wordpress/settings | Get Agency Plan website WordPress settings
[**list_available_word_press_versions_for_an_agency_plan_website_v1**](AgencyHostingWordPressApi.md#list_available_word_press_versions_for_an_agency_plan_website_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/wordpress/settings/versions | List available WordPress versions for an Agency Plan website


# **change_agency_plan_website_word_press_core_version_v1**
> CommonSuccessEmptyResource change_agency_plan_website_word_press_core_version_v1(website_uid, agency_hosting_v1_word_press_change_version_request)

Change Agency Plan website WordPress core version

Changes the installed WordPress core version on an Agency Plan website to one of the versions available for installation.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_word_press_change_version_request import AgencyHostingV1WordPressChangeVersionRequest
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
    api_instance = hostinger_api.AgencyHostingWordPressApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_word_press_change_version_request = hostinger_api.AgencyHostingV1WordPressChangeVersionRequest() # AgencyHostingV1WordPressChangeVersionRequest | 

    try:
        # Change Agency Plan website WordPress core version
        api_response = api_instance.change_agency_plan_website_word_press_core_version_v1(website_uid, agency_hosting_v1_word_press_change_version_request)
        print("The response of AgencyHostingWordPressApi->change_agency_plan_website_word_press_core_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWordPressApi->change_agency_plan_website_word_press_core_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_word_press_change_version_request** | [**AgencyHostingV1WordPressChangeVersionRequest**](AgencyHostingV1WordPressChangeVersionRequest.md)|  | 

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

# **get_agency_plan_website_word_press_settings_v1**
> AgencyHostingV1WordPressSettingsResource get_agency_plan_website_word_press_settings_v1(website_uid)

Get Agency Plan website WordPress settings

Returns the current WordPress settings for an Agency Plan website: installed core version,
LiteSpeed Cache plugin status, object cache status, and maintenance mode status.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_word_press_settings_resource import AgencyHostingV1WordPressSettingsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWordPressApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # Get Agency Plan website WordPress settings
        api_response = api_instance.get_agency_plan_website_word_press_settings_v1(website_uid)
        print("The response of AgencyHostingWordPressApi->get_agency_plan_website_word_press_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWordPressApi->get_agency_plan_website_word_press_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**AgencyHostingV1WordPressSettingsResource**](AgencyHostingV1WordPressSettingsResource.md)

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

# **list_available_word_press_versions_for_an_agency_plan_website_v1**
> List[AgencyHostingV1WordPressVersionResource] list_available_word_press_versions_for_an_agency_plan_website_v1(website_uid)

List available WordPress versions for an Agency Plan website

Lists the WordPress core versions available for installation on an Agency Plan website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_word_press_version_resource import AgencyHostingV1WordPressVersionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWordPressApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # List available WordPress versions for an Agency Plan website
        api_response = api_instance.list_available_word_press_versions_for_an_agency_plan_website_v1(website_uid)
        print("The response of AgencyHostingWordPressApi->list_available_word_press_versions_for_an_agency_plan_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWordPressApi->list_available_word_press_versions_for_an_agency_plan_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**List[AgencyHostingV1WordPressVersionResource]**](AgencyHostingV1WordPressVersionResource.md)

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

