from flask import Blueprint
from app import APPNAME

main = Blueprint('main', __name__)

from . import views


################
# Injectare obiecte
################
@main.context_processor
def inject_permissions():
    return dict(APPNAME = APPNAME)