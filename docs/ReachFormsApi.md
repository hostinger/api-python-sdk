# hostinger_api.ReachFormsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_form_v1**](ReachFormsApi.md#delete_form_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid} | Delete form
[**get_form_details_v1**](ReachFormsApi.md#get_form_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid} | Get form details
[**list_forms_v1**](ReachFormsApi.md#list_forms_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/forms | List forms


# **delete_form_v1**
> CommonSuccessEmptyResource delete_form_v1(profile_uuid, form_uuid)

Delete form

Permanently delete a form together with its template.

A form that has already captured submissions cannot be deleted, so that the contacts it collected
are never silently discarded - pause the form instead to stop it collecting new ones. Views alone
do not block deletion.

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
    api_instance = hostinger_api.ReachFormsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    form_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Form uuid parameter

    try:
        # Delete form
        api_response = api_instance.delete_form_v1(profile_uuid, form_uuid)
        print("The response of ReachFormsApi->delete_form_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->delete_form_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 

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
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_details_v1**
> ReachV1FormsFormDetailsResource get_form_details_v1(profile_uuid, form_uuid)

Get form details

Get a single form with the URL of its hosted template and the tags it applies to the contacts
it captures.

There is no ready-made embed snippet in the response - either serve the template HTML yourself
or build your own embed around the form uuid.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_forms_form_details_resource import ReachV1FormsFormDetailsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachFormsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    form_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Form uuid parameter

    try:
        # Get form details
        api_response = api_instance.get_form_details_v1(profile_uuid, form_uuid)
        print("The response of ReachFormsApi->get_form_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->get_form_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 

### Return type

[**ReachV1FormsFormDetailsResource**](ReachV1FormsFormDetailsResource.md)

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

# **list_forms_v1**
> ReachListFormsV1200Response list_forms_v1(profile_uuid, page=page, per_page=per_page)

List forms

Get a paginated list of the signup forms in a profile.

Each form carries a reference to the template that renders it. Get the form details for a
directly usable template URL and for the tags the form puts on the contacts it captures.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_forms_v1200_response import ReachListFormsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachFormsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List forms
        api_response = api_instance.list_forms_v1(profile_uuid, page=page, per_page=per_page)
        print("The response of ReachFormsApi->list_forms_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->list_forms_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListFormsV1200Response**](ReachListFormsV1200Response.md)

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

