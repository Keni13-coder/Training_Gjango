from .utils import CrudOrder, CrudProduct, CrudUser, function_handler



def user_point(request, method: str):
    user = CrudUser()
    user_dict = {'name': 'Alex', 'email': 'alex@inbox.com', 'phone_number': '+64739173647', 'address':'кукуего'}
    return function_handler(method=method, model=user, data=user_dict)
            

def prod_point(request, method: str):
    product = CrudProduct()
    product_dict = {'title':'typewriter', 'description': 'color red, 10x15', 'price':15.0, 'count': 4}
    return function_handler(method=method, model=product, data=product_dict)



def order_point(request, method: str):
    order = CrudOrder()
    order_dict= {'user_id': 1, 'total_cost':30.0}
    # не стал уже еще больше заводиться по поводу добавление Many To Many. Есть статичное добавление [1,2] в классе CrudOrder
    return function_handler(method=method, model=order, data=order_dict)
