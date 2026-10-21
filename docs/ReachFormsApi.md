# hostinger_api.ReachFormsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_form_submitter_tags_v1**](ReachFormsApi.md#add_form_submitter_tags_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid}/tags | Add form submitter tags
[**create_form_v1**](ReachFormsApi.md#create_form_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/forms | Create form
[**delete_form_v1**](ReachFormsApi.md#delete_form_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid} | Delete form
[**duplicate_form_v1**](ReachFormsApi.md#duplicate_form_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid}/duplicate | Duplicate form
[**get_form_details_v1**](ReachFormsApi.md#get_form_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid} | Get form details
[**list_forms_v1**](ReachFormsApi.md#list_forms_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/forms | List forms
[**remove_form_submitter_tag_v1**](ReachFormsApi.md#remove_form_submitter_tag_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid}/tags | Remove form submitter tag
[**update_form_template_v1**](ReachFormsApi.md#update_form_template_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid}/template | Update form template
[**update_form_v1**](ReachFormsApi.md#update_form_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/forms/{formUuid} | Update form


# **add_form_submitter_tags_v1**
> CommonSuccessEmptyResource add_form_submitter_tags_v1(profile_uuid, form_uuid, reach_v1_forms_assign_tags_request)

Add form submitter tags

Add tags to a form so that every contact who submits it from now on receives them.

A tag the form already has is skipped; an unknown tag is rejected. Contacts who submitted earlier are
not tagged.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_forms_assign_tags_request import ReachV1FormsAssignTagsRequest
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
    reach_v1_forms_assign_tags_request = hostinger_api.ReachV1FormsAssignTagsRequest() # ReachV1FormsAssignTagsRequest | 

    try:
        # Add form submitter tags
        api_response = api_instance.add_form_submitter_tags_v1(profile_uuid, form_uuid, reach_v1_forms_assign_tags_request)
        print("The response of ReachFormsApi->add_form_submitter_tags_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->add_form_submitter_tags_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 
 **reach_v1_forms_assign_tags_request** | [**ReachV1FormsAssignTagsRequest**](ReachV1FormsAssignTagsRequest.md)|  | 

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

# **create_form_v1**
> ReachV1FormsFormResource create_form_v1(profile_uuid, reach_v1_forms_store_request)

Create form

Create an empty draft form.

Reach also adds an automatic `form:{name}` tag that every submitter receives. A draft has no design
and is not reachable by visitors: save a design with the update form template operation, then take
the form live by setting its status to `active`. Creating a form does not consume AI credits.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_forms_form_resource import ReachV1FormsFormResource
from hostinger_api.models.reach_v1_forms_store_request import ReachV1FormsStoreRequest
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
    reach_v1_forms_store_request = hostinger_api.ReachV1FormsStoreRequest() # ReachV1FormsStoreRequest | 

    try:
        # Create form
        api_response = api_instance.create_form_v1(profile_uuid, reach_v1_forms_store_request)
        print("The response of ReachFormsApi->create_form_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->create_form_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_forms_store_request** | [**ReachV1FormsStoreRequest**](ReachV1FormsStoreRequest.md)|  | 

### Return type

[**ReachV1FormsFormResource**](ReachV1FormsFormResource.md)

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

# **duplicate_form_v1**
> ReachV1FormsFormResource duplicate_form_v1(profile_uuid, form_uuid)

Duplicate form

Copy a form into a new draft form with the same name and design.

The copy shares the source's automatic `form:{name}` tag; other submitter tags are not copied. The
copy is not live until its status is set to `active`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_forms_form_resource import ReachV1FormsFormResource
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
        # Duplicate form
        api_response = api_instance.duplicate_form_v1(profile_uuid, form_uuid)
        print("The response of ReachFormsApi->duplicate_form_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->duplicate_form_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 

### Return type

[**ReachV1FormsFormResource**](ReachV1FormsFormResource.md)

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
> ReachListFormsV1200Response list_forms_v1(profile_uuid, page=page, per_page=per_page, status=status)

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
    status = 'status_example' # str | Return only forms with this status. (optional)

    try:
        # List forms
        api_response = api_instance.list_forms_v1(profile_uuid, page=page, per_page=per_page, status=status)
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
 **status** | **str**| Return only forms with this status. | [optional] 

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

# **remove_form_submitter_tag_v1**
> CommonSuccessEmptyResource remove_form_submitter_tag_v1(profile_uuid, form_uuid, reach_v1_forms_remove_tag_request)

Remove form submitter tag

Stop a form from applying a tag to its future submitters.

Succeeds also when the form did not have the tag. Contacts who already received the tag keep it, and
the tag itself is not deleted. The automatic `form:{name}` tag cannot be removed and is rejected with
a conflict.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_forms_remove_tag_request import ReachV1FormsRemoveTagRequest
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
    reach_v1_forms_remove_tag_request = hostinger_api.ReachV1FormsRemoveTagRequest() # ReachV1FormsRemoveTagRequest | 

    try:
        # Remove form submitter tag
        api_response = api_instance.remove_form_submitter_tag_v1(profile_uuid, form_uuid, reach_v1_forms_remove_tag_request)
        print("The response of ReachFormsApi->remove_form_submitter_tag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->remove_form_submitter_tag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 
 **reach_v1_forms_remove_tag_request** | [**ReachV1FormsRemoveTagRequest**](ReachV1FormsRemoveTagRequest.md)|  | 

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
**409** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form_template_v1**
> ReachV1FormsFormTemplateVersionResource update_form_template_v1(profile_uuid, form_uuid, reach_v1_forms_update_template_request)

Update form template

Save `content` as the latest design of a form and return the stored version.

The HTML is sanitized and, unless the plan allows removing it, the Reach signature is added. Visitors
submit the form with an `email` field (required) and optional `name`, `surname` and `phone`. After
sanitizing, the design must contain a form container (`data-reach-form`), an email input
(`data-reach-field="email"`) and a submit button (`data-reach-submit`); otherwise the request fails
with `422` and `errors.content` lists `missing_form_container`, `missing_email_field` and/or
`missing_submit_button`.

A `draft` or `paused` form stays unreachable until its status is set to `active`, which publishes this
design. On a form that is already `active` the saved design is not public until the form is paused and
set to `active` again. Saving a design does not consume AI credits.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_forms_form_template_version_resource import ReachV1FormsFormTemplateVersionResource
from hostinger_api.models.reach_v1_forms_update_template_request import ReachV1FormsUpdateTemplateRequest
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
    reach_v1_forms_update_template_request = hostinger_api.ReachV1FormsUpdateTemplateRequest() # ReachV1FormsUpdateTemplateRequest | 

    try:
        # Update form template
        api_response = api_instance.update_form_template_v1(profile_uuid, form_uuid, reach_v1_forms_update_template_request)
        print("The response of ReachFormsApi->update_form_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->update_form_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 
 **reach_v1_forms_update_template_request** | [**ReachV1FormsUpdateTemplateRequest**](ReachV1FormsUpdateTemplateRequest.md)|  | 

### Return type

[**ReachV1FormsFormTemplateVersionResource**](ReachV1FormsFormTemplateVersionResource.md)

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

# **update_form_v1**
> ReachV1FormsFormResource update_form_v1(profile_uuid, form_uuid, reach_v1_forms_update_request)

Update form

Rename a form and/or change its status.

Setting a `draft` or `paused` form to `active` takes it live: its latest saved design is published
and visitors can submit it. `paused` and `draft` stop the form from accepting submissions. A form is
not reachable by visitors until it is taken live. Design changes saved while the form is already
`active` stay unpublished until the form is paused and set to `active` again. Renaming does not rename
the automatic `form:{name}` tag.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_forms_form_resource import ReachV1FormsFormResource
from hostinger_api.models.reach_v1_forms_update_request import ReachV1FormsUpdateRequest
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
    reach_v1_forms_update_request = hostinger_api.ReachV1FormsUpdateRequest() # ReachV1FormsUpdateRequest | 

    try:
        # Update form
        api_response = api_instance.update_form_v1(profile_uuid, form_uuid, reach_v1_forms_update_request)
        print("The response of ReachFormsApi->update_form_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachFormsApi->update_form_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **form_uuid** | **str**| Form uuid parameter | 
 **reach_v1_forms_update_request** | [**ReachV1FormsUpdateRequest**](ReachV1FormsUpdateRequest.md)|  | 

### Return type

[**ReachV1FormsFormResource**](ReachV1FormsFormResource.md)

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

