# EcommerceGetStoresV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EcommerceV1StoreStoreResource]**](EcommerceV1StoreStoreResource.md) | Array of [&#x60;Ecommerce.V1.Store.StoreResource&#x60;](#model/ecommercev1storestoreresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_get_stores_v1200_response import EcommerceGetStoresV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceGetStoresV1200Response from a JSON string
ecommerce_get_stores_v1200_response_instance = EcommerceGetStoresV1200Response.from_json(json)
# print the JSON string representation of the object
print(EcommerceGetStoresV1200Response.to_json())

# convert the object into a dict
ecommerce_get_stores_v1200_response_dict = ecommerce_get_stores_v1200_response_instance.to_dict()
# create an instance of EcommerceGetStoresV1200Response from a dict
ecommerce_get_stores_v1200_response_from_dict = EcommerceGetStoresV1200Response.from_dict(ecommerce_get_stores_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


