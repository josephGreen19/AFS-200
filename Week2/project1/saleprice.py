product=(input("Enter a description for a product "))

quantity=int(input(f"How many of {product} are being purchased? "))

regPrice=float(input("what is the regular price of product? "))

print("Your Receipt")

save= float(regPrice*15/100*quantity)
bgSave=float(regPrice*25/100*quantity)
discount= float(regPrice-regPrice*15/100)
tax= float(6.5/100*quantity*discount)
bgDiscount= float(regPrice-regPrice*25/100)
regTax=float(6.5/100*quantity*regPrice)
bgTax= float(6.5/100*quantity*bgDiscount)
bgTotal= float(bgTax+bgDiscount*quantity)
total= float(tax+discount*quantity)
regTotal= float(tax+regPrice*quantity)

if regPrice > 19.99 and regPrice < 39.99:
    print(f"{quantity} {product} @ ${discount:.2f} each")
    print(f"Sales Tax ${tax:.2f}")
    print(f"Total amount due ${total:.2f}")
    print(f"You saved ${save:.2f} today")


elif regPrice > 39.99:
    print(f"{quantity} {product} @ ${bgDiscount:.2f} each")
    print(f"Sales Tax ${bgTax:.2f}")
    print(f"Total amount due ${bgTotal:.2f}")
    print(f"You saved ${bgSave:.2f} today")

else :
    print(f"{quantity} {product} @ ${regPrice:.2f} each")
    print(f"Sales Tax ${regTax:.2f}")
    print(f"Total amount due ${regTotal:.2f}")
    print("There is no savings today")




