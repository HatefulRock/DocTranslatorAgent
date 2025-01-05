# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : vo.py
# Time       ：2025/1/1 14:31
# Author     ：vince
# Description：
"""
from typing import List, Optional

from pydantic import BaseModel


class TextBlock(BaseModel):
    x0: int
    y0: int
    six_y0: int = None
    x1: int
    y1: int
    six_y1: int = None
    type: str
    text: Optional[str] = ''
    font_size: Optional[float] = None
    is_bold: Optional[bool] = None

class ReaderResult(BaseModel):
    page_no: int
    text_blocks: List[TextBlock]

class TranslateRequest(BaseModel):
    texts: List[str]
    source_lang: str
    target_lang: str
    translator: str

class TranslateResult(BaseModel):
    index: int
    result: str