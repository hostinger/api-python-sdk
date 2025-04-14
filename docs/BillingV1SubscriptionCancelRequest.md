# BillingV1SubscriptionCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** | Cancellation reason code | [optional] 
**cancel_option** | **str** | Cancellation option | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_subscription_cancel_request import BillingV1SubscriptionCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1SubscriptionCancelRequest from a JSON string
billing_v1_subscription_cancel_request_instance = BillingV1SubscriptionCancelRequest.from_json(json)
# print the JSON string representation of the object
print(BillingV1SubscriptionCancelRequest.to_json())

# convert the object into a dict
billing_v1_subscription_cancel_request_dict = billing_v1_subscription_cancel_request_instance.to_dict()
# create an instance of BillingV1SubscriptionCancelRequest from a dict
billing_v1_subscription_cancel_request_from_dict = BillingV1SubscriptionCancelRequest.from_dict(billing_v1_subscription_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


