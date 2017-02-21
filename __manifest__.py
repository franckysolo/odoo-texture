# -*- encoding: utf-8 -*-
##############################################################################
#
#    Aquilog - Open Source Solutions
#    Copyright (C) 2005 - 2016 Aquilog <http://www.aquilog.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################


{
    'name': "Website Sale Custom",
    'version': "1.0",
    'author': "Aquilog",
    'website': 'http://www.aquilog.fr',
    'category': "Theme",
    'depends': ['web', 'website', 'website_sale'],
    'init_xml': [],
    'demo_xml': [],
    'description': """
Custom interface for website sales
""",
    'data': [
        'security/ir.model.access.csv',
        'views/layout.xml',
        'views/pages.xml',
        'data.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
