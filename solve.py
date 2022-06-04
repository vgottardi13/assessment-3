import pandas as pd


orders_df = pd.read_csv("orders.csv")
order_details_df = pd.read_csv("order_details.csv")
product_categories_df = pd.read_json("pc.json")

period = "July 2021"

print(f"\nThis a estimation of the budget of the freights in the next month for this business. See results below")

def question_1(low,mid,high):
    total_freight = orders_df['freight'].sum()
    result_str = f"\nThe total freight expense for {period} is ${total_freight:,.2f}. Based on this, below estimates are provided.\n\n"
    result_str = f"low range budget increase {low}% is ${total_freight * (1 + low/100):,.2f}\n"
    result_str = f"mid range budget increase {mid}% is ${total_freight * (1 + mid/100):,.2f}\n"
    result_str = f"high range budget increase {high}% is ${total_freight * (1 + high/ 100):,.2f}\n"
    return result_str

print(question_1(5,10,15))

def question_2(top_n_rows):
    orders_group_by_country = orders_df.groupby('ship_country').size().nlargest(top_n_rows).reset_index()
    result_str = f"\nTop {top_n_rows} destination countries with number of orders placed in {period}.\n\n"
    result_str += "Country              No. of orders\n"
    result_str += "---------            -------------\n"
    for row in range(0,top_n_rows):
        result_str += f"{orders_group_by_country.iloc[row, 0]:<25}{orders_group_by_country.iloc[row, 1]:>5}\n"
        return result_str

print(question_2(3))

def question_3(top_n_rows):
    orders_group_by_customer = orders_df.groupby('customer_name').size().nlargest(top_n_rows).reset_index()
    result_str = f"\nTop {top_n_rows} customers with number of orders placed in {period}.\n\n"
    result_str += "Country              No. of orders\n"
    result_str += "---------            -------------\n"
    for row in range(0, top_n_rows):
        result_str += f"{orders_group_by_customer.iloc[row, 0]:<25}{orders_group_by_customer.iloc[row, 1]:>5}\n"
        return result_str

print(question_3(3))

def question_4(top_n):
    order_details_df["total_price"] = order_details_df["unit_price"] * order_details_df["quantity"]
    order_details_product_category = order_details_df.groupby(["product_category_id"], as_index=False).sum("total_price").nlargest(top_n,"total_price")
    top_sale = order_details_product_category.join(product_categories_df.set_index("category_id"), on="product_category_id")
    result_str = f"\nTop {top_n} product category with the highest sales revenue in the period {period}.\n\n"
    result_str += "Product cat. ID           Total sales revenue               Category name                Description           \n"
    result_str += "--------------------     --------------------              ------------------           -----------------      \n"
    for row in range(top_n):
        result_str += f"{top_sale.iloc[row, 0]:>15}      ${top_sale.iloc[row, 4]:>10,.02f}"
        result_str += f"{top_sale.iloc[row,5]:<15}       ${top_sale.iloc[row,6]:<60}\n"
        return result_str

print(question_4(1))
