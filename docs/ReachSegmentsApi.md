# hostinger_api.ReachSegmentsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_profile_segment_contacts_v1**](ReachSegmentsApi.md#count_profile_segment_contacts_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}/count | Count profile segment contacts
[**create_a_new_contact_segment_v1**](ReachSegmentsApi.md#create_a_new_contact_segment_v1) | **POST** /api/reach/v1/segmentation/segments | Create a new contact segment
[**create_a_profile_segment_v1**](ReachSegmentsApi.md#create_a_profile_segment_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/segmentation/segments | Create a profile segment
[**delete_a_profile_segment_v1**](ReachSegmentsApi.md#delete_a_profile_segment_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid} | Delete a profile segment
[**get_profile_segment_details_v1**](ReachSegmentsApi.md#get_profile_segment_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid} | Get profile segment details
[**get_segment_details_v1**](ReachSegmentsApi.md#get_segment_details_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid} | Get segment details
[**list_profile_segment_contacts_v1**](ReachSegmentsApi.md#list_profile_segment_contacts_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}/contacts | List profile segment contacts
[**list_profile_segments_v1**](ReachSegmentsApi.md#list_profile_segments_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments | List profile segments
[**list_segment_contacts_v1**](ReachSegmentsApi.md#list_segment_contacts_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid}/contacts | List segment contacts
[**list_segment_filter_attributes_v1**](ReachSegmentsApi.md#list_segment_filter_attributes_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/filters/attributes | List segment filter attributes
[**list_segments_v1**](ReachSegmentsApi.md#list_segments_v1) | **GET** /api/reach/v1/segmentation/segments | List segments
[**preview_contacts_matching_conditions_v1**](ReachSegmentsApi.md#preview_contacts_matching_conditions_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/segmentation/filters/contacts | Preview contacts matching conditions
[**update_a_profile_segment_v1**](ReachSegmentsApi.md#update_a_profile_segment_v1) | **PUT** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid} | Update a profile segment


# **count_profile_segment_contacts_v1**
> ReachV1ContactsSegmentsSegmentContactsCountResource count_profile_segment_contacts_v1(profile_uuid, segment_uuid)

Count profile segment contacts

Count the contacts currently matching a segment without listing them.

Cheaper than paging through the segment contacts endpoint when only the size is needed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_segment_contacts_count_resource import ReachV1ContactsSegmentsSegmentContactsCountResource
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

    try:
        # Count profile segment contacts
        api_response = api_instance.count_profile_segment_contacts_v1(profile_uuid, segment_uuid)
        print("The response of ReachSegmentsApi->count_profile_segment_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->count_profile_segment_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **segment_uuid** | **str**| Segment uuid parameter | 

### Return type

[**ReachV1ContactsSegmentsSegmentContactsCountResource**](ReachV1ContactsSegmentsSegmentContactsCountResource.md)

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

# **create_a_new_contact_segment_v1**
> ReachV1ContactsSegmentsSegmentResource create_a_new_contact_segment_v1(reach_v1_contacts_segments_store_request)

Create a new contact segment

Create a new contact segment.

This endpoint allows creating a new contact segment that can be used to organize contacts.
The segment can be configured with specific criteria like email, name, subscription status, etc.

**Deprecated.** This endpoint cannot target a profile, so it always falls back to
the client's default profile and cannot create segments in any other profile. Use
`POST /api/reach/v1/profiles/{profileUuid}/segmentation/segments` instead.

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

# **create_a_profile_segment_v1**
> ReachV1ContactsSegmentsSegmentResource create_a_profile_segment_v1(profile_uuid, reach_v1_contacts_segments_profile_store_request)

Create a profile segment

Create a segment in a profile.

A segment is a saved set of conditions rather than a fixed list, so its membership changes
as contacts change. Creating one does not modify any contact.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_profile_store_request import ReachV1ContactsSegmentsProfileStoreRequest
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
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_contacts_segments_profile_store_request = hostinger_api.ReachV1ContactsSegmentsProfileStoreRequest() # ReachV1ContactsSegmentsProfileStoreRequest | 

    try:
        # Create a profile segment
        api_response = api_instance.create_a_profile_segment_v1(profile_uuid, reach_v1_contacts_segments_profile_store_request)
        print("The response of ReachSegmentsApi->create_a_profile_segment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->create_a_profile_segment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_segments_profile_store_request** | [**ReachV1ContactsSegmentsProfileStoreRequest**](ReachV1ContactsSegmentsProfileStoreRequest.md)|  | 

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

# **delete_a_profile_segment_v1**
> CommonSuccessEmptyResource delete_a_profile_segment_v1(profile_uuid, segment_uuid)

Delete a profile segment

Delete a segment.

Only the segment definition is removed. The contacts that matched it are left untouched.

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
    api_instance = hostinger_api.ReachSegmentsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter

    try:
        # Delete a profile segment
        api_response = api_instance.delete_a_profile_segment_v1(profile_uuid, segment_uuid)
        print("The response of ReachSegmentsApi->delete_a_profile_segment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->delete_a_profile_segment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **segment_uuid** | **str**| Segment uuid parameter | 

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

# **get_profile_segment_details_v1**
> ReachV1ContactsSegmentsSegmentResource get_profile_segment_details_v1(profile_uuid, segment_uuid)

Get profile segment details

Get a single segment of a profile, including the conditions that define it.

To retrieve the contacts currently matching those conditions, use the segment contacts
endpoint instead.

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
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter

    try:
        # Get profile segment details
        api_response = api_instance.get_profile_segment_details_v1(profile_uuid, segment_uuid)
        print("The response of ReachSegmentsApi->get_profile_segment_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->get_profile_segment_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
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

# **get_segment_details_v1**
> ReachV1ContactsSegmentsSegmentResource get_segment_details_v1(segment_uuid)

Get segment details

Get details of a specific segment.

This endpoint retrieves information about a single segment identified by UUID.
Segments are used to organize and group contacts based on specific criteria.

**Deprecated.** This endpoint cannot target a profile, so it always falls back to
the client's default profile and cannot read segments of any other profile. Use
`GET /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}` instead.

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

# **list_profile_segments_v1**
> ReachListProfileSegmentsV1200Response list_profile_segments_v1(profile_uuid, count_type=count_type, page=page, per_page=per_page)

List profile segments

Get a paginated list of the segments defined in a profile.

Each entry carries the number of contacts currently matching it, which is recalculated on
read rather than stored. Use `count_type` to count either every matching contact or only
the subscribed ones.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_profile_segments_v1200_response import ReachListProfileSegmentsV1200Response
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
    count_type = all # str | Which matching contacts to count for each segment (optional) (default to all)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List profile segments
        api_response = api_instance.list_profile_segments_v1(profile_uuid, count_type=count_type, page=page, per_page=per_page)
        print("The response of ReachSegmentsApi->list_profile_segments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->list_profile_segments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **count_type** | **str**| Which matching contacts to count for each segment | [optional] [default to all]
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListProfileSegmentsV1200Response**](ReachListProfileSegmentsV1200Response.md)

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

**Deprecated.** This endpoint cannot target a profile, so it always falls back to
the client's default profile and cannot read segments of any other profile. Use
`GET /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}/contacts` instead.

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

# **list_segment_filter_attributes_v1**
> ReachV1ContactsSegmentsSegmentFilterAttributesResource list_segment_filter_attributes_v1(profile_uuid)

List segment filter attributes

List every attribute a segment condition can filter on, with the operators each attribute
accepts, the value format they expect and, where the value is constrained, the allowed
values.

The list is profile specific: it includes the profile's custom contact fields, its tags and
its 20 most recently published campaigns, so the valid attributes cannot be hardcoded. Read
it before creating or updating a segment to discover the valid `attribute`, `operator` and
`value` combinations.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_segment_filter_attributes_resource import ReachV1ContactsSegmentsSegmentFilterAttributesResource
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

    try:
        # List segment filter attributes
        api_response = api_instance.list_segment_filter_attributes_v1(profile_uuid)
        print("The response of ReachSegmentsApi->list_segment_filter_attributes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->list_segment_filter_attributes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**ReachV1ContactsSegmentsSegmentFilterAttributesResource**](ReachV1ContactsSegmentsSegmentFilterAttributesResource.md)

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

**Deprecated.** This endpoint cannot target a profile, so it always falls back to
the client's default profile and cannot list the segments of any other profile. Use
`GET /api/reach/v1/profiles/{profileUuid}/segmentation/segments` instead.

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

# **preview_contacts_matching_conditions_v1**
> ReachListProfileContactsV1200Response preview_contacts_matching_conditions_v1(profile_uuid, reach_v1_contacts_segments_profile_filter_contacts_request)

Preview contacts matching conditions

Preview the contacts matching a set of conditions without saving a segment.

The body is the same set of conditions accepted when creating or updating a segment, so this
is how to check who a filter reaches, and how many, before persisting it. Nothing is stored
and no contact is modified.

Call the segment filter attributes endpoint first to discover the valid `attribute`,
`operator` and `value` combinations.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_profile_contacts_v1200_response import ReachListProfileContactsV1200Response
from hostinger_api.models.reach_v1_contacts_segments_profile_filter_contacts_request import ReachV1ContactsSegmentsProfileFilterContactsRequest
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
    reach_v1_contacts_segments_profile_filter_contacts_request = hostinger_api.ReachV1ContactsSegmentsProfileFilterContactsRequest() # ReachV1ContactsSegmentsProfileFilterContactsRequest | 

    try:
        # Preview contacts matching conditions
        api_response = api_instance.preview_contacts_matching_conditions_v1(profile_uuid, reach_v1_contacts_segments_profile_filter_contacts_request)
        print("The response of ReachSegmentsApi->preview_contacts_matching_conditions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->preview_contacts_matching_conditions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_segments_profile_filter_contacts_request** | [**ReachV1ContactsSegmentsProfileFilterContactsRequest**](ReachV1ContactsSegmentsProfileFilterContactsRequest.md)|  | 

### Return type

[**ReachListProfileContactsV1200Response**](ReachListProfileContactsV1200Response.md)

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

# **update_a_profile_segment_v1**
> ReachV1ContactsSegmentsSegmentResource update_a_profile_segment_v1(profile_uuid, segment_uuid, reach_v1_contacts_segments_profile_update_request)

Update a profile segment

Rename a segment and/or replace the conditions that define it.

`name` is always required. Omit `conditions` to rename without touching the conditions;
supply them and they replace the existing set entirely rather than being merged into it.
Contacts are never modified, but which of them match the segment can change immediately.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_segments_profile_update_request import ReachV1ContactsSegmentsProfileUpdateRequest
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
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    segment_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Segment uuid parameter
    reach_v1_contacts_segments_profile_update_request = hostinger_api.ReachV1ContactsSegmentsProfileUpdateRequest() # ReachV1ContactsSegmentsProfileUpdateRequest | 

    try:
        # Update a profile segment
        api_response = api_instance.update_a_profile_segment_v1(profile_uuid, segment_uuid, reach_v1_contacts_segments_profile_update_request)
        print("The response of ReachSegmentsApi->update_a_profile_segment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachSegmentsApi->update_a_profile_segment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **segment_uuid** | **str**| Segment uuid parameter | 
 **reach_v1_contacts_segments_profile_update_request** | [**ReachV1ContactsSegmentsProfileUpdateRequest**](ReachV1ContactsSegmentsProfileUpdateRequest.md)|  | 

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

