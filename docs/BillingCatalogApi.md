# @hostinger/api.BillingCatalogApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item_list_v1**](BillingCatalogApi.md#get_catalog_item_list_v1) | **GET** /api/billing/v1/catalog | Get catalog item list


# **get_catalog_item_list_v1**
> List[BillingV1CatalogCatalogItemResource] get_catalog_item_list_v1()

Get catalog item list

This endpoint retrieves a list of catalog items available for order. 

Prices in catalog items is displayed as cents (without floating point), e.g: float `17.99` is displayed as integer `1799`.

### Example

* Bearer Authentication (apiToken):

```python
import @hostinger/api
from @hostinger/api.models.billing_v1_catalog_catalog_item_resource import BillingV1CatalogCatalogItemResource
from @hostinger/api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = @hostinger/api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with @hostinger/api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = @hostinger/api.BillingCatalogApi(api_client)

    try:
        # Get catalog item list
        api_response = api_instance.get_catalog_item_list_v1()
        print("The response of BillingCatalogApi->get_catalog_item_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingCatalogApi->get_catalog_item_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

