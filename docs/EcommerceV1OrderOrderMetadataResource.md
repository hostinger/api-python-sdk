# EcommerceV1OrderOrderMetadataResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, str]** | Custom attributes collected at checkout, keyed by attribute name, or null. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_metadata_resource import EcommerceV1OrderOrderMetadataResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderMetadataResource from a JSON string
ecommerce_v1_order_order_metadata_resource_instance = EcommerceV1OrderOrderMetadataResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderMetadataResource.to_json())

# convert the object into a dict
ecommerce_v1_order_order_metadata_resource_dict = ecommerce_v1_order_order_metadata_resource_instance.to_dict()
# create an instance of EcommerceV1OrderOrderMetadataResource from a dict
ecommerce_v1_order_order_metadata_resource_from_dict = EcommerceV1OrderOrderMetadataResource.from_dict(ecommerce_v1_order_order_metadata_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


