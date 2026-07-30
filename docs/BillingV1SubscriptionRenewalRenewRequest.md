# BillingV1SubscriptionRenewalRenewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **int** | Payment method ID, default will be used if not provided | [optional] 
**coupons** | **List[object]** | Discount coupon codes | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_subscription_renewal_renew_request import BillingV1SubscriptionRenewalRenewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1SubscriptionRenewalRenewRequest from a JSON string
billing_v1_subscription_renewal_renew_request_instance = BillingV1SubscriptionRenewalRenewRequest.from_json(json)
# print the JSON string representation of the object
print(BillingV1SubscriptionRenewalRenewRequest.to_json())

# convert the object into a dict
billing_v1_subscription_renewal_renew_request_dict = billing_v1_subscription_renewal_renew_request_instance.to_dict()
# create an instance of BillingV1SubscriptionRenewalRenewRequest from a dict
billing_v1_subscription_renewal_renew_request_from_dict = BillingV1SubscriptionRenewalRenewRequest.from_dict(billing_v1_subscription_renewal_renew_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


