#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:54:51 2023

@author: stevenschindler
"""
from flask import Blueprint, render_template

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template("home.html")

