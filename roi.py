print('This program will tell you about your cashflow and cash on cash ROI \
with a rental property.\nTell us about your rental income!')

def cashoncash():
    rent = int(input('\nHow much rent will you collect per month? '))

    print('Now for expenses...')
    mortgage = int(input('What will be the monthly mortgage payment? '))
    tax = int(input('Taxes? '))
    insur = int(input('Insurance? '))
    util = int(input('Utilities? '))
    hoa = int(input('HOA Fees? '))
    lawnsnow = int(input('Lawn/Snow? '))
    vacancy = int(input('How much would you like to save each month to prepare \
for a vacancy? '))
    repairs = int(input('Repairs? '))
    capex = int(input('Capex? '))
    management = int(input('Property Management? '))

    print('\nTell me about your initial investment.')
    down = int(input('How much is the down payment? '))
    closing = int(input('Closing costs? '))
    maint = int(input('Initial maintenance? '))
    misc = int(input('Other miscellaneous costs? '))

    expenses = sum([mortgage, tax, insur, util, hoa, lawnsnow, vacancy, \
repairs, capex, management])
    invest = sum([down, closing, maint, misc])
    print(f"Your monthly cashflow is ${rent - expenses}.")
    print(f"Your annual cash on cash ROI is {(rent - expenses) * 12 / invest * 100}%.")

cashoncash()