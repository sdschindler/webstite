#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:51:38 2023

@author: stevenschindler
"""

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)