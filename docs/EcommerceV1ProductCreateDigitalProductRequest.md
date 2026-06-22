# EcommerceV1ProductCreateDigitalProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The product name. | 
**price** | **int** | Price in the smallest currency unit (e.g. cents). Must be positive. | 
**description** | **str** | The product description. | [optional] 
**currency** | **str** | ISO 4217 currency code. Defaults to the store&#39;s default currency when omitted. | [optional] 
**download_url** | **str** | Optional external download link delivered to the customer after purchase. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_create_digital_product_request import EcommerceV1ProductCreateDigitalProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductCreateDigitalProductRequest from a JSON string
ecommerce_v1_product_create_digital_product_request_instance = EcommerceV1ProductCreateDigitalProductRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductCreateDigitalProductRequest.to_json())

# convert the object into a dict
ecommerce_v1_product_create_digital_product_request_dict = ecommerce_v1_product_create_digital_product_request_instance.to_dict()
# create an instance of EcommerceV1ProductCreateDigitalProductRequest from a dict
ecommerce_v1_product_create_digital_product_request_from_dict = EcommerceV1ProductCreateDigitalProductRequest.from_dict(ecommerce_v1_product_create_digital_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


