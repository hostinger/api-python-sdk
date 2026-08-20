# EcommerceV1OrderFulfillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EcommerceV1OrderFulfillRequestItemsInner]**](EcommerceV1OrderFulfillRequestItemsInner.md) | Line items to fulfil. Omit to fulfil every remaining unfulfilled item. | [optional] 
**tracking_number** | **str** | Carrier tracking number for the shipment. | [optional] 
**tracking_url** | **str** | Public tracking URL for the shipment. Requires tracking_number. | [optional] 
**notify_customer** | **bool** | Whether to email the customer about the fulfilment. Defaults to true. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_fulfill_request import EcommerceV1OrderFulfillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderFulfillRequest from a JSON string
ecommerce_v1_order_fulfill_request_instance = EcommerceV1OrderFulfillRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderFulfillRequest.to_json())

# convert the object into a dict
ecommerce_v1_order_fulfill_request_dict = ecommerce_v1_order_fulfill_request_instance.to_dict()
# create an instance of EcommerceV1OrderFulfillRequest from a dict
ecommerce_v1_order_fulfill_request_from_dict = EcommerceV1OrderFulfillRequest.from_dict(ecommerce_v1_order_fulfill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


