# DNSV1PropagationPropagationReportResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authoritative** | [**DNSV1PropagationAuthoritativeAnswerResource**](DNSV1PropagationAuthoritativeAnswerResource.md) |  | [optional] 
**vantage_points** | [**List[DNSV1PropagationVantagePointResource]**](DNSV1PropagationVantagePointResource.md) | Answers of public resolvers at locations around the world | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_propagation_propagation_report_resource import DNSV1PropagationPropagationReportResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1PropagationPropagationReportResource from a JSON string
dnsv1_propagation_propagation_report_resource_instance = DNSV1PropagationPropagationReportResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1PropagationPropagationReportResource.to_json())

# convert the object into a dict
dnsv1_propagation_propagation_report_resource_dict = dnsv1_propagation_propagation_report_resource_instance.to_dict()
# create an instance of DNSV1PropagationPropagationReportResource from a dict
dnsv1_propagation_propagation_report_resource_from_dict = DNSV1PropagationPropagationReportResource.from_dict(dnsv1_propagation_propagation_report_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


