# hostinger_api.ReachContactsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_contact_v1**](ReachContactsApi.md#create_a_new_contact_v1) | **POST** /api/reach/v1/contacts | Create a new contact
[**delete_a_contact_v1**](ReachContactsApi.md#delete_a_contact_v1) | **DELETE** /api/reach/v1/contacts/{uuid} | Delete a contact
[**list_contact_groups_v1**](ReachContactsApi.md#list_contact_groups_v1) | **GET** /api/reach/v1/contacts/groups | List contact groups
[**list_contacts_v1**](ReachContactsApi.md#list_contacts_v1) | **GET** /api/reach/v1/contacts | List contacts


# **create_a_new_contact_v1**
> ReachV1ContactsContactResource create_a_new_contact_v1(reach_v1_contacts_store_request)

Create a new contact

Create a new contact in the email marketing system.

This endpoint allows you to create a new contact with basic information like name, email, and surname.
You can optionally assign the contact to specific groups and add notes.

The contact will be automatically subscribed to email communications.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_contact_resource import ReachV1ContactsContactResource
from hostinger_api.models.reach_v1_contacts_store_request import ReachV1ContactsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    reach_v1_contacts_store_request = hostinger_api.ReachV1ContactsStoreRequest() # ReachV1ContactsStoreRequest | 

    try:
        # Create a new contact
        api_response = api_instance.create_a_new_contact_v1(reach_v1_contacts_store_request)
        print("The response of ReachContactsApi->create_a_new_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->create_a_new_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reach_v1_contacts_store_request** | [**ReachV1ContactsStoreRequest**](ReachV1ContactsStoreRequest.md)|  | 

### Return type

[**ReachV1ContactsContactResource**](ReachV1ContactsContactResource.md)

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

# **delete_a_contact_v1**
> CommonSuccessEmptyResource delete_a_contact_v1(uuid)

Delete a contact

Delete a contact with the specified UUID.

This endpoint permanently removes a contact from the email marketing system.

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
    api_instance = hostinger_api.ReachContactsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the contact to delete

    try:
        # Delete a contact
        api_response = api_instance.delete_a_contact_v1(uuid)
        print("The response of ReachContactsApi->delete_a_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->delete_a_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the contact to delete | 

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
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contact_groups_v1**
> List[ReachV1ContactsGroupsContactGroupResource] list_contact_groups_v1()

List contact groups

Get a list of all contact groups.

This endpoint returns a list of contact groups that can be used to organize contacts.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_groups_contact_group_resource import ReachV1ContactsGroupsContactGroupResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)

    try:
        # List contact groups
        api_response = api_instance.list_contact_groups_v1()
        print("The response of ReachContactsApi->list_contact_groups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->list_contact_groups_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReachV1ContactsGroupsContactGroupResource]**](ReachV1ContactsGroupsContactGroupResource.md)

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

# **list_contacts_v1**
> ReachListContactsV1200Response list_contacts_v1(group_uuid=group_uuid, subscription_status=subscription_status, page=page)

List contacts

Get a list of contacts, optionally filtered by group and subscription status.

This endpoint returns a paginated list of contacts with their basic information.
You can filter contacts by group UUID and subscription status.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_contacts_v1200_response import ReachListContactsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    group_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Filter contacts by group UUID (optional)
    subscription_status = 'subscribed' # str | Filter contacts by subscription status (optional)
    page = 1 # int | Page number (optional)

    try:
        # List contacts
        api_response = api_instance.list_contacts_v1(group_uuid=group_uuid, subscription_status=subscription_status, page=page)
        print("The response of ReachContactsApi->list_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->list_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| Filter contacts by group UUID | [optional] 
 **subscription_status** | **str**| Filter contacts by subscription status | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ReachListContactsV1200Response**](ReachListContactsV1200Response.md)

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

