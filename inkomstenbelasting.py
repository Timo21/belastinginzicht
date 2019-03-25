from loonheffing import bereken_loonheffing, loonbelastingschaal2019
from heffingskorting import bereken_heffingskorting, heffingskortingschaal2019
from arbeidskorting import bereken_arbeidskorting, arbeidskortingschaal2019


def bereken_inkomstenbelasting(bruto):
    loonheffing = bereken_loonheffing(bruto, loonbelastingschaal2019)
    arbeidskorting = bereken_arbeidskorting(bruto, arbeidskortingschaal2019)
    heffingskorting = bereken_heffingskorting(bruto, heffingskortingschaal2019)
    inkomstenbelasting = round(-1 * loonheffing + arbeidskorting + heffingskorting, 2)
    netto = bruto + inkomstenbelasting

    # Necessary for very low income exceptions
    if netto > bruto:
        netto = bruto
        inkomstenbelasting = 0

    inkomstenbelasting_details = {
        'loonheffing': loonheffing,
        'arbeidskorting': arbeidskorting,
        'heffingskorting': heffingskorting,
        'inkomstenbelasting': inkomstenbelasting,
        'netto': netto,
        'bruto': bruto
    }

    return(inkomstenbelasting_details)


if __name__ == '__main__':
    print(bereken_inkomstenbelasting(45000))