from flask import Blueprint

cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/')
def lista_clientes():
    pass