# HostingV1RedirectsRedirectResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Source URL | [optional] 
**to** | **str** | Destination URL | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_redirects_redirect_resource import HostingV1RedirectsRedirectResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1RedirectsRedirectResource from a JSON string
hosting_v1_redirects_redirect_resource_instance = HostingV1RedirectsRedirectResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1RedirectsRedirectResource.to_json())

# convert the object into a dict
hosting_v1_redirects_redirect_resource_dict = hosting_v1_redirects_redirect_resource_instance.to_dict()
# create an instance of HostingV1RedirectsRedirectResource from a dict
hosting_v1_redirects_redirect_resource_from_dict = HostingV1RedirectsRedirectResource.from_dict(hosting_v1_redirects_redirect_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


