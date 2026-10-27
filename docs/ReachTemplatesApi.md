# hostinger_api.ReachTemplatesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_email_template_v1**](ReachTemplatesApi.md#create_an_email_template_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/templates | Create an email template
[**get_email_template_v1**](ReachTemplatesApi.md#get_email_template_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/templates/{templateUuid} | Get email template
[**list_email_templates_v1**](ReachTemplatesApi.md#list_email_templates_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/templates | List email templates


# **create_an_email_template_v1**
> ReachV1TemplatesTemplateResource create_an_email_template_v1(profile_uuid, reach_v1_templates_store_request)

Create an email template

Create an email template in a profile.

The template holds the HTML body a campaign reuses, so it can be created before any
campaign exists. Only the template metadata comes back - keep the returned `uuid` to
reference it as the `template_uuid` of a campaign.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_templates_store_request import ReachV1TemplatesStoreRequest
from hostinger_api.models.reach_v1_templates_template_resource import ReachV1TemplatesTemplateResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTemplatesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_templates_store_request = hostinger_api.ReachV1TemplatesStoreRequest() # ReachV1TemplatesStoreRequest | 

    try:
        # Create an email template
        api_response = api_instance.create_an_email_template_v1(profile_uuid, reach_v1_templates_store_request)
        print("The response of ReachTemplatesApi->create_an_email_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTemplatesApi->create_an_email_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_templates_store_request** | [**ReachV1TemplatesStoreRequest**](ReachV1TemplatesStoreRequest.md)|  | 

### Return type

[**ReachV1TemplatesTemplateResource**](ReachV1TemplatesTemplateResource.md)

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

# **get_email_template_v1**
> ReachV1TemplatesTemplateDetailsResource get_email_template_v1(profile_uuid, template_uuid)

Get email template

Get one email template of the profile with its full HTML in `template_content`.

A campaign's email content is its template: to read what a campaign sends, get the campaign
and pass its `template_uuid` here. The HTML can be large, so fetch it only when the content
itself is needed, never to browse or pick templates - the list email templates endpoint does
that without content. Personalization tags such as `{{name}}` come back unrendered.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_templates_template_details_resource import ReachV1TemplatesTemplateDetailsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTemplatesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    template_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Template uuid parameter

    try:
        # Get email template
        api_response = api_instance.get_email_template_v1(profile_uuid, template_uuid)
        print("The response of ReachTemplatesApi->get_email_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTemplatesApi->get_email_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **template_uuid** | **str**| Template uuid parameter | 

### Return type

[**ReachV1TemplatesTemplateDetailsResource**](ReachV1TemplatesTemplateDetailsResource.md)

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

# **list_email_templates_v1**
> List[ReachV1TemplatesTemplateResource] list_email_templates_v1(profile_uuid)

List email templates

Get a list of the email templates in a profile, most recently updated first.

Templates are the reusable email bodies a campaign is built from. The list is not paginated
and only the metadata is returned, without the HTML content. Use the `uuid` of a template
as the `template_uuid` when creating a campaign. To read one template's HTML use the get
email template endpoint, and only when the content itself is needed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_templates_template_resource import ReachV1TemplatesTemplateResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachTemplatesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List email templates
        api_response = api_instance.list_email_templates_v1(profile_uuid)
        print("The response of ReachTemplatesApi->list_email_templates_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachTemplatesApi->list_email_templates_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1TemplatesTemplateResource]**](ReachV1TemplatesTemplateResource.md)

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

