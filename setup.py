#!/usr/bin/env python
from setuptools import setup

APP = ['correct_korean.py']  # 변환할 스크립트
OPTIONS = {
    'argv_emulation': True, 
    'plist': {
        'LSBackgroundOnly': True,  # 백그라운드 전용 (창 없이 실행)
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)