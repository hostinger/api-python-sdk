# ReachV1WebsitesWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Pass this to the disconnect endpoint matching &#x60;platform_type&#x60;. | [optional] 
**platform_type** | **str** | &#x60;wordpress&#x60;, &#x60;website_builder&#x60; (AI Website Builder site built manually) or &#x60;horizons&#x60; (site built with the agentic AI Website Builder). | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_websites_website_resource import ReachV1WebsitesWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1WebsitesWebsiteResource from a JSON string
reach_v1_websites_website_resource_instance = ReachV1WebsitesWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1WebsitesWebsiteResource.to_json())

# convert the object into a dict
reach_v1_websites_website_resource_dict = reach_v1_websites_website_resource_instance.to_dict()
# create an instance of ReachV1WebsitesWebsiteResource from a dict
reach_v1_websites_website_resource_from_dict = ReachV1WebsitesWebsiteResource.from_dict(reach_v1_websites_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


