# DNSV1PropagationVantagePointResource

Answer of a public resolver at one location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country code of the resolver | [optional] 
**provider** | **str** | Resolver provider | [optional] 
**ip** | **str** | IP address of the resolver | [optional] 
**location** | **str** | Location of the resolver | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**records** | **List[str]** | Records the resolver returned; null when it returned none or could not be queried | [optional] 
**is_propagated** | **bool** | Whether this location returns the same records as the authoritative nameservers. For GeoDNS domains, whose nameservers answer differently by region, true means the location returned a record. A records served from the Hostinger CDN count as propagated when the location also returns CDN addresses. True when every responding authoritative nameserver returns no records. Null when the location could not be queried or no authoritative answer could be compared. | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_propagation_vantage_point_resource import DNSV1PropagationVantagePointResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1PropagationVantagePointResource from a JSON string
dnsv1_propagation_vantage_point_resource_instance = DNSV1PropagationVantagePointResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1PropagationVantagePointResource.to_json())

# convert the object into a dict
dnsv1_propagation_vantage_point_resource_dict = dnsv1_propagation_vantage_point_resource_instance.to_dict()
# create an instance of DNSV1PropagationVantagePointResource from a dict
dnsv1_propagation_vantage_point_resource_from_dict = DNSV1PropagationVantagePointResource.from_dict(dnsv1_propagation_vantage_point_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


