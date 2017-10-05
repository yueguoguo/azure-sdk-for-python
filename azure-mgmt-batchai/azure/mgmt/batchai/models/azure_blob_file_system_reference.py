# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureBlobFileSystemReference(Model):
    """Details of the Azure Blob Storage container to mount on the cluster.

    :param account_name: Name of the Azure Blob Storage account.
    :type account_name: str
    :param container_name: Name of the Azure Blob Storage container to mount
     on the cluster.
    :type container_name: str
    :param credentials: Information of the Azure Blob Storage account
     credentials.
    :type credentials: :class:`AzureStorageCredentialsInfo
     <azure.mgmt.batchai.models.AzureStorageCredentialsInfo>`
    :param relative_mount_path: Specifies the relative path on the compute
     node where the Azure Blob file system will be mounted. Note that all blob
     file systems will be mounted under $AZ_BATCHAI_MOUNT_ROOT location.
    :type relative_mount_path: str
    :param mount_options: Specifies the various mount options that can be used
     to configure Blob file system.
    :type mount_options: str
    """

    _validation = {
        'account_name': {'required': True},
        'container_name': {'required': True},
        'credentials': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'AzureStorageCredentialsInfo'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
        'mount_options': {'key': 'mountOptions', 'type': 'str'},
    }

    def __init__(self, account_name, container_name, credentials, relative_mount_path, mount_options=None):
        self.account_name = account_name
        self.container_name = container_name
        self.credentials = credentials
        self.relative_mount_path = relative_mount_path
        self.mount_options = mount_options
