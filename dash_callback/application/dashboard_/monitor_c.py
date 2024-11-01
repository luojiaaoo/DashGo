from server import app
from dash.dependencies import Input, Output, State
from common.utilities import util_sys
import feffery_antd_components as fac
from dash import html
from flask_babel import gettext as _  # noqa


@app.callback(
    [
        Output('monitor-sys-desc', 'items'),
        Output('monitor-cpu-load-desc', 'items'),
        Output('monitor-mem-load-desc', 'items'),
    ],
    [
        Input('monitor-intervals', 'n_intervals'),
        Input('monitor-intervals-init', 'timeoutCount'),
    ],
)
def callback_func(n_intervals, timeoutCount):
    sys_info = util_sys.get_sys_info()
    return [
        [
            {'label': fac.AntdText(_('域名')), 'children': sys_info['hostname']},
            {'label': fac.AntdText(_('系统类型')), 'children': sys_info['os_name']},
            {'label': fac.AntdText(_('计算机名')), 'children': sys_info['computer_name']},
            {'label': fac.AntdText(_('核心架构')), 'children': sys_info['os_arch']},
        ],
        [
            {'label': fac.AntdText(_('型号')), 'children': sys_info['cpu_name']},
            {'label': fac.AntdText(_('逻辑核数')), 'children': sys_info['cpu_num']},
            {'label': fac.AntdText(_('空闲率')), 'children': f"{sys_info['cpu_free_percent']*100}%"},
            {'label': fac.AntdText(_('总使用率')), 'children': f"{sys_info['cpu_user_usage_percent']*100}%"},
            {'label': fac.AntdText(_('用户使用率')), 'children': f"{sys_info['cpu_user_usage_percent']*100}%"},
            {'label': fac.AntdText(_('系统使用率')), 'children': f"{sys_info['cpu_user_usage_percent']*100}%"},
        ],
        [
            {'label': fac.AntdText(_('总量')), 'children': sys_info['memory_total']},
            {'label': fac.AntdText(_('已用')), 'children': sys_info['memory_used']},
            {'label': fac.AntdText(_('剩余')), 'children': sys_info['memory_free']},
            {'label': fac.AntdText(_('使用率')), 'children': f"{sys_info['memory_usage_percent']*100}%"},
        ],
    ]
