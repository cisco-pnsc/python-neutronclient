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

class ShowSslAssociation(neutronV20.ShowCommand):

    """Show information of a given healthmonitor."""

    resource = 'ssl_association'
    log = logging.getLogger(__name__ + '.ShowSslAssociation')



class AssociateSslPolicy(neutronV20.NeutronCommand):
    """Associate SSL policy with a VIP"""

    log = logging.getLogger(__name__ + '.AssociateSslPolicy')
    resource = 'ssl_association'

    def get_parser(self, prog_name):
        parser = super(AssociateSslPolicy, self).get_parser(prog_name)

        parser.add_argument(
            'vip_id', metavar='VIP',
            help=_('Id of VIP'))

        parser.add_argument(
            'ssl_policy_id', metavar='SSL_POLICY_ID',
            help=_('SSL Policy to associate'))

        parser.add_argument(
            '--ssl_trusted_certificate_id',
            help=_('SSL Trusted Certificate to associate'))

        parser.add_argument(
            '--ssl_certificate_id',
            help=_('SSL certificate to associate'))

        parser.add_argument(
            '--private_key',
            help=_('Private key for the SSL certificate'))
        return parser

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = {'ssl_association': {
            'id': parsed_args.vip_id,
            'ssl_policy':{'id':parsed_args.ssl_policy_id},
            'ssl_certificates': [],
            'ssl_trusted_certificates':[],
            }}
        if parsed_args.ssl_certificate_id:
            body[self.resource]['ssl_certificates'].append(
                {'id':parsed_args.ssl_certificate_id,
                 'private_key': parsed_args.private_key
                })

        if parsed_args.ssl_trusted_certificate_id:
            body[self.resource]['ssl_trusted_certificates'].append(
                {'id':parsed_args.ssl_trusted_certificate_id })

        neutronV20.update_dict(parsed_args, body[self.resource],
                              ['tenant_id'])

        vip_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'vip', parsed_args.vip_id)
        neutron_client.create_ssl_policy_association(vip_id, body)


class DisassociateSslPolicy(neutronV20.NeutronCommand):
    """Remove a mapping from a health monitor to a pool."""

    log = logging.getLogger(__name__ + '.DisassociateSslPolicy')
    resource = 'ssl_association'

    def get_parser(self, prog_name):
        parser = super(DisassociateSslPolicy, self).get_parser(prog_name)
        parser.add_argument(
            'vip_id', metavar='VIP_ID',
            help=_('ID of the VIP to be disassociated with the SSL Policy'))
        parser.add_argument(
            'ssl_policy_id', metavar='SSL_POLICY_ID',
            help=_('SSL Policy to associate'))
        return parser

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format

        vip_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'vip', parsed_args.vip_id)

        ssl_policy_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'ssl_policy', parsed_args.ssl_policy_id)

        neutron_client.delete_ssl_policy_association(vip_id, ssl_policy_id)

