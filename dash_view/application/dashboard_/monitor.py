from common.utilities.util_menu_access import MenuAccess
import feffery_utils_components as fuc
import feffery_antd_components as fac
from common.utilities.util_logger import Log
from dash import html, dcc
from dash_components import Card
import dash_callback.application.dashboard_.monitor_c  # noqa
from functools import partial
from i18n import translator

_ = partial(translator.t)


# 二级菜单的标题、图标和显示顺序
title = '监控页'
icon = None
order = 2
logger = Log.get_logger(__name__)

access_metas = ('监控页-页面',)


def render_content(menu_access: MenuAccess, **kwargs):
    return html.Div(
        [
            dcc.Interval(id='monitor-intervals', interval=5000),
            fuc.FefferyTimeout(id='monitor-intervals-init', delay=0),
            fac.AntdFlex(
                [
                    Card(
                        fac.AntdDescriptions(
                            id='monitor-sys-desc',
                            items=[],
                            labelStyle={'fontWeight': 'bold'},
                            bordered=True,
                            layout='vertical',
                            column=2,
                        ),
                        title=_('系统信息'),
                    ),
                    Card(
                        fac.AntdDescriptions(
                            id='monitor-process-desc',
                            items=[],
                            labelStyle={'fontWeight': 'bold'},
                            bordered=True,
                            layout='vertical',
                            column=2,
                        ),
                        title=_('进程运行状态'),
                    ),
                    Card(
                        fac.AntdTable(
                            id='monitor-disk-desc',
                            columns=[
                                {'title': _('设备名'), 'dataIndex': 'dir_name'},
                                {'title': _('文件系统类型'), 'dataIndex': 'sys_type_name'},
                                {'title': _('总容量'), 'dataIndex': 'total'},
                                {'title': _('已用'), 'dataIndex': 'used'},
                                {'title': _('可用'), 'dataIndex': 'free'},
                                {'title': _('使用率'), 'dataIndex': 'usage'},
                                {'title': _('挂载点'), 'dataIndex': 'type_name'},
                            ],
                            data=[],
                            bordered=True,
                            pagination=False,
                        ),
                        title=_('磁盘状态'),
                    ),
                    Card(
                        fac.AntdDescriptions(
                            id='monitor-cpu-load-desc',
                            items=[],
                            labelStyle={'fontWeight': 'bold'},
                            bordered=True,
                            layout='vertical',
                            column=3,
                        ),
                        title='CPU',
                    ),
                    Card(
                        fac.AntdDescriptions(
                            id='monitor-mem-load-desc',
                            items=[],
                            labelStyle={'fontWeight': 'bold'},
                            bordered=True,
                            layout='vertical',
                            column=2,
                        ),
                        title=_('内存'),
                    ),
                ],
                gap='small',
                wrap='wrap',
            ),
        ]
    )
