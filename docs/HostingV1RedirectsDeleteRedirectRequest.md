# HostingV1RedirectsDeleteRedirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Source URL returned by the list redirects endpoint | 

## Example

```python
from hostinger_api.models.hosting_v1_redirects_delete_redirect_request import HostingV1RedirectsDeleteRedirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1RedirectsDeleteRedirectRequest from a JSON string
hosting_v1_redirects_delete_redirect_request_instance = HostingV1RedirectsDeleteRedirectRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1RedirectsDeleteRedirectRequest.to_json())

# convert the object into a dict
hosting_v1_redirects_delete_redirect_request_dict = hosting_v1_redirects_delete_redirect_request_instance.to_dict()
# create an instance of HostingV1RedirectsDeleteRedirectRequest from a dict
hosting_v1_redirects_delete_redirect_request_from_dict = HostingV1RedirectsDeleteRedirectRequest.from_dict(hosting_v1_redirects_delete_redirect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


