# VPSV1FirewallRulesReplaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[VPSV1FirewallRulesStoreRequest]**](VPSV1FirewallRulesStoreRequest.md) | The complete set of firewall rules that atomically replaces all existing rules in the group | 
**sync** | **bool** | Synchronize the firewall group to all its virtual machines after replacing the rules | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_firewall_rules_replace_request import VPSV1FirewallRulesReplaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1FirewallRulesReplaceRequest from a JSON string
vpsv1_firewall_rules_replace_request_instance = VPSV1FirewallRulesReplaceRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1FirewallRulesReplaceRequest.to_json())

# convert the object into a dict
vpsv1_firewall_rules_replace_request_dict = vpsv1_firewall_rules_replace_request_instance.to_dict()
# create an instance of VPSV1FirewallRulesReplaceRequest from a dict
vpsv1_firewall_rules_replace_request_from_dict = VPSV1FirewallRulesReplaceRequest.from_dict(vpsv1_firewall_rules_replace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


