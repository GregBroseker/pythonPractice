# Prints out the comission you would make on a total repair price (2% comission)
#repair_price = input("Enter total repair price: ")
#print("The repair price is: " + repair_price)
#repair_comission = float(repair_price) * .02
#print("The comission earned on this repair is: " , repair_comission)

# Prints out the comission you would make on a total sale price (3% comission)
#sale_price = input("Enter total sale price: ")
#print("The sale price is: " + sale_price)
#sale_comission = float(sale_price) * .03
#print("The comission earned on this sale is: " , sale_comission)

# Prints out the comission you would make on a total accessory price (10% comission)
#accessory_price = input("Enter total accessory price: ")
#print("The accessory price is: " + accessory_price)
#accessory_comission = int(accessory_price) * .10
#print("The comission earned on these accessories is: " , accessory_comission)

#create an array called repairs
repairs = [159.99, 99.99, 119.99, 199.99, 249.99, 299.99, 349.99, 399.99, 499.99, 219.99]
# i is the loop counter that corresponds to each element in the array starting with the first. Note that i doesn't get the true value of the element in the array
# like x does it is just a reference or index of what position each element in the array is in. (when x = 159.99, i = 1; when x = 99.99, i = 2; when x = 119.99. i = 3; etc.)
i = 0
#sum starts at 0 and is added to itself by x which is the for loop variable that gets assigned the element values in the repairs array (all x values added together)
sum = 0
#loop through repairs array and assign each value to x through each pass
for x in repairs: 
    #increase loop counter value by 1
    i = i + 1
    #add next x value to sum variable
    sum = sum + x
    print('Repair price', i , 'is:' , x)
    #if repairs array is at end of list print the sum variable of all repairs as well as the commission earned from them.
if repairs[-1]:
    print('The total price of all repairs is: ', sum)
repair_comission = sum * .02
print('The total comission earned on these repairs is', repair_comission)
# To make easy sense of this note that i, sum, and x all get incremented at same time together

sales = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
i = 0
sum = 0
for x in sales: 
    i = i + 1
    sum = sum + x
    print('Sale price', i , 'is:' , x)
if sales[-1]:
    print('The total price of all sales is: ', sum)
sale_comission = sum * .03
print('The total comission from sales is', sale_comission)

#note that you can easily change the values of variables in the global scope
#so this is why its best to get scope localized by using functions and classes

accessories = [20, 40, 45, 50, 60, 80, 100, 120, 150, 200]
i = 0
sum = 0
for x in accessories: 
    i = i + 1
    sum = sum + x
    print('Accessory price', i , 'is:' , x)
if accessories[-1]:
    print('The total price of all accessories is: ', sum)
accessory_comission = sum * .10
print('The total comission earned on these accessories is', accessory_comission)