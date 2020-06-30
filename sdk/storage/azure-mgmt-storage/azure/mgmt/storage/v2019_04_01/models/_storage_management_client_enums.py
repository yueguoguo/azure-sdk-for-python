# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AccessTier(str, Enum):
    """Required for storage accounts where kind = BlobStorage. The access tier used for billing.
    """

    hot = "Hot"
    cool = "Cool"

class AccountStatus(str, Enum):
    """Gets the status indicating whether the primary location of the storage account is available or
    unavailable.
    """

    available = "available"
    unavailable = "unavailable"

class Bypass(str, Enum):
    """Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are
    any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to
    bypass none of those traffics.
    """

    none = "None"
    logging = "Logging"
    metrics = "Metrics"
    azure_services = "AzureServices"

class CorsRuleAllowedMethodsItem(str, Enum):

    delete = "DELETE"
    get = "GET"
    head = "HEAD"
    merge = "MERGE"
    post = "POST"
    options = "OPTIONS"
    put = "PUT"

class DefaultAction(str, Enum):
    """Specifies the default action of allow or deny when no other rules match.
    """

    allow = "Allow"
    deny = "Deny"

class DirectoryServiceOptions(str, Enum):
    """Indicates the directory service used.
    """

    none = "None"
    aadds = "AADDS"
    ad = "AD"

class GeoReplicationStatus(str, Enum):
    """The status of the secondary location. Possible values are: - Live: Indicates that the secondary
    location is active and operational. - Bootstrap: Indicates initial synchronization from the
    primary location to the secondary location is in progress.This typically occurs when
    replication is first enabled. - Unavailable: Indicates that the secondary location is
    temporarily unavailable.
    """

    live = "Live"
    bootstrap = "Bootstrap"
    unavailable = "Unavailable"

class HttpProtocol(str, Enum):
    """The protocol permitted for a request made with the account SAS.
    """

    https_http = "https,http"
    https = "https"

class ImmutabilityPolicyState(str, Enum):
    """The ImmutabilityPolicy state of a blob container, possible values include: Locked and Unlocked.
    """

    locked = "Locked"
    unlocked = "Unlocked"

class ImmutabilityPolicyUpdateType(str, Enum):
    """The ImmutabilityPolicy update type of a blob container, possible values include: put, lock and
    extend.
    """

    put = "put"
    lock = "lock"
    extend = "extend"

class KeyPermission(str, Enum):
    """Permissions for the key -- read-only or full permissions.
    """

    read = "Read"
    full = "Full"

class KeySource(str, Enum):
    """The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage,
    Microsoft.Keyvault
    """

    microsoft_storage = "Microsoft.Storage"
    microsoft_keyvault = "Microsoft.Keyvault"

class Kind(str, Enum):
    """Indicates the type of storage account.
    """

    storage = "Storage"
    storage_v2 = "StorageV2"
    blob_storage = "BlobStorage"
    file_storage = "FileStorage"
    block_blob_storage = "BlockBlobStorage"

class LargeFileSharesState(str, Enum):
    """Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled.
    """

    disabled = "Disabled"
    enabled = "Enabled"

class LeaseContainerRequestAction(str, Enum):
    """Specifies the lease action. Can be one of the available actions.
    """

    acquire = "Acquire"
    renew = "Renew"
    change = "Change"
    release = "Release"
    break_enum = "Break"

class LeaseDuration(str, Enum):
    """Specifies whether the lease on a container is of infinite or fixed duration, only when the
    container is leased.
    """

    infinite = "Infinite"
    fixed = "Fixed"

class LeaseState(str, Enum):
    """Lease state of the container.
    """

    available = "Available"
    leased = "Leased"
    expired = "Expired"
    breaking = "Breaking"
    broken = "Broken"

class LeaseStatus(str, Enum):
    """The lease status of the container.
    """

    locked = "Locked"
    unlocked = "Unlocked"

class MinimumTlsVersion(str, Enum):
    """Set the minimum TLS version to be permitted on requests to storage. The default interpretation
    is TLS 1.0 for this property.
    """

    tls1_0 = "TLS1_0"
    tls1_1 = "TLS1_1"
    tls1_2 = "TLS1_2"

class Permissions(str, Enum):
    """The signed permissions for the account SAS. Possible values include: Read (r), Write (w),
    Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p).
    """

    r = "r"
    d = "d"
    w = "w"
    l = "l"
    a = "a"
    c = "c"
    u = "u"
    p = "p"

class ProvisioningState(str, Enum):
    """Gets the status of the storage account at the time the operation was called.
    """

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"

class PublicAccess(str, Enum):
    """Specifies whether data in the container may be accessed publicly and the level of access.
    """

    container = "Container"
    blob = "Blob"
    none = "None"

class Reason(str, Enum):
    """Gets the reason that a storage account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"

class ReasonCode(str, Enum):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". Quota Id is set when the SKU has requiredQuotas parameter as the
    subscription does not belong to that quota. The "NotAvailableForSubscription" is related to
    capacity at DC.
    """

    quota_id = "QuotaId"
    not_available_for_subscription = "NotAvailableForSubscription"

class Services(str, Enum):
    """The signed services accessible with the account SAS. Possible values include: Blob (b), Queue
    (q), Table (t), File (f).
    """

    b = "b"
    q = "q"
    t = "t"
    f = "f"

class SignedResource(str, Enum):
    """The signed services accessible with the service SAS. Possible values include: Blob (b),
    Container (c), File (f), Share (s).
    """

    b = "b"
    c = "c"
    f = "f"
    s = "s"

class SignedResourceTypes(str, Enum):
    """The signed resource types that are accessible with the account SAS. Service (s): Access to
    service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to
    object-level APIs for blobs, queue messages, table entities, and files.
    """

    s = "s"
    c = "c"
    o = "o"

class SkuName(str, Enum):
    """Gets or sets the SKU name. Required for account creation; optional for update. Note that in
    older versions, SKU name was called accountType.
    """

    standard_lrs = "Standard_LRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"
    premium_zrs = "Premium_ZRS"
    standard_gzrs = "Standard_GZRS"
    standard_ragzrs = "Standard_RAGZRS"

class SkuTier(str, Enum):
    """Gets the SKU tier. This is based on the SKU name.
    """

    standard = "Standard"
    premium = "Premium"

class State(str, Enum):
    """Gets the state of virtual network rule.
    """

    provisioning = "provisioning"
    deprovisioning = "deprovisioning"
    succeeded = "succeeded"
    failed = "failed"
    network_source_deleted = "networkSourceDeleted"

class UsageUnit(str, Enum):
    """Gets the unit of measurement.
    """

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    counts_per_second = "CountsPerSecond"
    bytes_per_second = "BytesPerSecond"
