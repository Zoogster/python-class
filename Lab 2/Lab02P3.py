admission_only = float(input('Enter amount of people only buying admission: '))
show_only = float(
    input('Enter amount of people only buying an IMAX show ticket: '))
combo = float(
    input('Enter amount of people buying the admission and show combo: '))
admission_only_total = admission_only * 14
show_only_total = show_only * 8
combo_price = 0.75 * (14+8)
combo_total = combo * combo_price
amount_due = admission_only_total + show_only_total + combo_total
print('Amount due: $', amount_due)
