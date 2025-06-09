# hostinger_api.BillingCatalogApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item_list_v1**](BillingCatalogApi.md#get_catalog_item_list_v1) | **GET** /api/billing/v1/catalog | Get catalog item list


# **get_catalog_item_list_v1**
> List[BillingV1CatalogCatalogItemResource] get_catalog_item_list_v1(category=category, name=name)

Get catalog item list

This endpoint retrieves a list of catalog items available for order. 

Prices in catalog items is displayed as cents (without floating point), e.g: float `17.99` is displayed as integer `1799`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_catalog_catalog_item_resource import BillingV1CatalogCatalogItemResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingCatalogApi(api_client)
    category = 'VPS' # str | Filter catalog items by category (optional)
    name = '.COM*' # str | Filter catalog items by name. Use `*` for wildcard search, e.g. `.COM*` to find .com domain (optional)

    try:
        # Get catalog item list
        api_response = api_instance.get_catalog_item_list_v1(category=category, name=name)
        print("The response of BillingCatalogApi->get_catalog_item_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingCatalogApi->get_catalog_item_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter catalog items by category | [optional] 
 **name** | **str**| Filter catalog items by name. Use &#x60;*&#x60; for wildcard search, e.g. &#x60;.COM*&#x60; to find .com domain | [optional] 

### Return type

[**List[BillingV1CatalogCatalogItemResource]**](BillingV1CatalogCatalogItemResource.md)

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

