# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

# version_info format: (MAJOR, MINOR, MICRO, RELEASE_LEVEL, SERIAL)
# inspired by Python's own sys.version_info, in order to be
# properly comparable using normal operators, for example:
#  (6,1,0,'beta',0) < (6,1,0,'candidate',1) < (6,1,0,'candidate',2)
#  (6,1,0,'candidate',2) < (6,1,0,'final',0) < (6,1,2,'final',0)
version_info = (18, 0, 0, FINAL, 0, '')
version = '.'.join(str(s) for s in version_info[:2]) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '') + version_info[5]
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])

product_name = 'Odoo'
description = 'Odoo Server'
long_desc = '''Odoo is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, an object database, a dynamic GUI,
customizable reports, and XML-RPC interfaces.
'''
classifiers = """Development Status :: 5 - Production/Stable
License :: OSI Approved :: GNU Lesser General Public License v3

Programming Language :: Python
"""
url = 'https://www.odoo.com'
author = 'OpenERP S.A.'
author_email = 'info@odoo.com'
license = 'LGPL-3'

nt_service_name = "odoo-server-" + series.replace('~','-')

version += '-20250503'

repos_heads = {'odoo': '14b53e0ef7738bfe0681ebf4f5eaedadf18bf9e8', 'enterprise': '43c9979d02dc8e2c0138ad162c87baaf4c06cd9b', 'design-themes': 'a0b6a5b4103f169715c545783bd4aa2f8d3686df'}
