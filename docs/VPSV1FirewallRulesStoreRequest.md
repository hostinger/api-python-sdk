# VPSV1FirewallRulesStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | 
**port** | **str** | Port or port range, ex: 1024:2048 | 
**source** | **str** |  | 
**source_detail** | **str** | IP range, CIDR, single IP or &#x60;any&#x60; | 

## Example

```python
from hostinger-api.models.vpsv1_firewall_rules_store_request import VPSV1FirewallRulesStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1FirewallRulesStoreRequest from a JSON string
vpsv1_firewall_rules_store_request_instance = VPSV1FirewallRulesStoreRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1FirewallRulesStoreRequest.to_json())

# convert the object into a dict
vpsv1_firewall_rules_store_request_dict = vpsv1_firewall_rules_store_request_instance.to_dict()
# create an instance of VPSV1FirewallRulesStoreRequest from a dict
vpsv1_firewall_rules_store_request_from_dict = VPSV1FirewallRulesStoreRequest.from_dict(vpsv1_firewall_rules_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


