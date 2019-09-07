from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from django.http import HttpResponse
import json
# Create your views here.


def index(request):

    params ={}
    products = Product.objects.all()
    print(products)
    allprods =[]



    category_of_products = Product.objects.values('product_category')   # it will give category of products in object form {product_category:instrument} }
    print(category_of_products)

    category = {item['product_category']  for item in category_of_products}  # from here we will story all categories in list
    print(category)

    for cat in category:
        prod=Product.objects.filter(product_category=cat)    # category wise product will get store in prod

        print(prod)
        n = len(prod)
        slides = 0
        if (n / 4 != 0):
            slides = n // 4 + 1
            print(slides)

        if (n / 4 == 0):
            slides = n // 4
            print(slides)

        allprods.append([prod,range(0,slides),slides])   # list of list will be formed




    params ={ 'allprods':allprods }



    return render(request,"shop/index.html",params)


def about(request):
    return render(request,"shop/about.html")


def products(request,myid):

    product= Product.objects.filter(id=myid)

    params ={'product':product[0]}      # since there is only one product

    return render(request,"shop/products.html",params)



def contactResponse(request):
    return render(request,'shop/contactSubmitResponse.html')

def contactUs(request):

    if request.method=="POST":
        name= request.POST.get('name','')
        email = request.POST.get('email', '')
        feedback = request.POST.get('feedback','')
        phone = request.POST.get('phone', '')

        contact =Contact(name=name,email=email,suggestion=feedback,phone_no=phone)

        contact.save()

        return render(request,'shop/contactSubmitResponse.html')

    else:

     return render(request,'shop/contactPage.html')




def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip=zip, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")  # storing the id in the updateorder model
        update.save()
        #thank = True
        id = order.order_id
        return render(request, 'shop/orderIdShow.html', {'id': id})
    else:

     return render(request, 'shop/checkoutPage.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        '''try:
            order = Orders.objects.filter(order_id=orderId, email=email)  # checking weather any order of the given orderId is present in the Order database
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId) # all the orderupdate will get store in update
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)

                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
       '''
        order = Orders.objects.filter(order_id=orderId, email=email)

        if len(order)>0:
            updates = OrderUpdate.objects.filter(order_id=orderId)
            length =len(updates);
            list1=[]

            #updates=[]

            #for item in update:
             #   updates.append([item.update_desc,item.timestamp])

            #prod_details =order[0].items_json
            #print(prod_details)
            prod_details= json.loads(order[0].items_json)
            print(prod_details)

            for item in prod_details:
               value= prod_details[item][0]
               name = prod_details[item][1]
               list1.append([value,name])

            params ={'updates':updates,'prod_details':list1,'length':length}
            return render(request,'shop/tracker.html', params)



        else:

            updates = OrderUpdate.objects.filter(order_id=orderId)
            length = len(updates);
            params ={'length':length}
            return render(request,'shop/tracker.html',params)

    return render(request, 'shop/tracker.html')


def searchfunc(query,item):
    if query in item.product_name.lower() or query in item.product_category.lower() or query in item.product_desc.lower():
        return True
    else:
        return False




def search(request):
    query = request.GET.get('search')
    query =query.lower();

    params = {}
    products = Product.objects.all()
    print(products)
    allprods = []

    category_of_products = Product.objects.values('product_category')  # it will give category of products in object form {product_category:instrument} }
    print(category_of_products)

    category = {item['product_category'] for item in category_of_products}  # from here we will story all categories in list
    print(category)

    for cat in category:
        prod1 = Product.objects.filter(product_category=cat)  # category wise product will get store in prod
        prod =  [ item for item in prod1 if searchfunc(query,item) ]  # only those product will get store which matches with query
        print(prod)
        n = len(prod)
        slides = 0
        if (n / 4 != 0):
            slides = n // 4 + 1
            print(slides)

        if (n / 4 == 0):
            slides = n // 4
            print(slides)

        allprods.append([prod, range(0, slides), slides])  # list of list will be formed
        if n<0:
         msg="not found anything realted"
         params={'allprods': allprods,'msg':msg}
        else:
         params = {'allprods': allprods}

    return render(request, "shop/search.html", params)






