from common.utilities.util_menu_access import MenuAccess
from typing import List
import feffery_antd_components as fac
from common.utilities.util_logger import Log
from dash import html
from flask_babel import gettext as _  # noqa


# 二级菜单的标题、图标和显示顺序
def get_title():
    return _('监控页')


icon = None
order = 2
logger = Log.get_logger(__name__)


def render_content(menu_access: MenuAccess, **kwargs):
    access_metas: List[str] = menu_access.get_access_metas(__name__)
    if 'show' not in access_metas:
        return '您没有权限显示该页面'
    return html.Iframe(
        style={
            'width': '100%',
            'height': '100%',
            'borderStyle': 'none',
        },
        src='https://fac.feffery.tech/',
    )