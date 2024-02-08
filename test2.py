

sold_index_list = [0, 1, 3]
sold_quants = [5, 3, 2]
sum_list = [399.95, 299.97, 119.98]
total = 0 # Initialize the total amount earned
print("Sales Report")
# Loop through the indexes list and use the loop variable as the index for the other two lists
for i,index in sold_index_list:
    quantity_sold = sold_quants[i] # Access the quantity sold from the quantities list using the same index
    amount_made = sum_list[i] # Access the amount made from the amounts list using the same index
    isbn, title, author, quantity, price = fields[index] # Use the index to access the corresponding book record from fields
    # Print the information of each book sold in a separate line with a label
    print(f"Book sold:\n\tISBN: {isbn}\n\tTitle: {title}\n\tAuthor: {author}\n\tQuantity sold: {quantity_sold}\n\tCurrent quantity: {quantity}\n\tAmount made: {amount_made}")
    total += amount_made # Add the amount made to the total amount earned

# Print the total amount earned at the end of the report
print(f"Total amount earned: {total}")