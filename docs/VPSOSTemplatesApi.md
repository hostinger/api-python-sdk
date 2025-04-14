# hostinger-api.VPSOSTemplatesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template_list_v1**](VPSOSTemplatesApi.md#get_template_list_v1) | **GET** /api/vps/v1/templates | Get template list
[**get_template_v1**](VPSOSTemplatesApi.md#get_template_v1) | **GET** /api/vps/v1/templates/{templateId} | Get template


# **get_template_list_v1**
> List[VPSV1TemplateTemplateResource] get_template_list_v1()

Get template list

This endpoint retrieves a list of available OS templates for virtual machines.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.vpsv1_template_template_resource import VPSV1TemplateTemplateResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.VPSOSTemplatesApi(api_client)

    try:
        # Get template list
        api_response = api_instance.get_template_list_v1()
        print("The response of VPSOSTemplatesApi->get_template_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSOSTemplatesApi->get_template_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VPSV1TemplateTemplateResource]**](VPSV1TemplateTemplateResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_v1**
> VPSV1TemplateTemplateResource get_template_v1(template_id)

Get template

This endpoint retrieves details of a specific OS template for virtual machines.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.vpsv1_template_template_resource import VPSV1TemplateTemplateResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.VPSOSTemplatesApi(api_client)
    template_id = 2868928 # int | Template ID

    try:
        # Get template
        api_response = api_instance.get_template_v1(template_id)
        print("The response of VPSOSTemplatesApi->get_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSOSTemplatesApi->get_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Template ID | 

### Return type

[**VPSV1TemplateTemplateResource**](VPSV1TemplateTemplateResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

