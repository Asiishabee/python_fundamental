
Create two functions: purchase_mobile and purchase_shoe
purchase_mobile() takes two parameters: price and brand
purchase_shoe() takes two parameters: price and material
If the mobile brand is “Apple”, discount is 10%, else discount is 5%
If the shoe material is “leather”, tax is 5%, else tax is 2%


def purshase_mobile(price,brand):
    if brand== "apple":
     discount =10
    else:
     discount =5
    
    total_price=price-price*discount/100
    print("Total price of "+brand+" is "+str(total_price))




def purshase_shoe(price,material):
    if material== "leather":
     tax =5
    else:
     tax =2
    
    total_price=price+price*tax/100
    print("Total price of "+material+" is "+str(total_price))
    
    
purshase_mobile(10000,"apple")
purshase_shoe(500,"wool")
