#Inventory stock counter
print("===Inventory stock counter===")
print("Counting stock for products one at a time")
box_sizes = [5 , 20 , 10 , 5 , 1]
products_counted = 0
total_items = 0
log = [] 
counting = True
while counting:
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity for {product_name}: "))
    
    if quantity <= 0 :
        print("Invalid quantity! Please enter a positive number")
        continue
    print(f"Paking {quantity} items of {product_name}")
    print("-" * 30)

    remaining = quantity
    i = 0
    used = {}
    #Inner while loop - breaks quantity into box_sizes
    while i < len(box_sizes):
        count = remaining // box_sizes[i]
        if count > 0 :
            print(f"{count}box(es) is of {box_sizes[i]} items = {count * box_sizes[i]}")
            used[box_sizes[i]] = count

            remaining -= count * box_sizes[i]
        i += 1
        products_counted += 1
        total_items += quantity
        log.append({'product' : product_name , 'used' : used})

        print(f"Stock succesfully counted for {product_name}")
        again = input("Would you like o add another product(yes/no)").strip().lower()
        if again != 'yes':
            counting = False
print("==Final box size report==")
for box in box_sizes:
    total_boxes = 0 

    for entry in log:
        total_boxes += entry["used"].get(box , 0)

    if total_boxes > 0:
        print(f"{box}-item boxes used today: {total_boxes}")
print(f"products_counted = {products_counted}")
print(f"total items = {total_items}")
print("Inventry counting complete!\n")
print("Thanks for using this website! plese come again")