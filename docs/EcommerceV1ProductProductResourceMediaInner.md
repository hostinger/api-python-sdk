# EcommerceV1ProductProductResourceMediaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The media URL. | [optional] 
**type** | **str** | The media type, e.g. image or video. | [optional] 
**is_thumbnail** | **bool** | Whether this media is the product&#39;s thumbnail. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_resource_media_inner import EcommerceV1ProductProductResourceMediaInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductResourceMediaInner from a JSON string
ecommerce_v1_product_product_resource_media_inner_instance = EcommerceV1ProductProductResourceMediaInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductResourceMediaInner.to_json())

# convert the object into a dict
ecommerce_v1_product_product_resource_media_inner_dict = ecommerce_v1_product_product_resource_media_inner_instance.to_dict()
# create an instance of EcommerceV1ProductProductResourceMediaInner from a dict
ecommerce_v1_product_product_resource_media_inner_from_dict = EcommerceV1ProductProductResourceMediaInner.from_dict(ecommerce_v1_product_product_resource_media_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


