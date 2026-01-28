# -*- coding: utf-8 -*-
{
    'name': "Chấm công",

    'summary': "Quản lý chấm công, ca làm, đơn từ và dashboard.",

    'description': """Quản lý chấm công theo ngày/ca, đơn xin nghỉ/đi muộn/về sớm và dashboard tổng hợp.""",

    'author': "",
    'website': "",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    'application': True,
    'installable': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'nhan_su'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/nhan_vien_ext.xml',
        'views/tao_bang_cham_cong_wizard.xml',
        'views/dang_ky_ca_lam_theo_ngay.xml',
        'views/bang_cham_cong.xml',
        'views/dot_dang_ky.xml',
        'views/don_tu.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}