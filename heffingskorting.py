#class voor een loonheffingskortingschaal (uniek per jaar)
class Heffingskortingschaal:
    def __init__(self, naam, jaar, heffingskortingschijf1, heffingskortingschijf2,
                 heffingskortingschijf3):
        self.naam = naam
        self.jaar = jaar
        self.heffingskortingschijf1 = heffingskortingschijf1
        self.heffingskortingschijf2 = heffingskortingschijf2
        self.heffingskortingschijf3 = heffingskortingschijf3
        self.heffingskortingschijven = [heffingskortingschijf1, heffingskortingschijf2, heffingskortingschijf3]

#class voor een loonheffingskortingschijf in de loonheffingskortingschaal
class Heffingskortingschijf:
    def __init__(self, naam, schijfnummer, ondergrens, bovengrens, basisheffingskorting, heffingskortingpercentage):
            self.naam = naam
            self.schijfnummer = schijfnummer
            self.ondergrens = ondergrens
            self.bovengrens = bovengrens
            self.basisheffingskorting = basisheffingskorting
            self.heffingskortingpercentage = heffingskortingpercentage

class HeffingskortingCalculator():

    def __init__(self):
        #In code definieren van heffingsschalen, kan later csv
        self.heffingskortingschaal2017 = Heffingskortingschaal(
            naam="Heffingskortingschaal 2017",
            jaar="2017",
            heffingskortingschijf1=Heffingskortingschijf("heffingskortingschijf 1", 1, 0, 19982, 2254, 0),
            heffingskortingschijf2=Heffingskortingschijf("heffingskortingschijf 2", 2, 19983, 67068, 2254, -0.04787),
            heffingskortingschijf3=Heffingskortingschijf("heffingskortingschijf 3", 3, 67069, 99999999, 0, 0))

        self.heffingskortingschaal2019 = Heffingskortingschaal(
            naam="Heffingskortingschaal 2019",
            jaar="2019",
            heffingskortingschijf1=Heffingskortingschijf("heffingskortingschijf 1", 1, 0, 20384, 2477, 0),
            heffingskortingschijf2=Heffingskortingschijf("heffingskortingschijf 2", 2, 20385, 68507, 2477, -0.05147),
            heffingskortingschijf3=Heffingskortingschijf("heffingskortingschijf 3", 3, 68508, 99999999, 0, 0))

        self.heffingskortingschaal2020 = Heffingskortingschaal(
            naam="Heffingskortingschaal 2020",
            jaar="2020",
            heffingskortingschijf1=Heffingskortingschijf("heffingskortingschijf 1", 1, 0, 20711, 2711, 0),
            heffingskortingschijf2=Heffingskortingschijf("heffingskortingschijf 2", 2, 20712, 68507, 2711, -0.05672),
            heffingskortingschijf3=Heffingskortingschijf("heffingskortingschijf 3", 3, 68508, 99999999, 0, 0))

    def get_heffingskortingschijf(self, brutojaarsalaris, heffingskortingschaal):
        for heffingskortingschijf in heffingskortingschaal.heffingskortingschijven:
            if brutojaarsalaris < heffingskortingschijf.bovengrens and \
            brutojaarsalaris >= heffingskortingschijf.ondergrens:
                return(heffingskortingschijf)


    def bereken_heffingskorting(self, brutojaarsalaris, jaar):
        if jaar == 2017:
            heffingskortingschaal = self.heffingskortingschaal2017
        elif jaar == 2019:
            heffingskortingschaal = self.heffingskortingschaal2019
        elif jaar == 2020:
            heffingskortingschaal = self.heffingskortingschaal2020

        relevante_schijf = self.get_heffingskortingschijf(brutojaarsalaris, heffingskortingschaal)
        heffingskorting = relevante_schijf.basisheffingskorting + \
        relevante_schijf.heffingskortingpercentage * (brutojaarsalaris - relevante_schijf.ondergrens + 1)
        
        return(round(heffingskorting, 2))
