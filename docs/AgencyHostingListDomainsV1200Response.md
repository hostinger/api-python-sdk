# AgencyHostingListDomainsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgencyHostingV1DomainsDomainResource]**](AgencyHostingV1DomainsDomainResource.md) | Array of [&#x60;AgencyHosting.V1.Domains.DomainResource&#x60;](#model/agencyhostingv1domainsdomainresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_list_domains_v1200_response import AgencyHostingListDomainsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingListDomainsV1200Response from a JSON string
agency_hosting_list_domains_v1200_response_instance = AgencyHostingListDomainsV1200Response.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingListDomainsV1200Response.to_json())

# convert the object into a dict
agency_hosting_list_domains_v1200_response_dict = agency_hosting_list_domains_v1200_response_instance.to_dict()
# create an instance of AgencyHostingListDomainsV1200Response from a dict
agency_hosting_list_domains_v1200_response_from_dict = AgencyHostingListDomainsV1200Response.from_dict(agency_hosting_list_domains_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


