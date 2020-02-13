from loonheffing import LoonbelastingCalculator
from heffingskorting import HeffingskortingCalculator
from arbeidskorting import ArbeidskortingCalculator


def bereken_inkomstenbelasting(bruto, jaar):
    loonbelasting_calculator = LoonbelastingCalculator()
    loonheffing = loonbelasting_calculator.bereken_loonheffing(bruto, jaar)

    arbeidskorting_calculator = ArbeidskortingCalculator()
    arbeidskorting = arbeidskorting_calculator.bereken_arbeidskorting(bruto, jaar)

    heffingskorting_calculator = HeffingskortingCalculator()
    heffingskorting = heffingskorting_calculator.bereken_heffingskorting(bruto, jaar)

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
    print(bereken_inkomstenbelasting(45000, 2020))