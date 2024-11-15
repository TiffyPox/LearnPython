# A function that inserts the product code after the third character
def add_product_code(prod_code, prod_id):
    # If product code is missing
    if prod_id[3] != '-':
        return (f"{prod_id[:3]}-{prod_code}-{prod_id[3:]}")
    else:
        return prod_id

def main():
    print("Hello World")

x = "Tiffany"

print(x.upper())
print(x.lower())

y = "Tiffypox"

print(y.strip()) # removes whitespace from beginning or end

print(y.replace("p", "b"))

print(y.split("p"))

z = "gREEN fROG"

print(z.swapcase())

product_code1 = "70912"
product_id1 = "JOKFRT-LPO-8BHY-1PL-2ON"

product_code2 = "09234"
product_id2 = "GHO-09234-BNW-DFL-3N-GLSM"

result1 = add_product_code(product_code1, product_id1)
result2 = add_product_code(product_code2, product_id2)

print(f"{result1}\n{result2}")

if __name__ == '__main__':
    main()