# EcommerceV1StoreStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 country code. | [optional] 
**company_email** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**language** | **str** | ISO 639-1 language code. | [optional] 
**sales_channel** | [**EcommerceV1StoreStoreRequestSalesChannel**](EcommerceV1StoreStoreRequestSalesChannel.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_request import EcommerceV1StoreStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreRequest from a JSON string
ecommerce_v1_store_store_request_instance = EcommerceV1StoreStoreRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreRequest.to_json())

# convert the object into a dict
ecommerce_v1_store_store_request_dict = ecommerce_v1_store_store_request_instance.to_dict()
# create an instance of EcommerceV1StoreStoreRequest from a dict
ecommerce_v1_store_store_request_from_dict = EcommerceV1StoreStoreRequest.from_dict(ecommerce_v1_store_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


