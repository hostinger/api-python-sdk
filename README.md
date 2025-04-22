# Hostinger API Python SDK

[![PyPI version](https://badge.fury.io/py/hostinger_api.svg)](https://badge.fury.io/py/hostinger_api)

## About
This is a Python SDK for the [Hostinger API](https://developers.hostinger.com).

For more information, please visit [https://developers.hostinger.com](https://developers.hostinger.com).

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

Setup new virtual environment (optional but recommended):
```sh
python3 -m venv venv
source venv/bin/activate
```

Install the package via [pip](https://pypi.org/project/pip/):
```sh
pip install hostinger_api
```

Then import the package:
```python
import hostinger_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hostinger_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import hostinger_api
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingCatalogApi(api_client)

    try:
        # Get catalog item list
        api_response = api_instance.get_catalog_item_list_v1()
        print("The response of BillingCatalogApi->get_catalog_item_list_v1:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingCatalogApi->get_catalog_item_list_v1: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://developers.hostinger.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BillingCatalogApi* | [**get_catalog_item_list_v1**](docs/BillingCatalogApi.md#get_catalog_item_list_v1) | **GET** /api/billing/v1/catalog | Get catalog item list
*BillingOrdersApi* | [**create_new_service_order_v1**](docs/BillingOrdersApi.md#create_new_service_order_v1) | **POST** /api/billing/v1/orders | Create new service order
*BillingPaymentMethodsApi* | [**delete_payment_method_v1**](docs/BillingPaymentMethodsApi.md#delete_payment_method_v1) | **DELETE** /api/billing/v1/payment-methods/{paymentMethodId} | Delete payment method
*BillingPaymentMethodsApi* | [**get_payment_method_list_v1**](docs/BillingPaymentMethodsApi.md#get_payment_method_list_v1) | **GET** /api/billing/v1/payment-methods | Get payment method list
*BillingPaymentMethodsApi* | [**set_default_payment_method_v1**](docs/BillingPaymentMethodsApi.md#set_default_payment_method_v1) | **POST** /api/billing/v1/payment-methods/{paymentMethodId} | Set default payment method
*BillingSubscriptionsApi* | [**cancel_subscription_v1**](docs/BillingSubscriptionsApi.md#cancel_subscription_v1) | **DELETE** /api/billing/v1/subscriptions/{subscriptionId} | Cancel subscription
*BillingSubscriptionsApi* | [**get_subscription_list_v1**](docs/BillingSubscriptionsApi.md#get_subscription_list_v1) | **GET** /api/billing/v1/subscriptions | Get subscription list
*DNSSnapshotApi* | [**get_snapshot_list_v1**](docs/DNSSnapshotApi.md#get_snapshot_list_v1) | **GET** /api/dns/v1/snapshots/{domain} | Get snapshot list
*DNSSnapshotApi* | [**get_snapshot_v1**](docs/DNSSnapshotApi.md#get_snapshot_v1) | **GET** /api/dns/v1/snapshots/{domain}/{snapshotId} | Get snapshot
*DNSSnapshotApi* | [**restore_snapshot_v1**](docs/DNSSnapshotApi.md#restore_snapshot_v1) | **POST** /api/dns/v1/snapshots/{domain}/{snapshotId}/restore | Restore snapshot
*DNSZoneApi* | [**delete_zone_records_v1**](docs/DNSZoneApi.md#delete_zone_records_v1) | **DELETE** /api/dns/v1/zones/{domain} | Delete zone records
*DNSZoneApi* | [**get_records_v1**](docs/DNSZoneApi.md#get_records_v1) | **GET** /api/dns/v1/zones/{domain} | Get records
*DNSZoneApi* | [**reset_zone_records_v1**](docs/DNSZoneApi.md#reset_zone_records_v1) | **POST** /api/dns/v1/zones/{domain}/reset | Reset zone records
*DNSZoneApi* | [**update_zone_records_v1**](docs/DNSZoneApi.md#update_zone_records_v1) | **PUT** /api/dns/v1/zones/{domain} | Update zone records
*DNSZoneApi* | [**validate_zone_records_v1**](docs/DNSZoneApi.md#validate_zone_records_v1) | **POST** /api/dns/v1/zones/{domain}/validate | Validate zone records
*DomainsAvailabilityApi* | [**check_domain_availability_v1**](docs/DomainsAvailabilityApi.md#check_domain_availability_v1) | **POST** /api/domains/v1/availability | Check domain availability
*DomainsPortfolioApi* | [**get_domain_list_v1**](docs/DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list
*VPSActionsApi* | [**get_action_list_v1**](docs/VPSActionsApi.md#get_action_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions | Get action list
*VPSActionsApi* | [**get_action_v1**](docs/VPSActionsApi.md#get_action_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions/{actionId} | Get action
*VPSBackupsApi* | [**delete_backup_v1**](docs/VPSBackupsApi.md#delete_backup_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId} | Delete backup
*VPSBackupsApi* | [**get_backup_list_v1**](docs/VPSBackupsApi.md#get_backup_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/backups | Get backup list
*VPSBackupsApi* | [**restore_backup_v1**](docs/VPSBackupsApi.md#restore_backup_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId}/restore | Restore backup
*VPSDataCentersApi* | [**get_data_centers_list_v1**](docs/VPSDataCentersApi.md#get_data_centers_list_v1) | **GET** /api/vps/v1/data-centers | Get data centers list
*VPSFirewallApi* | [**activate_firewall_v1**](docs/VPSFirewallApi.md#activate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/activate/{virtualMachineId} | Activate firewall
*VPSFirewallApi* | [**create_firewall_rule_v1**](docs/VPSFirewallApi.md#create_firewall_rule_v1) | **POST** /api/vps/v1/firewall/{firewallId}/rules | Create firewall rule
*VPSFirewallApi* | [**create_new_firewall_v1**](docs/VPSFirewallApi.md#create_new_firewall_v1) | **POST** /api/vps/v1/firewall | Create new firewall
*VPSFirewallApi* | [**deactivate_firewall_v1**](docs/VPSFirewallApi.md#deactivate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/deactivate/{virtualMachineId} | Deactivate firewall
*VPSFirewallApi* | [**delete_firewall_rule_v1**](docs/VPSFirewallApi.md#delete_firewall_rule_v1) | **DELETE** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Delete firewall rule
*VPSFirewallApi* | [**delete_firewall_v1**](docs/VPSFirewallApi.md#delete_firewall_v1) | **DELETE** /api/vps/v1/firewall/{firewallId} | Delete firewall
*VPSFirewallApi* | [**get_firewall_list_v1**](docs/VPSFirewallApi.md#get_firewall_list_v1) | **GET** /api/vps/v1/firewall | Get firewall list
*VPSFirewallApi* | [**get_firewall_v1**](docs/VPSFirewallApi.md#get_firewall_v1) | **GET** /api/vps/v1/firewall/{firewallId} | Get firewall
*VPSFirewallApi* | [**sync_firewall_v1**](docs/VPSFirewallApi.md#sync_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/sync/{virtualMachineId} | Sync firewall
*VPSFirewallApi* | [**update_firewall_rule_v1**](docs/VPSFirewallApi.md#update_firewall_rule_v1) | **PUT** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Update firewall rule
*VPSMalwareScannerApi* | [**get_scan_metrics_v1**](docs/VPSMalwareScannerApi.md#get_scan_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Get scan metrics
*VPSMalwareScannerApi* | [**install_monarx_v1**](docs/VPSMalwareScannerApi.md#install_monarx_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Install Monarx
*VPSMalwareScannerApi* | [**uninstall_monarx_v1**](docs/VPSMalwareScannerApi.md#uninstall_monarx_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Uninstall Monarx
*VPSOSTemplatesApi* | [**get_template_list_v1**](docs/VPSOSTemplatesApi.md#get_template_list_v1) | **GET** /api/vps/v1/templates | Get template list
*VPSOSTemplatesApi* | [**get_template_v1**](docs/VPSOSTemplatesApi.md#get_template_v1) | **GET** /api/vps/v1/templates/{templateId} | Get template
*VPSPTRRecordsApi* | [**create_ptr_record_v1**](docs/VPSPTRRecordsApi.md#create_ptr_record_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr | Create PTR record
*VPSPTRRecordsApi* | [**delete_ptr_record_v1**](docs/VPSPTRRecordsApi.md#delete_ptr_record_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr | Delete PTR record
*VPSPostInstallScriptsApi* | [**create_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#create_post_install_script_v1) | **POST** /api/vps/v1/post-install-scripts | Create post-install script
*VPSPostInstallScriptsApi* | [**delete_a_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#delete_a_post_install_script_v1) | **DELETE** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Delete a post-install script
*VPSPostInstallScriptsApi* | [**get_post_install_script_list_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_script_list_v1) | **GET** /api/vps/v1/post-install-scripts | Get post-install script list
*VPSPostInstallScriptsApi* | [**get_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_script_v1) | **GET** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Get post-install script
*VPSPostInstallScriptsApi* | [**update_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#update_post_install_script_v1) | **PUT** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Update post-install script
*VPSPublicKeysApi* | [**attach_public_key_v1**](docs/VPSPublicKeysApi.md#attach_public_key_v1) | **POST** /api/vps/v1/public-keys/attach/{virtualMachineId} | Attach public key
*VPSPublicKeysApi* | [**create_new_public_key_v1**](docs/VPSPublicKeysApi.md#create_new_public_key_v1) | **POST** /api/vps/v1/public-keys | Create new public key
*VPSPublicKeysApi* | [**delete_a_public_key_v1**](docs/VPSPublicKeysApi.md#delete_a_public_key_v1) | **DELETE** /api/vps/v1/public-keys/{publicKeyId} | Delete a public key
*VPSPublicKeysApi* | [**get_public_key_list_v1**](docs/VPSPublicKeysApi.md#get_public_key_list_v1) | **GET** /api/vps/v1/public-keys | Get public key list
*VPSRecoveryApi* | [**start_recovery_mode_v1**](docs/VPSRecoveryApi.md#start_recovery_mode_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Start recovery mode
*VPSRecoveryApi* | [**stop_recovery_mode_v1**](docs/VPSRecoveryApi.md#stop_recovery_mode_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Stop recovery mode
*VPSSnapshotsApi* | [**create_snapshot_v1**](docs/VPSSnapshotsApi.md#create_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Create snapshot
*VPSSnapshotsApi* | [**delete_snapshot_v1**](docs/VPSSnapshotsApi.md#delete_snapshot_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Delete snapshot
*VPSSnapshotsApi* | [**get_snapshot_v1**](docs/VPSSnapshotsApi.md#get_snapshot_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Get snapshot
*VPSSnapshotsApi* | [**restore_snapshot_v1**](docs/VPSSnapshotsApi.md#restore_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot/restore | Restore snapshot
*VPSVirtualMachineApi* | [**get_attached_public_keys_v1**](docs/VPSVirtualMachineApi.md#get_attached_public_keys_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/public-keys | Get attached public keys
*VPSVirtualMachineApi* | [**get_metrics_v1**](docs/VPSVirtualMachineApi.md#get_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/metrics | Get metrics
*VPSVirtualMachineApi* | [**get_virtual_machine_list_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machine_list_v1) | **GET** /api/vps/v1/virtual-machines | Get virtual machine list
*VPSVirtualMachineApi* | [**get_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machine_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId} | Get virtual machine
*VPSVirtualMachineApi* | [**recreate_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#recreate_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recreate | Recreate virtual machine
*VPSVirtualMachineApi* | [**reset_hostname_v1**](docs/VPSVirtualMachineApi.md#reset_hostname_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Reset hostname
*VPSVirtualMachineApi* | [**restart_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#restart_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/restart | Restart virtual machine
*VPSVirtualMachineApi* | [**set_hostname_v1**](docs/VPSVirtualMachineApi.md#set_hostname_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Set hostname
*VPSVirtualMachineApi* | [**set_nameservers_v1**](docs/VPSVirtualMachineApi.md#set_nameservers_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/nameservers | Set nameservers
*VPSVirtualMachineApi* | [**set_panel_password_v1**](docs/VPSVirtualMachineApi.md#set_panel_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/panel-password | Set panel password
*VPSVirtualMachineApi* | [**set_root_password_v1**](docs/VPSVirtualMachineApi.md#set_root_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/root-password | Set root password
*VPSVirtualMachineApi* | [**setup_new_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#setup_new_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/setup | Setup new virtual machine
*VPSVirtualMachineApi* | [**start_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#start_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/start | Start virtual machine
*VPSVirtualMachineApi* | [**stop_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#stop_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/stop | Stop virtual machine


## Documentation For Models

 - [BillingV1CatalogCatalogItemPriceResource](docs/BillingV1CatalogCatalogItemPriceResource.md)
 - [BillingV1CatalogCatalogItemResource](docs/BillingV1CatalogCatalogItemResource.md)
 - [BillingV1OrderOrderBillingAddressResource](docs/BillingV1OrderOrderBillingAddressResource.md)
 - [BillingV1OrderOrderResource](docs/BillingV1OrderOrderResource.md)
 - [BillingV1OrderStoreRequest](docs/BillingV1OrderStoreRequest.md)
 - [BillingV1OrderStoreRequestItemsInner](docs/BillingV1OrderStoreRequestItemsInner.md)
 - [BillingV1PaymentMethodPaymentMethodResource](docs/BillingV1PaymentMethodPaymentMethodResource.md)
 - [BillingV1SubscriptionCancelRequest](docs/BillingV1SubscriptionCancelRequest.md)
 - [BillingV1SubscriptionSubscriptionResource](docs/BillingV1SubscriptionSubscriptionResource.md)
 - [CommonSchemaErrorResponseSchema](docs/CommonSchemaErrorResponseSchema.md)
 - [CommonSchemaPaginationMetaSchema](docs/CommonSchemaPaginationMetaSchema.md)
 - [CommonSchemaUnauthorizedResponseSchema](docs/CommonSchemaUnauthorizedResponseSchema.md)
 - [CommonSchemaUnprocessableContentResponseSchema](docs/CommonSchemaUnprocessableContentResponseSchema.md)
 - [CommonSchemaUnprocessableContentResponseSchemaErrors](docs/CommonSchemaUnprocessableContentResponseSchemaErrors.md)
 - [CommonSuccessEmptyResource](docs/CommonSuccessEmptyResource.md)
 - [DNSV1SnapshotSnapshotResource](docs/DNSV1SnapshotSnapshotResource.md)
 - [DNSV1SnapshotSnapshotWithContentResource](docs/DNSV1SnapshotSnapshotWithContentResource.md)
 - [DNSV1ZoneDestroyRequest](docs/DNSV1ZoneDestroyRequest.md)
 - [DNSV1ZoneDestroyRequestFiltersInner](docs/DNSV1ZoneDestroyRequestFiltersInner.md)
 - [DNSV1ZoneNameRecordResource](docs/DNSV1ZoneNameRecordResource.md)
 - [DNSV1ZoneRecordResource](docs/DNSV1ZoneRecordResource.md)
 - [DNSV1ZoneResetRequest](docs/DNSV1ZoneResetRequest.md)
 - [DNSV1ZoneUpdateRequest](docs/DNSV1ZoneUpdateRequest.md)
 - [DNSV1ZoneUpdateRequestZoneInner](docs/DNSV1ZoneUpdateRequestZoneInner.md)
 - [DNSV1ZoneUpdateRequestZoneInnerRecordsInner](docs/DNSV1ZoneUpdateRequestZoneInnerRecordsInner.md)
 - [DomainsV1AvailabilityAvailabilityRequest](docs/DomainsV1AvailabilityAvailabilityRequest.md)
 - [DomainsV1AvailabilityAvailabilityResource](docs/DomainsV1AvailabilityAvailabilityResource.md)
 - [DomainsV1DomainDomainResource](docs/DomainsV1DomainDomainResource.md)
 - [VPSGetActionListV1200Response](docs/VPSGetActionListV1200Response.md)
 - [VPSGetBackupListV1200Response](docs/VPSGetBackupListV1200Response.md)
 - [VPSGetFirewallListV1200Response](docs/VPSGetFirewallListV1200Response.md)
 - [VPSGetPostInstallScriptListV1200Response](docs/VPSGetPostInstallScriptListV1200Response.md)
 - [VPSGetPublicKeyListV1200Response](docs/VPSGetPublicKeyListV1200Response.md)
 - [VPSV1ActionActionResource](docs/VPSV1ActionActionResource.md)
 - [VPSV1BackupBackupResource](docs/VPSV1BackupBackupResource.md)
 - [VPSV1DataCenterDataCenterResource](docs/VPSV1DataCenterDataCenterResource.md)
 - [VPSV1FirewallFirewallResource](docs/VPSV1FirewallFirewallResource.md)
 - [VPSV1FirewallFirewallRuleResource](docs/VPSV1FirewallFirewallRuleResource.md)
 - [VPSV1FirewallRulesStoreRequest](docs/VPSV1FirewallRulesStoreRequest.md)
 - [VPSV1FirewallStoreRequest](docs/VPSV1FirewallStoreRequest.md)
 - [VPSV1IPAddressIPAddressResource](docs/VPSV1IPAddressIPAddressResource.md)
 - [VPSV1MalwareMetricsResource](docs/VPSV1MalwareMetricsResource.md)
 - [VPSV1MetricsMetricsCollection](docs/VPSV1MetricsMetricsCollection.md)
 - [VPSV1MetricsMetricsCollectionCpuUsage](docs/VPSV1MetricsMetricsCollectionCpuUsage.md)
 - [VPSV1MetricsMetricsCollectionDiskSpace](docs/VPSV1MetricsMetricsCollectionDiskSpace.md)
 - [VPSV1MetricsMetricsCollectionIncomingTraffic](docs/VPSV1MetricsMetricsCollectionIncomingTraffic.md)
 - [VPSV1MetricsMetricsCollectionOutgoingTraffic](docs/VPSV1MetricsMetricsCollectionOutgoingTraffic.md)
 - [VPSV1MetricsMetricsCollectionRamUsage](docs/VPSV1MetricsMetricsCollectionRamUsage.md)
 - [VPSV1MetricsMetricsCollectionUptime](docs/VPSV1MetricsMetricsCollectionUptime.md)
 - [VPSV1MetricsMetricsResource](docs/VPSV1MetricsMetricsResource.md)
 - [VPSV1PostInstallScriptPostInstallScriptResource](docs/VPSV1PostInstallScriptPostInstallScriptResource.md)
 - [VPSV1PostInstallScriptStoreRequest](docs/VPSV1PostInstallScriptStoreRequest.md)
 - [VPSV1PublicKeyAttachRequest](docs/VPSV1PublicKeyAttachRequest.md)
 - [VPSV1PublicKeyPublicKeyResource](docs/VPSV1PublicKeyPublicKeyResource.md)
 - [VPSV1PublicKeyStoreRequest](docs/VPSV1PublicKeyStoreRequest.md)
 - [VPSV1SnapshotSnapshotResource](docs/VPSV1SnapshotSnapshotResource.md)
 - [VPSV1TemplateTemplateResource](docs/VPSV1TemplateTemplateResource.md)
 - [VPSV1VirtualMachineHostnameUpdateRequest](docs/VPSV1VirtualMachineHostnameUpdateRequest.md)
 - [VPSV1VirtualMachineNameserversUpdateRequest](docs/VPSV1VirtualMachineNameserversUpdateRequest.md)
 - [VPSV1VirtualMachinePanelPasswordUpdateRequest](docs/VPSV1VirtualMachinePanelPasswordUpdateRequest.md)
 - [VPSV1VirtualMachineRecoveryStartRequest](docs/VPSV1VirtualMachineRecoveryStartRequest.md)
 - [VPSV1VirtualMachineRecreateRequest](docs/VPSV1VirtualMachineRecreateRequest.md)
 - [VPSV1VirtualMachineRootPasswordUpdateRequest](docs/VPSV1VirtualMachineRootPasswordUpdateRequest.md)
 - [VPSV1VirtualMachineSetupRequest](docs/VPSV1VirtualMachineSetupRequest.md)
 - [VPSV1VirtualMachineSetupRequestPublicKey](docs/VPSV1VirtualMachineSetupRequestPublicKey.md)
 - [VPSV1VirtualMachineVirtualMachineResource](docs/VPSV1VirtualMachineVirtualMachineResource.md)
 - [VPSV1VirtualMachineVirtualMachineResourceIpv4](docs/VPSV1VirtualMachineVirtualMachineResourceIpv4.md)
 - [VPSV1VirtualMachineVirtualMachineResourceIpv6](docs/VPSV1VirtualMachineVirtualMachineResourceIpv6.md)
 - [VPSV1VirtualMachineVirtualMachineResourceTemplate](docs/VPSV1VirtualMachineVirtualMachineResourceTemplate.md)


