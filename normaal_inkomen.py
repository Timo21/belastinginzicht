from inkomstenbelasting import bereken_inkomstenbelasting
import pandas as pd

def bereken_normaal_inkomen(bruto, jaar, kosten = 0, representatiekosten = 0):
    inkomstenbelasting_details = bereken_inkomstenbelasting(bruto, jaar)
    inkomstenbelasting = inkomstenbelasting_details['inkomstenbelasting']
    netto = inkomstenbelasting_details['netto']
    print(inkomstenbelasting_details)

    normaal_inkomen_details = {
        'bruto': bruto,
        'inkomstenbelasting': inkomstenbelasting,
        'netto': netto
    }

    return(normaal_inkomen_details)

if __name__ == "__main__":
    inkomen_details = bereken_normaal_inkomen(40000, jaar = 2019)
    inkomen_details = pd.DataFrame(list(inkomen_details.items()), columns=['Post', 'Eur'])
    print(inkomen_details)
