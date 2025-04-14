# VPSGetFirewallListV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1FirewallFirewallResource]**](VPSV1FirewallFirewallResource.md) | Array of [&#x60;VPS.V1.Firewall.FirewallResource&#x60;](#model/vpsv1firewallfirewallresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger-api.models.vps_get_firewall_list_v1200_response import VPSGetFirewallListV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VPSGetFirewallListV1200Response from a JSON string
vps_get_firewall_list_v1200_response_instance = VPSGetFirewallListV1200Response.from_json(json)
# print the JSON string representation of the object
print(VPSGetFirewallListV1200Response.to_json())

# convert the object into a dict
vps_get_firewall_list_v1200_response_dict = vps_get_firewall_list_v1200_response_instance.to_dict()
# create an instance of VPSGetFirewallListV1200Response from a dict
vps_get_firewall_list_v1200_response_from_dict = VPSGetFirewallListV1200Response.from_dict(vps_get_firewall_list_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


