# hostinger_api.ReachTagsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_a_contact_to_a_tag_v1**](ReachTagsApi.md#assign_a_contact_to_a_tag_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid}/contacts/{contactUuid} | Assign a contact to a tag
[**assign_contacts_to_a_tag_v1**](ReachTagsApi.md#assign_contacts_to_a_tag_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid}/contacts | Assign contacts to a tag
[**create_or_find_tags_v1**](ReachTagsApi.md#create_or_find_tags_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/tags | Create or find tags
[**delete_a_tag_v1**](ReachTagsApi.md#delete_a_tag_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid} | Delete a tag
[**list_profile_tags_v1**](ReachTagsApi.md#list_profile_tags_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/tags | List profile tags
[**remove_a_contact_from_a_tag_v1**](ReachTagsApi.md#remove_a_contact_from_a_tag_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid}/contacts/{contactUuid} | Remove a contact from a tag
[**remove_contacts_from_a_tag_v1**](ReachTagsApi.md#remove_contacts_from_a_tag_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid}/contacts | Remove contacts from a tag
[**rename_a_tag_v1**](ReachTagsApi.md#rename_a_tag_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/tags/{tagUuid} | Rename a tag


# **assign_a_contact_to_a_tag_v1**
> ReachV1ContactsTagsTagResource assign_a_contact_to_a_tag_v1(profile_uuid, tag_uuid, contact_uuid)

Assign a contact to a tag

Assign a tag to a single contact.

Unlike the bulk endpoint this is applied immediately rather than queued. Assigning a tag
the contact already carries succeeds without duplicating it.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_tags_tag_resource import ReachV1ContactsTagsTagResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter
    contact_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact uuid parameter

    try:
        # Assign a contact to a tag
        api_response = api_instance.assign_a_contact_to_a_tag_v1(profile_uuid, tag_uuid, contact_uuid)
        print("The response of ReachTagsApi->assign_a_contact_to_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->assign_a_contact_to_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 
 **contact_uuid** | **str**| Contact uuid parameter | 

### Return type

[**ReachV1ContactsTagsTagResource**](ReachV1ContactsTagsTagResource.md)

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

# **assign_contacts_to_a_tag_v1**
> CommonSuccessEmptyResource assign_contacts_to_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_manage_contacts_request)

Assign contacts to a tag

Assign a tag to many contacts at once.

Pass `contact_uuids` to target specific contacts, or `all_contacts` to target every contact
in the profile. The work is queued, so a success response means it was accepted rather than
finished. Contacts that already carry the tag are left alone.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_contacts_tags_manage_contacts_request import ReachV1ContactsTagsManageContactsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter
    reach_v1_contacts_tags_manage_contacts_request = hostinger_api.ReachV1ContactsTagsManageContactsRequest() # ReachV1ContactsTagsManageContactsRequest | 

    try:
        # Assign contacts to a tag
        api_response = api_instance.assign_contacts_to_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_manage_contacts_request)
        print("The response of ReachTagsApi->assign_contacts_to_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->assign_contacts_to_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 
 **reach_v1_contacts_tags_manage_contacts_request** | [**ReachV1ContactsTagsManageContactsRequest**](ReachV1ContactsTagsManageContactsRequest.md)|  | 

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

# **create_or_find_tags_v1**
> List[ReachV1ContactsTagsTagResource] create_or_find_tags_v1(profile_uuid, reach_v1_contacts_tags_store_request)

Create or find tags

Create tags in a profile.

Names that already exist in the profile are not duplicated: the existing tag is returned
instead, so the call is safe to repeat. Every tag in the request is returned, whether it
was created now or already existed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_tags_store_request import ReachV1ContactsTagsStoreRequest
from hostinger_api.models.reach_v1_contacts_tags_tag_resource import ReachV1ContactsTagsTagResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_contacts_tags_store_request = hostinger_api.ReachV1ContactsTagsStoreRequest() # ReachV1ContactsTagsStoreRequest | 

    try:
        # Create or find tags
        api_response = api_instance.create_or_find_tags_v1(profile_uuid, reach_v1_contacts_tags_store_request)
        print("The response of ReachTagsApi->create_or_find_tags_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->create_or_find_tags_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_tags_store_request** | [**ReachV1ContactsTagsStoreRequest**](ReachV1ContactsTagsStoreRequest.md)|  | 

### Return type

[**List[ReachV1ContactsTagsTagResource]**](ReachV1ContactsTagsTagResource.md)

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

# **delete_a_tag_v1**
> CommonSuccessEmptyResource delete_a_tag_v1(profile_uuid, tag_uuid)

Delete a tag

Delete a tag and remove it from every contact carrying it.

The contacts themselves are not deleted. This is idempotent: deleting a tag that does not
exist in the profile still succeeds.

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
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter

    try:
        # Delete a tag
        api_response = api_instance.delete_a_tag_v1(profile_uuid, tag_uuid)
        print("The response of ReachTagsApi->delete_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->delete_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 

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

# **list_profile_tags_v1**
> List[ReachV1ContactsTagsTagResource] list_profile_tags_v1(profile_uuid)

List profile tags

Get all tags defined in a profile.

Tags are the way contacts are grouped in Reach, and can be used to filter the contact
list or to build segments.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_tags_tag_resource import ReachV1ContactsTagsTagResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List profile tags
        api_response = api_instance.list_profile_tags_v1(profile_uuid)
        print("The response of ReachTagsApi->list_profile_tags_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->list_profile_tags_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1ContactsTagsTagResource]**](ReachV1ContactsTagsTagResource.md)

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

# **remove_a_contact_from_a_tag_v1**
> CommonSuccessEmptyResource remove_a_contact_from_a_tag_v1(profile_uuid, tag_uuid, contact_uuid)

Remove a contact from a tag

Remove a tag from a single contact.

Unlike the bulk endpoint this is applied immediately rather than queued. Neither the tag
nor the contact is deleted.

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
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter
    contact_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact uuid parameter

    try:
        # Remove a contact from a tag
        api_response = api_instance.remove_a_contact_from_a_tag_v1(profile_uuid, tag_uuid, contact_uuid)
        print("The response of ReachTagsApi->remove_a_contact_from_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->remove_a_contact_from_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 
 **contact_uuid** | **str**| Contact uuid parameter | 

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

# **remove_contacts_from_a_tag_v1**
> CommonSuccessEmptyResource remove_contacts_from_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_manage_contacts_request)

Remove contacts from a tag

Remove a tag from many contacts at once.

Pass `contact_uuids` to target specific contacts, or `all_contacts` to target every contact
in the profile. The work is queued, so a success response means it was accepted rather than
finished. The tag itself and the contacts are not deleted.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_contacts_tags_manage_contacts_request import ReachV1ContactsTagsManageContactsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter
    reach_v1_contacts_tags_manage_contacts_request = hostinger_api.ReachV1ContactsTagsManageContactsRequest() # ReachV1ContactsTagsManageContactsRequest | 

    try:
        # Remove contacts from a tag
        api_response = api_instance.remove_contacts_from_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_manage_contacts_request)
        print("The response of ReachTagsApi->remove_contacts_from_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->remove_contacts_from_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 
 **reach_v1_contacts_tags_manage_contacts_request** | [**ReachV1ContactsTagsManageContactsRequest**](ReachV1ContactsTagsManageContactsRequest.md)|  | 

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

# **rename_a_tag_v1**
> ReachV1ContactsTagsTagResource rename_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_update_request)

Rename a tag

Rename a tag.

The contacts assigned to the tag are unaffected. Names are unique within a profile, so
renaming a tag to a name that is already taken is rejected.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_tags_tag_resource import ReachV1ContactsTagsTagResource
from hostinger_api.models.reach_v1_contacts_tags_update_request import ReachV1ContactsTagsUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTagsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Tag uuid parameter
    reach_v1_contacts_tags_update_request = hostinger_api.ReachV1ContactsTagsUpdateRequest() # ReachV1ContactsTagsUpdateRequest | 

    try:
        # Rename a tag
        api_response = api_instance.rename_a_tag_v1(profile_uuid, tag_uuid, reach_v1_contacts_tags_update_request)
        print("The response of ReachTagsApi->rename_a_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTagsApi->rename_a_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **tag_uuid** | **str**| Tag uuid parameter | 
 **reach_v1_contacts_tags_update_request** | [**ReachV1ContactsTagsUpdateRequest**](ReachV1ContactsTagsUpdateRequest.md)|  | 

### Return type

[**ReachV1ContactsTagsTagResource**](ReachV1ContactsTagsTagResource.md)

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

