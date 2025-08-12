def calculate_product_sum(number_1,number_2):
    product=number_1*number_2
    if product<=1000:
        print(product)
    else:
        print(number_1+number_2)


num_1=input("input num 1:")
num_2=input("input num 2:")
print("User entered Number 1: ",num_1," and Number 2: ",num_2)
calculate_product_sum(int(num_1),int(num_2))
