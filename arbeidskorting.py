#class voor eenarbeidskortingschaal (uniek per jaar)
class Arbeidskortingschaal:
    def __init__(self, naam, jaar, arbeidskortingschijf1, arbeidskortingschijf2,
                 arbeidskortingschijf3, arbeidskortingschijf4, arbeidskortingschijf5):
        self.naam = naam
        self.jaar = jaar
        self.arbeidskortingschijf1 = arbeidskortingschijf1
        self.arbeidskortingschijf2 = arbeidskortingschijf2
        self.arbeidskortingschijf3 = arbeidskortingschijf3
        self.arbeidskortingschijf4 = arbeidskortingschijf4
        self.arbeidskortingschijf5 = arbeidskortingschijf5
        self.arbeidskortingschijven = [arbeidskortingschijf1, arbeidskortingschijf2,
                                       arbeidskortingschijf3, arbeidskortingschijf4, arbeidskortingschijf5]

#class voor een Arbeidskortingschijf in de Arbeidskortingschaal
class Arbeidskortingschijf:
    def __init__(self, naam, schijfnummer, ondergrens, bovengrens, basisarbeidskorting, arbeidskortingpercentage):
            self.naam = naam
            self.schijfnummer = schijfnummer
            self.ondergrens = ondergrens
            self.bovengrens = bovengrens
            self.basisarbeidskorting = basisarbeidskorting
            self.arbeidskortingpercentage = arbeidskortingpercentage

class ArbeidskortingCalculator:

    def __init__(self):
        #In code definieren van arbeidskortingschalen, kan later csv
        self.arbeidskortingschaal2017 = Arbeidskortingschaal(
            naam="Arbeidskortingschaal 2017",
            jaar="2017",
            arbeidskortingschijf1=Arbeidskortingschijf("Arbeidskortingschijf 1", 1, 0, 9309, 0, 0.01772),
            arbeidskortingschijf2=Arbeidskortingschijf("Arbeidskortingschijf 2", 2, 9310, 20108, 165, 0.28317),
            arbeidskortingschijf3=Arbeidskortingschijf("Arbeidskortingschijf 3", 3, 20109, 32444, 3223, 0),
            arbeidskortingschijf4=Arbeidskortingschijf("Arbeidskortingschijf 4", 4, 32445, 121972, 3223,- 0.036),
            arbeidskortingschijf5=Arbeidskortingschijf("Arbeidskortingschijf 5", 5, 121973, 999999999, 0, 0))

        self.arbeidskortingschaal2019 = Arbeidskortingschaal(
            naam="Arbeidskortingschaal 2019",
            jaar="2019",
            arbeidskortingschijf1=Arbeidskortingschijf("Arbeidskortingschijf 1", 1, 0, 9694, 0, 0.01754),
            arbeidskortingschijf2=Arbeidskortingschijf("Arbeidskortingschijf 2", 2, 9695, 20940, 170, 0.28712),
            arbeidskortingschijf3=Arbeidskortingschijf("Arbeidskortingschijf 3", 3, 20941, 34060, 3399, 0),
            arbeidskortingschijf4=Arbeidskortingschijf("Arbeidskortingschijf 4", 4, 34061, 90710, 3399,- 0.06),
            arbeidskortingschijf5=Arbeidskortingschijf("Arbeidskortingschijf 5", 5, 90711, 999999999, 0, 0))

        self.arbeidskortingschaal2020 = Arbeidskortingschaal(
            naam="Arbeidskortingschaal 2020",
            jaar="2020",
            arbeidskortingschijf1=Arbeidskortingschijf("Arbeidskortingschijf 1", 1, 0, 9918, 0, 0.02813),
            arbeidskortingschijf2=Arbeidskortingschijf("Arbeidskortingschijf 2", 2, 9919, 21422, 279, 0.28825),
            arbeidskortingschijf3=Arbeidskortingschijf("Arbeidskortingschijf 3", 3, 21423, 34937, 3595, 0.01657),
            arbeidskortingschijf4=Arbeidskortingschijf("Arbeidskortingschijf 4", 4, 34938, 98587, 3819,- 0.06),
            arbeidskortingschijf5=Arbeidskortingschijf("Arbeidskortingschijf 5", 5, 98588, 999999999, 0, 0))



    def get_arbeidskortingschijf(self, brutojaarsalaris, arbeidskortingschaal):
        for arbeidskortingschijf in arbeidskortingschaal.arbeidskortingschijven:
            if brutojaarsalaris < arbeidskortingschijf.bovengrens and \
            brutojaarsalaris >= arbeidskortingschijf.ondergrens:
                return(arbeidskortingschijf)

    def bereken_arbeidskorting(self, brutojaarsalaris, jaar):
        
        if jaar == 2017:
            arbeidskortingschaal = self.arbeidskortingschaal2017
        elif jaar == 2019:
            arbeidskortingschaal = self.arbeidskortingschaal2019
        elif jaar == 2020:
            arbeidskortingschaal = self.arbeidskortingschaal2020

        relevante_schijf = self.get_arbeidskortingschijf(brutojaarsalaris, arbeidskortingschaal)
        arbeidskorting = relevante_schijf.basisarbeidskorting + \
        relevante_schijf.arbeidskortingpercentage * (brutojaarsalaris - relevante_schijf.ondergrens + 1)
        
        return(round(arbeidskorting, 2))

