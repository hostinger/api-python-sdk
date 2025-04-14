# BillingV1SubscriptionSubscriptionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription ID | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**billing_period** | **int** |  | [optional] 
**billing_period_unit** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**total_price** | **int** | Total price in cents | [optional] 
**renewal_price** | **int** | Renewal price in cents | [optional] 
**auto_renew** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**next_billing_at** | **datetime** |  | [optional] 
**canceled_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.billing_v1_subscription_subscription_resource import BillingV1SubscriptionSubscriptionResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1SubscriptionSubscriptionResource from a JSON string
billing_v1_subscription_subscription_resource_instance = BillingV1SubscriptionSubscriptionResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1SubscriptionSubscriptionResource.to_json())

# convert the object into a dict
billing_v1_subscription_subscription_resource_dict = billing_v1_subscription_subscription_resource_instance.to_dict()
# create an instance of BillingV1SubscriptionSubscriptionResource from a dict
billing_v1_subscription_subscription_resource_from_dict = BillingV1SubscriptionSubscriptionResource.from_dict(billing_v1_subscription_subscription_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


