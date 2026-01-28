# -*- coding: utf-8 -*-
{
    'name': "Tính lương",

    'summary': "Tự động tính phiếu lương dựa trên dữ liệu chấm công.",

    'description': """Tạo phiếu lương theo tháng/năm, tự tổng hợp giờ công, phạt đi muộn và dashboard lương.""",

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
        'nhan_su',
        'cham_cong',
        'mail',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_phieu_luong.xml',
        'views/nhan_vien_ext.xml',
        'views/tao_phieu_luong_wizard.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}