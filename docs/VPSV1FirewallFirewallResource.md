# VPSV1FirewallFirewallResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Firewall ID | [optional] 
**name** | **str** | Firewall name | [optional] 
**is_synced** | **bool** | Is current firewall synced with VPS | [optional] 
**rules** | [**List[VPSV1FirewallFirewallRuleResource]**](VPSV1FirewallFirewallRuleResource.md) | Array of [&#x60;VPS.V1.Firewall.FirewallRuleResource&#x60;](#model/vpsv1firewallfirewallruleresource) | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_firewall_firewall_resource import VPSV1FirewallFirewallResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1FirewallFirewallResource from a JSON string
vpsv1_firewall_firewall_resource_instance = VPSV1FirewallFirewallResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1FirewallFirewallResource.to_json())

# convert the object into a dict
vpsv1_firewall_firewall_resource_dict = vpsv1_firewall_firewall_resource_instance.to_dict()
# create an instance of VPSV1FirewallFirewallResource from a dict
vpsv1_firewall_firewall_resource_from_dict = VPSV1FirewallFirewallResource.from_dict(vpsv1_firewall_firewall_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


