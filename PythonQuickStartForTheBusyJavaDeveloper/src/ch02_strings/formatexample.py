product = "Apple iMac"
price = 3699

# Varianten der formatierten Ausgabe
print("the", product, "costs", price)
print("the {} costs {}".format(product, price))
print("the %s costs %d" % (product, price))
print(f"the {product} costs {price}")

# print("the %s costs %d" % (3.1415, "UNSINN"))