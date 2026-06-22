# hostinger_api.ReachSegmentsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_contact_segment_v1**](ReachSegmentsApi.md#create_a_new_contact_segment_v1) | **POST** /api/reach/v1/segmentation/segments | Create a new contact segment
[**get_segment_details_v1**](ReachSegmentsApi.md#get_segment_details_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid} | Get segment details
[**list_profile_segment_contacts_v1**](ReachSegmentsApi.md#list_profile_segment_contacts_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}/contacts | List profile segment contacts
[**list_segment_contacts_v1**](ReachSegmentsApi.md#list_segment_contacts_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid}/contacts | List segment contacts
[**list_segments_v1**](ReachSegmentsApi.md#list_segments_v1) | **GET** /api/reach/v1/segmentation/segments | List segments


# **create_a_new_contact_segment_v1**
> ReachV1ContactsSegmentsSegmentResource create_a_new_contact_segment_v1(reach_v1_contacts_segments_store_request)

Create a new contact segment

Create a new contact segment.

This endpoint allows creating a new contact segment that can be used to organize contacts.
The segment can be configured with specific criteria like email, name, subscription status, etc.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_segment_resource import ReachV1ContactsSegmentsSegmentResource
from hostinger_api.models.reach_v1_contacts_segments_store_request import ReachV1ContactsSegmentsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachSegmentsApi(api_client)
    reach_v1_contacts_segments_store_request = hostinger_api.ReachV1ContactsSegmentsStoreRequest() # ReachV1ContactsSegmentsStoreRequest | 

    try:
        # Create a new contact segment
        api_response = api_instance.create_a_new_contact_segment_v1(reach_v1_contacts_segments_store_request)
        print("The response of ReachSegmentsApi->create_a_new_contact_segment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->create_a_new_contact_segment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reach_v1_contacts_segments_store_request** | [**ReachV1ContactsSegmentsStoreRequest**](ReachV1ContactsSegmentsStoreRequest.md)|  | 

### Return type

[**ReachV1ContactsSegmentsSegmentResource**](ReachV1ContactsSegmentsSegmentResource.md)

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

# **get_segment_details_v1**
> ReachV1ContactsSegmentsSegmentResource get_segment_details_v1(segment_uuid)

Get segment details

Get details of a specific segment.

This endpoint retrieves information about a single segment identified by UUID.
Segments are used to organize and group contacts based on specific criteria.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_segment_resource import ReachV1ContactsSegmentsSegmentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachSegmentsApi(api_client)
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter

    try:
        # Get segment details
        api_response = api_instance.get_segment_details_v1(segment_uuid)
        print("The response of ReachSegmentsApi->get_segment_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->get_segment_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_uuid** | **str**| Segment uuid parameter | 

### Return type

[**ReachV1ContactsSegmentsSegmentResource**](ReachV1ContactsSegmentsSegmentResource.md)

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

# **list_profile_segment_contacts_v1**
> ReachListProfileSegmentContactsV1200Response list_profile_segment_contacts_v1(profile_uuid, segment_uuid, page=page, per_page=per_page)

List profile segment contacts

Retrieve contacts associated with a specific segment for a given profile.

This endpoint allows you to fetch and filter contacts that belong to a particular segment,
identified by its UUID, scoped to a specific profile.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_profile_segment_contacts_v1200_response import ReachListProfileSegmentContactsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachSegmentsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List profile segment contacts
        api_response = api_instance.list_profile_segment_contacts_v1(profile_uuid, segment_uuid, page=page, per_page=per_page)
        print("The response of ReachSegmentsApi->list_profile_segment_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->list_profile_segment_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **segment_uuid** | **str**| Segment uuid parameter | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListProfileSegmentContactsV1200Response**](ReachListProfileSegmentContactsV1200Response.md)

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

# **list_segment_contacts_v1**
> ReachListProfileSegmentContactsV1200Response list_segment_contacts_v1(segment_uuid, page=page, per_page=per_page)

List segment contacts

Retrieve contacts associated with a specific segment.

This endpoint allows you to fetch and filter contacts that belong to a particular segment,
identified by its UUID.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_profile_segment_contacts_v1200_response import ReachListProfileSegmentContactsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachSegmentsApi(api_client)
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List segment contacts
        api_response = api_instance.list_segment_contacts_v1(segment_uuid, page=page, per_page=per_page)
        print("The response of ReachSegmentsApi->list_segment_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->list_segment_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_uuid** | **str**| Segment uuid parameter | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListProfileSegmentContactsV1200Response**](ReachListProfileSegmentContactsV1200Response.md)

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

# **list_segments_v1**
> List[ReachV1ContactsSegmentsContactSegmentResource] list_segments_v1()

List segments

Get a list of all contact segments.

This endpoint returns a list of contact segments that can be used to organize contacts.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_contact_segment_resource import ReachV1ContactsSegmentsContactSegmentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachSegmentsApi(api_client)

    try:
        # List segments
        api_response = api_instance.list_segments_v1()
        print("The response of ReachSegmentsApi->list_segments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->list_segments_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReachV1ContactsSegmentsContactSegmentResource]**](ReachV1ContactsSegmentsContactSegmentResource.md)

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

