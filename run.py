import json
import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask_mail import Mail, Message
from task import *
from celery import Celery


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'top-secret!'

    # Flask-Mail configuration
    app.config['MAIL_DEBUG'] = True  # 开启debug，便于调试看信息
    app.config['MAIL_SUPPRESS_SEND'] = False  # 发送邮件，为True则不发送
    app.config['MAIL_SERVER'] = 'smtp.163.com'  # 邮箱服务器
    app.config['MAIL_PORT'] = 465  # 端口
    app.config['MAIL_USE_SSL'] = True  # 重要，qq邮箱需要使用SSL
    app.config['MAIL_USE_TLS'] = False  # 不需要使用TLS
    app.config['MAIL_USERNAME'] = '13135673615@163.com'  # 填邮箱
    app.config['MAIL_PASSWORD'] = 'zz1313'  # 填授权码
    app.config['MAIL_DEFAULT_SENDER'] = '13135673615@163.com'  # 填邮箱，默认发送者

    # Celery configuration
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

    # Initialize extensions


    return app