jackpot_amount = float(input('Amount won: '))
installmant_before_tax = jackpot_amount / 20
installmant_after_tax = installmant_before_tax * 0.7
cash_option_before_tax = jackpot_amount * 0.65
cash_option_after_tax = cash_option_before_tax * 0.7
print(
    f'The annual installment before taxes is ${installmant_before_tax} and after taxes it is ${installmant_after_tax}')
print(
    f'The cash option before taxes is ${cash_option_before_tax} and after taxes it is ${cash_option_after_tax}')
