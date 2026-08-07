# ReachV1ContactsSegmentsProfileStoreRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | A built-in contact attribute, or &#x60;cf:{fieldUuid}&#x60; to target a custom contact field. Custom fields are addressed by field UUID; their slug is not accepted.  Built-in attributes: &#x60;email&#x60;, &#x60;note&#x60;, &#x60;domain&#x60;, &#x60;source&#x60;, &#x60;opt_in_method&#x60;, &#x60;subscription_status&#x60;, &#x60;subscribed_at&#x60;, &#x60;unsubscribed_at&#x60;, &#x60;created_at&#x60;, &#x60;tag&#x60;, &#x60;campaigns&#x60;, &#x60;processed&#x60;, &#x60;opened&#x60;, &#x60;clicked&#x60;, &#x60;delivered&#x60;, &#x60;bounced&#x60;, &#x60;soft_bounced&#x60;, &#x60;dropped&#x60;.  Which operators are accepted depends on the attribute. | 
**operator** | **str** |  | 
**value** | **str** | Always a string, including for numeric and date comparisons | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_profile_store_request_conditions_inner import ReachV1ContactsSegmentsProfileStoreRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsProfileStoreRequestConditionsInner from a JSON string
reach_v1_contacts_segments_profile_store_request_conditions_inner_instance = ReachV1ContactsSegmentsProfileStoreRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsProfileStoreRequestConditionsInner.to_json())

# convert the object into a dict
reach_v1_contacts_segments_profile_store_request_conditions_inner_dict = reach_v1_contacts_segments_profile_store_request_conditions_inner_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsProfileStoreRequestConditionsInner from a dict
reach_v1_contacts_segments_profile_store_request_conditions_inner_from_dict = ReachV1ContactsSegmentsProfileStoreRequestConditionsInner.from_dict(reach_v1_contacts_segments_profile_store_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


