# DomainsV1AvailabilityAlternativesFromDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name to base the suggestions on | 
**limit** | **int** | Amount of domain names to suggest | 

## Example

```python
from hostinger_api.models.domains_v1_availability_alternatives_from_domain_request import DomainsV1AvailabilityAlternativesFromDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1AvailabilityAlternativesFromDomainRequest from a JSON string
domains_v1_availability_alternatives_from_domain_request_instance = DomainsV1AvailabilityAlternativesFromDomainRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1AvailabilityAlternativesFromDomainRequest.to_json())

# convert the object into a dict
domains_v1_availability_alternatives_from_domain_request_dict = domains_v1_availability_alternatives_from_domain_request_instance.to_dict()
# create an instance of DomainsV1AvailabilityAlternativesFromDomainRequest from a dict
domains_v1_availability_alternatives_from_domain_request_from_dict = DomainsV1AvailabilityAlternativesFromDomainRequest.from_dict(domains_v1_availability_alternatives_from_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


