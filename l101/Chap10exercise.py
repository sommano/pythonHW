def get_country_codes(prices):
    # your code here
    split_country = prices.split(", ")
    #print(split_country)
    #print(len(split_country))
    country = []
    for i in range(len(split_country)):
        country.append(split_country[i][:2])
    comma = ", "
    country = comma.join(country)
    return country

cc = "NZ$300, KR$1200, DK$5"
print(get_country_codes(cc))

# don't include these tests in Vocareum
#from test import testEqual

#testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
#testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
#testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
#testEqual(get_country_codes("CA$40"), "CA")
