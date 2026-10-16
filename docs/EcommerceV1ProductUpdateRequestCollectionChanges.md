# EcommerceV1ProductUpdateRequestCollectionChanges

Adds the product to or removes it from collections without touching its other collections. Send at least one collection in add or remove.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | [**List[EcommerceV1ProductUpdateRequestCollectionChangesAddInner]**](EcommerceV1ProductUpdateRequestCollectionChangesAddInner.md) | Collections to add the product to. Every id must exist in the store. | [optional] 
**remove** | [**List[EcommerceV1ProductUpdateRequestCollectionChangesAddInner]**](EcommerceV1ProductUpdateRequestCollectionChangesAddInner.md) | Collections to take the product out of. Ids the product is not in are ignored. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_update_request_collection_changes import EcommerceV1ProductUpdateRequestCollectionChanges

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductUpdateRequestCollectionChanges from a JSON string
ecommerce_v1_product_update_request_collection_changes_instance = EcommerceV1ProductUpdateRequestCollectionChanges.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductUpdateRequestCollectionChanges.to_json())

# convert the object into a dict
ecommerce_v1_product_update_request_collection_changes_dict = ecommerce_v1_product_update_request_collection_changes_instance.to_dict()
# create an instance of EcommerceV1ProductUpdateRequestCollectionChanges from a dict
ecommerce_v1_product_update_request_collection_changes_from_dict = EcommerceV1ProductUpdateRequestCollectionChanges.from_dict(ecommerce_v1_product_update_request_collection_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


