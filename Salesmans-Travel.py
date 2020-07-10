# salesman has a list of addresses
# salesman wants to order addresses in following format
# zipcode:street_address1,street_address2/house1,house2
# r is the full text
# zipcode is the zip he wants to organize the addresses for

def travel(r, zipcode):
    if len(zipcode) < 8:
        return zipcode + ":/"
    addresses = list(r.split(","))
    house_num = []
    street = []
    for x in addresses:
        if zipcode in x:
            house_num.append(x[:x.find(" ")].strip())
            street.append(x[x.find(" "):-len(zipcode)].strip())
    return (zipcode + ":" +','.join(street)+"/"+",".join(house_num))
