# EcommerceV1StoreStoreMetadataResourceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_payment_methods** | **bool** | Whether the store has at least one payment method connected. | [optional] 
**has_shipping** | **bool** | Whether the store has at least one shipping option configured. | [optional] 
**default_currency_code** | **str** | The default currency code of the store. | [optional] 
**default_currency** | [**EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency**](EcommerceV1StoreStoreMetadataResourceMetadataDefaultCurrency.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_metadata_resource_metadata import EcommerceV1StoreStoreMetadataResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreMetadataResourceMetadata from a JSON string
ecommerce_v1_store_store_metadata_resource_metadata_instance = EcommerceV1StoreStoreMetadataResourceMetadata.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreMetadataResourceMetadata.to_json())

# convert the object into a dict
ecommerce_v1_store_store_metadata_resource_metadata_dict = ecommerce_v1_store_store_metadata_resource_metadata_instance.to_dict()
# create an instance of EcommerceV1StoreStoreMetadataResourceMetadata from a dict
ecommerce_v1_store_store_metadata_resource_metadata_from_dict = EcommerceV1StoreStoreMetadataResourceMetadata.from_dict(ecommerce_v1_store_store_metadata_resource_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


