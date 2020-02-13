from inkomstenbelasting import bereken_inkomstenbelasting
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def get_info(jaar):

    if jaar == 2019:
        info = {
            'zvw_premie_grens': 55927,
            'zvw_premie_percentage': 0.057,
            'zelfstandigenaftrek': 7280,
            'startersaftrek': 2123
        }
    elif jaar == 2020:
        info = {
            'zvw_premie_grens': 57232,
            'zvw_premie_percentage': 0.0545,
            'zelfstandigenaftrek': 7030,
            'startersaftrek': 2123,
        }

    return(info)

def bereken_zvw_premie(belastbaar_inkomen, info):
    if belastbaar_inkomen < 0:
        zvw_premie = 0
    
    if belastbaar_inkomen > info['zvw_premie_grens']:
        zvw_premie = round(info['zvw_premie_grens'] * info['zvw_premie_percentage'] * -1, 2)
    else:
        zvw_premie = round(belastbaar_inkomen * info['zvw_premie_percentage'] * -1, 2)

    return(zvw_premie)


def bereken_eenmanszaak_inkomen(
    omzet_ex_btw,
    jaar,
    kosten = 0,
    representatiekosten = 0,
    starter = True,
    urencriterium_voldaan = True
):

    info = get_info(jaar)

    # Hoogte zelfstandigen aftrek bepalen
    if urencriterium_voldaan and omzet_ex_btw >= info['zelfstandigenaftrek']:
        zelfstandigen_aftrek = info['zelfstandigenaftrek']
    
    elif urencriterium_voldaan:
        zelfstandigen_aftrek = omzet_ex_btw
    
    else:
        zelfstandigen_aftrek = 0

    omzet_over = omzet_ex_btw - zelfstandigen_aftrek

    # Hoogte startersaftrek bepalen
    if urencriterium_voldaan and starter:
        if omzet_over > info['startersaftrek']:
            starters_aftrek = info['startersaftrek']

        elif omzet_over > 0:
            starters_aftrek = omzet_over

        else:
            starters_aftrek = 0
    else:
        starters_aftrek = 0

    omzet_over = omzet_over - starters_aftrek

    # Hoogte kosten bepalen
    if omzet_over >= kosten:
        omzet_over = omzet_over - kosten
        kosten_niet_afgetrokken = 0
    else:
        omzet_over = 0
        kosten_niet_afgetrokken = kosten - omzet_over

    # Hoogte representatiekosten bepalen
    if omzet_over >= representatiekosten * 0.8:
        omzet_over = omzet_over - representatiekosten * 0.8
    else:
        omzet_over = 0
        representatiekosten_niet_afgetrokken = (representatiekosten * 0.8) - omzet_over

    # Hoogte mkb-winstvrijstelling bepalen
    mkb_winstvrijstelling = 0.14 * omzet_over
    belastbare_winst = (1 - 0.14) * omzet_over

    # Hoogte inkmostenbelasting
    inkomstenbelasting_details = bereken_inkomstenbelasting(belastbare_winst, jaar)
    inkomstenbelasting = inkomstenbelasting_details['inkomstenbelasting']

    # Zvw premie
    zvw_premie = bereken_zvw_premie(belastbare_winst, info)

    # Inkomen
    inkomen = belastbare_winst + inkomstenbelasting + mkb_winstvrijstelling + zelfstandigen_aftrek + starters_aftrek + zvw_premie
    inkomen = round(inkomen, 2)

    eenmanszaak_inkomen_details = {
        'omzet_ex_btw': omzet_ex_btw, 
        'zelfstandigen_aftrek': zelfstandigen_aftrek, 
        'starters_aftrek': starters_aftrek, 
        'kosten': kosten, 
        'representatiekosten': representatiekosten, 
        'mkb_winstvrijstelling': mkb_winstvrijstelling, 
        'belastbare_winst': belastbare_winst, 
        'inkomstenbelasting': inkomstenbelasting, 
        'zvw_premie': zvw_premie,
        'inkomen': inkomen
    }

    return(eenmanszaak_inkomen_details)


def plot_inkomsten_eenmanszaak():
    rows_list = list()
    uurtarieven = range(25, 125)
    for uurtarief in uurtarieven:
        omzet = uurtarief * 8 * 4 * 47
        eenmanszaak_details = bereken_eenmanszaak_inkomen(omzet, urencriterium_voldaan=True)
        rows_list.append({
            'uurtarief': uurtarief,
            'omzet_ex_btw': eenmanszaak_details['omzet_ex_btw'],
            'inkomen': eenmanszaak_details['inkomen']
        })

    df = pd.DataFrame(rows_list)
    df['huidige_arbeid'] = 32356
    
    plt.plot(df.uurtarief, df.omzet_ex_btw)
    plt.plot(df.uurtarief, df.inkomen)
    plt.plot(df.uurtarief, df.huidige_arbeid)

    fmt = '€{x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(tick)
    plt.gca().yaxis.grid(which="major")

    plt.legend()
    plt.show()

if __name__ == '__main__':
    eenmanszaak_details = bereken_eenmanszaak_inkomen(100000, 2020, kosten=0, urencriterium_voldaan=True, )
    eenmanszaak_details = pd.DataFrame(list(eenmanszaak_details.items()), columns=['Post', 'Eur'])
    print(eenmanszaak_details)
    # plot_inkomsten_eenmanszaak()  

    

