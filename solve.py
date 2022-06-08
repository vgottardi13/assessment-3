import pandas as pd
orders_df = pd.read_csv("orders.csv")
order_details_df = pd.read_csv("order_details.csv")
product_categories_df = pd.read_json("pc.json")
period = "July 2021"

print("\n Current Freight Budget : ", orders_df['freight'].sum())
print(f"\nThis is an estimation of the freight budget for the next month based on the above freight charges.")

def question_1(low,mid,high):
    total_freight = orders_df['freight'].sum()
    result_str = f"\nThe total freight expense for {period} is ${total_freight:,.2f}. Based on this, below estimates are provided.\n\n"
    result_str = f"Low range budget increase {low}% is ${total_freight * (1 + low/100):,.2f}\n"
    result_str = f"Mid range budget increase {mid}% is ${total_freight * (1 + mid/100):,.2f}\n"
    result_str = f"Estimated freight budget(high range {high}%)  is ${total_freight * (1 + high/ 100):,.2f}\n"
    return result_str

print(question_1(5,10,25))


# Question 2:
orders_by_country = orders_df.groupby('ship_country').size().sort_values(ascending=False)
print("\nTop 2 destination countries with number of orders placed in ", period)
print("Country    No. of orders")
print("----------------------")
print(orders_by_country.index[0],"    ", orders_by_country.iloc[0])
print(orders_by_country.index[1],"        ",orders_by_country.iloc[1])




# Question 3 :
def top_customers(no):
    orders_group_by_customer = orders_df.groupby('customer_name').size().nlargest(no).reset_index()
    print("\nTop 3 customers with number of orders placed in", period)
    print("\nCustomers        No. of orders")
    print("---------        -------------")
    for i in range(0, no):
        print(orders_group_by_customer.iloc[i, 0],"      ",orders_group_by_customer.iloc[i, 1])

top_customers(3)

# Question 4 :

def question_4(top_n):
    order_details_df["total_price"] = order_details_df["unit_price"] * order_details_df["quantity"]
    order_details_product_category = order_details_df.groupby(["product_category_id"], as_index=False).sum("total_price").nlargest(top_n,"total_price")
    top_sale = order_details_product_category.join(product_categories_df.set_index("category_id"), on="product_category_id")
    result_str = f"\nTop {top_n} product category with the highest sales revenue in the period {period}.\n\n"
    result_str += "Product cat. ID           Total sales revenue               Category name                Description           \n"
    result_str += "--------------------     --------------------              ------------------           -----------------      \n"
    for row in range(top_n):
        result_str += f"{top_sale.iloc[row, 0]:>15}      ${top_sale.iloc[row, 4]:>10,.02f}"
        result_str += f"{top_sale.iloc[row,5]:<15}       ${top_sale.iloc[row, 6]:<60}\n"
        return result_str

print(question_4(1))
