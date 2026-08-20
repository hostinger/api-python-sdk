# EcommerceV1DiscountDiscountResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The discount ID, required by every other discount endpoint. | [optional] 
**code** | **str** | The discount code customers enter at checkout. | [optional] 
**name** | **str** | The discount name, or null. | [optional] 
**type** | **str** | The discount type, or null. | [optional] 
**value** | **int** | The discount value, or null. Percentage is 1-100; fixed is in the smallest currency unit. | [optional] 
**allocation** | **str** | Whether the discount applies to the cart total or to each item, or null. | [optional] 
**is_disabled** | **bool** | Whether the discount is disabled. | [optional] 
**starts_at** | **datetime** | When the discount becomes active. | [optional] 
**ends_at** | **datetime** | When the discount expires, or null. | [optional] 
**usage_limit** | **int** | Maximum number of redemptions, or null for unlimited. | [optional] 
**usage_count** | **int** | Number of times the discount has been redeemed. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_discount_discount_resource import EcommerceV1DiscountDiscountResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1DiscountDiscountResource from a JSON string
ecommerce_v1_discount_discount_resource_instance = EcommerceV1DiscountDiscountResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1DiscountDiscountResource.to_json())

# convert the object into a dict
ecommerce_v1_discount_discount_resource_dict = ecommerce_v1_discount_discount_resource_instance.to_dict()
# create an instance of EcommerceV1DiscountDiscountResource from a dict
ecommerce_v1_discount_discount_resource_from_dict = EcommerceV1DiscountDiscountResource.from_dict(ecommerce_v1_discount_discount_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


