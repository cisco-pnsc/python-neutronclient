# Copyright 2013 Mirantis Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Ilya Shakhat, Mirantis Inc.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import logging

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListSslTrustedCertificate(neutronV20.ListCommand):
    """List SSL Trusted Certificates that belong to a given tenant."""

    resource = 'ssl_trusted_certificate'
    log = logging.getLogger(__name__ + '.ListSslTrustedCertificate')
    list_columns = ['id', 'name', 'tenant_id', 'certificate', 'vips']
    pagination_support = True
    sorting_support = True


class ShowSslTrustedCertificate(neutronV20.ShowCommand):
    """Show information of a given SSL Certificate."""

    resource = 'ssl_trusted_certificate'
    log = logging.getLogger(__name__ + '.ShowSslTrustedCertificate')


class CreateSslTrustedCertificate(neutronV20.CreateCommand):
    """Create a SSL Trusted Certificate."""

    resource = 'ssl_trusted_certificate'
    log = logging.getLogger(__name__ + '.CreateSslTrustedCertificate')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            required=True,
            help=_('Name of the certificate'))
        parser.add_argument(
            '--certificate',
            required=True,
            help=_('Certificate content'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                  ['name', 'certificate', 'tenant_id'])
        return body


class UpdateSslTrustedCertificate(neutronV20.UpdateCommand):
    """Update a given SSL Trusted Certificate."""

    resource = 'ssl_trusted_certificate'
    log = logging.getLogger(__name__ + '.UpdateSslTrustedCertificate')


class DeleteSslTrustedCertificate(neutronV20.DeleteCommand):
    """Delete a given SSL Trusted Certificate."""

    resource = 'ssl_trusted_certificate'
    log = logging.getLogger(__name__ + '.DeleteSslTrustedCertificate')
