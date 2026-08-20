# EcommerceV1DiscountCreateDiscountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The discount code customers enter at checkout. | 
**name** | **str** | A human-friendly discount name. | [optional] 
**type** | **str** | The discount type. | 
**value** | **int** | For percentage discounts a whole number 1-100; for fixed discounts an amount in the smallest currency unit (e.g. $10 is 1000). Ignored for free_shipping. | 
**allocation** | **str** | Whether the discount applies to the cart total or to each eligible item. | [optional] 
**starts_at** | **datetime** | When the discount becomes active. A bare date (2026-11-27) anchors to time_zone. Defaults to now when omitted. | [optional] 
**ends_at** | **datetime** | When the discount expires. A bare date runs to the end of that day in time_zone. Never expires when omitted. | [optional] 
**usage_limit** | **int** | Maximum number of times the discount can be redeemed. | [optional] 
**min_cart_value** | **int** | Minimum cart value in the smallest currency unit required for the discount to apply. | [optional] 
**time_zone** | **str** | IANA time zone used to interpret starts_at and ends_at. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_discount_create_discount_request import EcommerceV1DiscountCreateDiscountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1DiscountCreateDiscountRequest from a JSON string
ecommerce_v1_discount_create_discount_request_instance = EcommerceV1DiscountCreateDiscountRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1DiscountCreateDiscountRequest.to_json())

# convert the object into a dict
ecommerce_v1_discount_create_discount_request_dict = ecommerce_v1_discount_create_discount_request_instance.to_dict()
# create an instance of EcommerceV1DiscountCreateDiscountRequest from a dict
ecommerce_v1_discount_create_discount_request_from_dict = EcommerceV1DiscountCreateDiscountRequest.from_dict(ecommerce_v1_discount_create_discount_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


