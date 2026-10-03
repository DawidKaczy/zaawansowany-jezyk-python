from functools import partial

def apply_tax(net_price, tax_rate):
    gross_price = net_price * (1 + tax_rate / 100)
    return round(gross_price, 2)

vat_23 = partial(apply_tax, tax_rate=23)

vat_8 = partial(apply_tax, tax_rate=8)



wynik_23 = vat_23(200)
wynik_8 = vat_8(50)

print("--- Wyniki obliczeń podatkowych ---")
print(f"Cena netto: 200, VAT 23% -> Cena brutto: {wynik_23:.2f}")
print(f"Cena netto: 50,  VAT 8%  -> Cena brutto: {wynik_8:.2f}")