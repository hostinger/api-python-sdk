# BillingV1OrderOrderBillingAddressResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_order_billing_address_resource import BillingV1OrderOrderBillingAddressResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderOrderBillingAddressResource from a JSON string
billing_v1_order_order_billing_address_resource_instance = BillingV1OrderOrderBillingAddressResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderOrderBillingAddressResource.to_json())

# convert the object into a dict
billing_v1_order_order_billing_address_resource_dict = billing_v1_order_order_billing_address_resource_instance.to_dict()
# create an instance of BillingV1OrderOrderBillingAddressResource from a dict
billing_v1_order_order_billing_address_resource_from_dict = BillingV1OrderOrderBillingAddressResource.from_dict(billing_v1_order_order_billing_address_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


