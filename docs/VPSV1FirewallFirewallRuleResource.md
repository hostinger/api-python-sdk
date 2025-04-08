# VPSV1FirewallFirewallRuleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Firewall rule ID | [optional] 
**action** | **str** | Firewall rule action | [optional] 
**protocol** | **str** | Firewall rule protocol | [optional] 
**port** | **str** | Firewall rule destination port: single or port range | [optional] 
**source** | **str** | Firewall rule source. Can be &#x60;any&#x60; or &#x60;custom&#x60; | [optional] 
**source_detail** | **str** | Firewall rule source detail. Can be &#x60;any&#x60; or IP address, CIDR or range | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_firewall_firewall_rule_resource import VPSV1FirewallFirewallRuleResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1FirewallFirewallRuleResource from a JSON string
vpsv1_firewall_firewall_rule_resource_instance = VPSV1FirewallFirewallRuleResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1FirewallFirewallRuleResource.to_json())

# convert the object into a dict
vpsv1_firewall_firewall_rule_resource_dict = vpsv1_firewall_firewall_rule_resource_instance.to_dict()
# create an instance of VPSV1FirewallFirewallRuleResource from a dict
vpsv1_firewall_firewall_rule_resource_from_dict = VPSV1FirewallFirewallRuleResource.from_dict(vpsv1_firewall_firewall_rule_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


