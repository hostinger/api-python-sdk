# EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency

The store's default currency, or null when unset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**symbol_native** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_plural** | **str** |  | [optional] 
**decimal_digits** | **int** |  | [optional] 
**rounding** | **float** |  | [optional] 
**template** | **str** |  | [optional] 
**min_amount** | **float** |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_metadata_resource_metadata_default_currency import EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency from a JSON string
ecommerce_v1_store_store_metadata_resource_metadata_default_currency_instance = EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency.to_json())

# convert the object into a dict
ecommerce_v1_store_store_metadata_resource_metadata_default_currency_dict = ecommerce_v1_store_store_metadata_resource_metadata_default_currency_instance.to_dict()
# create an instance of EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency from a dict
ecommerce_v1_store_store_metadata_resource_metadata_default_currency_from_dict = EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency.from_dict(ecommerce_v1_store_store_metadata_resource_metadata_default_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


