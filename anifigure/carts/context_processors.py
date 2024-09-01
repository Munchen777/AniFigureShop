from .cart import _Cart


def cart(request):
    return {"cart": _Cart(request)}
