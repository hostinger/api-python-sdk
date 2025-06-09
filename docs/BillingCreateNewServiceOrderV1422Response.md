# BillingCreateNewServiceOrderV1422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Validation error message | [optional] 
**errors** | [**BillingCreateNewServiceOrderV1422ResponseErrors**](BillingCreateNewServiceOrderV1422ResponseErrors.md) |  | [optional] 
**correlation_id** | **str** | Request correlation ID | [optional] 

## Example

```python
from hostinger_api.models.billing_create_new_service_order_v1422_response import BillingCreateNewServiceOrderV1422Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCreateNewServiceOrderV1422Response from a JSON string
billing_create_new_service_order_v1422_response_instance = BillingCreateNewServiceOrderV1422Response.from_json(json)
# print the JSON string representation of the object
print(BillingCreateNewServiceOrderV1422Response.to_json())

# convert the object into a dict
billing_create_new_service_order_v1422_response_dict = billing_create_new_service_order_v1422_response_instance.to_dict()
# create an instance of BillingCreateNewServiceOrderV1422Response from a dict
billing_create_new_service_order_v1422_response_from_dict = BillingCreateNewServiceOrderV1422Response.from_dict(billing_create_new_service_order_v1422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


