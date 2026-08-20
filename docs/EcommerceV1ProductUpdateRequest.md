# EcommerceV1ProductUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The product name. | [optional] 
**description** | **str** | The product description. | [optional] 
**status** | **str** | Set \&quot;published\&quot; to make the product buyable, \&quot;draft\&quot; to hide it, or \&quot;archived\&quot; to retire it. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_update_request import EcommerceV1ProductUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductUpdateRequest from a JSON string
ecommerce_v1_product_update_request_instance = EcommerceV1ProductUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductUpdateRequest.to_json())

# convert the object into a dict
ecommerce_v1_product_update_request_dict = ecommerce_v1_product_update_request_instance.to_dict()
# create an instance of EcommerceV1ProductUpdateRequest from a dict
ecommerce_v1_product_update_request_from_dict = EcommerceV1ProductUpdateRequest.from_dict(ecommerce_v1_product_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


