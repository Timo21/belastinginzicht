#class voor een loonbelastingschaal (uniek per jaar)
class Loonbelastingschaal:
    def __init__(self, naam, jaar, belastingschijf1, belastingschijf2,
                 belastingschijf3, belastingschijf4):
        self.naam = naam
        self.jaar = jaar
        self.belastingschijf1 = belastingschijf1
        self.belastingschijf2 = belastingschijf2
        self.belastingschijf3 = belastingschijf3
        self.belastingschijf4 = belastingschijf4
        self.belastingschijven = [belastingschijf1, belastingschijf2, belastingschijf3, belastingschijf4]


#class voor een loonbelastingschijf in de loonbelastingschaal
class Loonbelastingschijf:
    def __init__(self, naam, schijfnummer, ondergrens, bovengrens, loonbelastingspercentage):
            self.naam = naam
            self.schijfnummer = schijfnummer
            self.ondergrens = ondergrens
            self.bovengrens = bovengrens
            self.loonbelastingspercentage = loonbelastingspercentage


#In code definieren van belastingschalen, kan later csv
loonbelastingschaal2017 = Loonbelastingschaal(
    naam="Belastingschaal 2017",
    jaar="2017",
    belastingschijf1=Loonbelastingschijf("Belastingschijf 1", 1, 0, 19982, 0.3655),
    belastingschijf2=Loonbelastingschijf("Belastingschijf 2", 2, 19983, 33791, 0.408),
    belastingschijf3=Loonbelastingschijf("Belastingschijf 3", 3, 33792, 67072, 0.408),
    belastingschijf4=Loonbelastingschijf("Belastingschijf 4", 4, 67073, 999999999, 0.502))

loonbelastingschaal2019 = Loonbelastingschaal(
    naam="Belastingschaal 2019",
    jaar="2019",
    belastingschijf1=Loonbelastingschijf("Belastingschijf 1", 1, 0, 20384, 0.3665),
    belastingschijf2=Loonbelastingschijf("Belastingschijf 2", 2, 20385, 34300, 0.381),
    belastingschijf3=Loonbelastingschijf("Belastingschijf 3", 3, 34301, 68507, 0.381),
    belastingschijf4=Loonbelastingschijf("Belastingschijf 4", 4, 68508, 999999999, 0.5175))


def get_loonbelastingschijf(brutojaarsalaris, belastingschaal):
    for belastingschijf in belastingschaal.belastingschijven:
        if brutojaarsalaris < belastingschijf.bovengrens and \
           brutojaarsalaris >= belastingschijf.ondergrens:
            return(belastingschijf.schijfnummer)


def bereken_loonheffing(brutojaarsalaris, loonbelastingschaal):
    schijfnummer = get_loonbelastingschijf(brutojaarsalaris, loonbelastingschaal)
    belastingschijf1 = loonbelastingschaal.belastingschijf1
    belastingschijf2 = loonbelastingschaal.belastingschijf2
    belastingschijf3 = loonbelastingschaal.belastingschijf3
    belastingschijf4 = loonbelastingschaal.belastingschijf4

    def opt1():
        loonbelasting = brutojaarsalaris * belastingschijf1.loonbelastingspercentage
        return(loonbelasting)

    def opt2():
        loonbelasting = belastingschijf1.bovengrens * \
            belastingschijf1.loonbelastingspercentage + \
            (brutojaarsalaris - belastingschijf1.bovengrens) * \
            belastingschijf2.loonbelastingspercentage
        return(loonbelasting)

    def opt3():
        loonbelasting = belastingschijf1.bovengrens * \
            belastingschijf1.loonbelastingspercentage + \
            (belastingschijf2.bovengrens - belastingschijf1.bovengrens) * \
            belastingschijf2.loonbelastingspercentage + \
            (brutojaarsalaris - belastingschijf2.bovengrens) * \
            belastingschijf3.loonbelastingspercentage
        return(loonbelasting)

    def opt4():
        loonbelasting = belastingschijf1.bovengrens * \
            belastingschijf1.loonbelastingspercentage + \
            (belastingschijf2.bovengrens - belastingschijf1.bovengrens) * \
            belastingschijf2.loonbelastingspercentage + \
            (belastingschijf3.bovengrens - belastingschijf2.bovengrens) * \
            belastingschijf3.loonbelastingspercentage + \
            (brutojaarsalaris - belastingschijf3.bovengrens) * \
            belastingschijf4.loonbelastingspercentage
        return(loonbelasting)

    options = {1: opt1, 2: opt2, 3: opt3, 4: opt4}
    loonbelasting = options[schijfnummer]()

    return(round(loonbelasting, 2))
