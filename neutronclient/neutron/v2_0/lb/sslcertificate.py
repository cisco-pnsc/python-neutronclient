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


class ListSslCertificate(neutronV20.ListCommand):
    """List SSL Certificates that belong to a given tenant."""

    resource = 'ssl_certificate'
    log = logging.getLogger(__name__ + '.ListSslCertificate')
    list_columns = ['id', 'tenant_id', 'name', 'certificate', 'passphrase', 'certificate_chain']
    pagination_support = True
    sorting_support = True


class ShowSslCertificate(neutronV20.ShowCommand):
    """Show information of a given SSL Certificate."""

    resource = 'ssl_certificate'
    log = logging.getLogger(__name__ + '.ShowSslCertificate')


class CreateSslCertificate(neutronV20.CreateCommand):
    """Create a SSL Certificate."""

    resource = 'ssl_certificate'
    log = logging.getLogger(__name__ + '.CreateSslCertificate')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            required=True,
            help=_('Name of the certificate'))
        parser.add_argument(
            '--certificate',
            required=True,
            help=_('Certificate content'))
        parser.add_argument(
            '--passphrase',
            help=_('Passphrase used to encrypt the private key'))
        parser.add_argument(
            '--certificate_chain',
            help=_('Chain of the issuer\'s certificates'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                  ['name', 'certificate', 'passphrase', 'certificate_chain', 'tenant_id'])
        return body


class UpdateSslCertificate(neutronV20.UpdateCommand):
    """Update a given SSL Certificate."""

    resource = 'ssl_certificate'
    log = logging.getLogger(__name__ + '.UpdateSslCertificate')


class DeleteSslCertificate(neutronV20.DeleteCommand):
    """Delete a given SSL Certificate."""

    resource = 'ssl_certificate'
    log = logging.getLogger(__name__ + '.DeleteSslCertificate')
