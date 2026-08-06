# hostinger_api.ReachContactFieldsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_contact_field_v1**](ReachContactFieldsApi.md#create_a_contact_field_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/contacts/fields | Create a contact field
[**delete_a_contact_field_v1**](ReachContactFieldsApi.md#delete_a_contact_field_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/contacts/fields/{fieldUuid} | Delete a contact field
[**list_contact_fields_v1**](ReachContactFieldsApi.md#list_contact_fields_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/contacts/fields | List contact fields
[**update_a_contact_field_v1**](ReachContactFieldsApi.md#update_a_contact_field_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/contacts/fields/{fieldUuid} | Update a contact field


# **create_a_contact_field_v1**
> ReachV1ContactsFieldsContactFieldResource create_a_contact_field_v1(profile_uuid, reach_v1_contacts_fields_store_request)

Create a contact field

Define a new custom contact field in a profile.

The `slug` is derived from the label and, like the field type, cannot be changed later.
Use the returned uuid to set values on contacts.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_fields_contact_field_resource import ReachV1ContactsFieldsContactFieldResource
from hostinger_api.models.reach_v1_contacts_fields_store_request import ReachV1ContactsFieldsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactFieldsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_contacts_fields_store_request = hostinger_api.ReachV1ContactsFieldsStoreRequest() # ReachV1ContactsFieldsStoreRequest | 

    try:
        # Create a contact field
        api_response = api_instance.create_a_contact_field_v1(profile_uuid, reach_v1_contacts_fields_store_request)
        print("The response of ReachContactFieldsApi->create_a_contact_field_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactFieldsApi->create_a_contact_field_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_fields_store_request** | [**ReachV1ContactsFieldsStoreRequest**](ReachV1ContactsFieldsStoreRequest.md)|  | 

### Return type

[**ReachV1ContactsFieldsContactFieldResource**](ReachV1ContactsFieldsContactFieldResource.md)

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

# **delete_a_contact_field_v1**
> CommonSuccessEmptyResource delete_a_contact_field_v1(profile_uuid, field_uuid)

Delete a contact field

Delete a custom contact field.

Every value contacts hold for the field is deleted with it, and for the choice types so
are its options. The contacts themselves are not affected.

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
    api_instance = hostinger_api.ReachContactFieldsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    field_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact field uuid parameter

    try:
        # Delete a contact field
        api_response = api_instance.delete_a_contact_field_v1(profile_uuid, field_uuid)
        print("The response of ReachContactFieldsApi->delete_a_contact_field_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactFieldsApi->delete_a_contact_field_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **field_uuid** | **str**| Contact field uuid parameter | 

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

# **list_contact_fields_v1**
> List[ReachV1ContactsFieldsContactFieldResource] list_contact_fields_v1(profile_uuid)

List contact fields

Get the custom contact fields defined in a profile.

Custom fields let you store your own attributes on contacts. The returned uuids are what
you pass to the contact update endpoint to set values, and choice fields also list the
options available to pick from.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_fields_contact_field_resource import ReachV1ContactsFieldsContactFieldResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactFieldsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List contact fields
        api_response = api_instance.list_contact_fields_v1(profile_uuid)
        print("The response of ReachContactFieldsApi->list_contact_fields_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactFieldsApi->list_contact_fields_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1ContactsFieldsContactFieldResource]**](ReachV1ContactsFieldsContactFieldResource.md)

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

# **update_a_contact_field_v1**
> ReachV1ContactsFieldsContactFieldResource update_a_contact_field_v1(profile_uuid, field_uuid, reach_v1_contacts_fields_update_request)

Update a contact field

Rename a custom contact field and, for the choice types, replace its option set.

Options carrying a uuid are kept and relabelled, options without one are created, and any
existing option left out of the list is deleted along with the values contacts hold for
it. The field type and slug cannot be changed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_fields_contact_field_resource import ReachV1ContactsFieldsContactFieldResource
from hostinger_api.models.reach_v1_contacts_fields_update_request import ReachV1ContactsFieldsUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactFieldsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    field_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact field uuid parameter
    reach_v1_contacts_fields_update_request = hostinger_api.ReachV1ContactsFieldsUpdateRequest() # ReachV1ContactsFieldsUpdateRequest | 

    try:
        # Update a contact field
        api_response = api_instance.update_a_contact_field_v1(profile_uuid, field_uuid, reach_v1_contacts_fields_update_request)
        print("The response of ReachContactFieldsApi->update_a_contact_field_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactFieldsApi->update_a_contact_field_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **field_uuid** | **str**| Contact field uuid parameter | 
 **reach_v1_contacts_fields_update_request** | [**ReachV1ContactsFieldsUpdateRequest**](ReachV1ContactsFieldsUpdateRequest.md)|  | 

### Return type

[**ReachV1ContactsFieldsContactFieldResource**](ReachV1ContactsFieldsContactFieldResource.md)

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

