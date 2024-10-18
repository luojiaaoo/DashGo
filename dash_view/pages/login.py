import feffery_utils_components as fuc
import feffery_antd_components as fac
from config.dash_melon_conf import ShowConf


def render_content():
    return fuc.FefferyDiv(
        children=[
            fuc.FefferyDiv(
                children=[
                    fuc.FefferyDiv(
                        children=ShowConf.SYSTEM_NAME,
                        className={
                            'letter-spacing': '2px',
                            'font-family': "'Microsoft YaHei', sans-serif",
                            'font-size': '30px',
                            'height': '15%',
                            'display': 'flex',
                            'justify-content': 'center',
                            'align-items': 'center',
                            'color': 'rgb(245,245,245)'
                        },
                    ),
                    fac.AntdTabs(
                        items=[
                            {
                                'key': '账号密码登录',
                                'label': fac.AntdText(
                                    '账号密码登录',
                                    className={
                                        'letter-spacing': '2px',
                                        'font-family': "'Microsoft YaHei', sans-serif",
                                        'font-size': '24px',
                                        'color': 'rgb(22,119,255)',
                                    },
                                ),
                                'children': [
                                    fac.AntdSpace(
                                        [
                                            fac.AntdInput(
                                                prefix=fac.AntdIcon(icon='antd-user'),
                                                placeholder='请输入用户名',
                                                className={
                                                    'margin-top': '20px',
                                                    'letter-spacing': '2px',
                                                    'font-family': "'Microsoft YaHei', sans-serif",
                                                    'font-size': '24px',
                                                },
                                            ),
                                            fac.AntdInput(
                                                prefix=fac.AntdIcon(icon='antd-lock'),
                                                mode='password',
                                                placeholder='请输入密码',
                                                className={
                                                    'margin-top': '20px',
                                                    'letter-spacing': '2px',
                                                    'font-family': "'Microsoft YaHei', sans-serif",
                                                    'font-size': '24px',
                                                },
                                            ),
                                            fac.AntdFlex(
                                                [
                                                    fac.AntdInput(
                                                        prefix=fac.AntdIcon(icon='antd-right'),
                                                        allowClear=True,
                                                        className={
                                                            'letter-spacing': '2px',
                                                            'font-family': "'Microsoft YaHei', sans-serif",
                                                            'font-size': '24px',
                                                            'width': '100%',
                                                            'margin-right': '20px',
                                                        },
                                                    ),
                                                    fuc.FefferyCaptcha(width=150),
                                                ],
                                                className={
                                                    'margin-top': '20px',
                                                },
                                            ),
                                        ],
                                        direction='vertical',
                                        className={
                                            'width': '100%',
                                        },
                                    )
                                ],
                            },
                        ],
                        className={
                            'height': '85%',
                            'width': '90%',
                        },
                    ),
                ],
                className={
                    'width': 'max(25%,600px)',
                    'height': 'max(35%,700px)',
                    'margin-right': '10%',
                    'backdrop-filter': 'blur(10px)',
                    'background-color': 'rgba(0, 0, 0, 0.15)',
                    'border-radius': '5px',
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                    'box-shadow': '0 10px 20px rgba(0, 0, 0, 0.3)',
                    'border': '1px solid rgba(255, 255, 255, 0.3)',
                    'animation': 'float 2s ease-in-out infinite',
                },
            ),
        ],
        className={
            'display': 'flex',
            'background-image': 'url("/assets/imgs/login_background.jpeg")',
            'background-size': 'cover',
            'background-position': 'center center',
            'background-attachment': 'fixed',
            'background-repeat': 'no-repeat',
            'width': '100vw',
            'height': '100vh',
            'justify-content': 'flex-end',
            'align-items': 'center',
        },
    )
