loondienst <- 3450 * 6 + 3197 + 184 - 1144 # Jan t/m Jun (vakantiegeld eigenlijk ook in 2018 verdient..)
jul_aug <- (5796 + 2323) * 0.79
zzp <- (36 * 4/12 * 47 * 75)

loondienst + jul_aug + zzp

belastbaar <- 33807

zvw <- 1927

vrije_winst <- jul_aug + zzp - belastbaar

loondienst + belastbaar
38063 # is wat je netto overhoud als je loondienst + belastbaar belasting betaalt

netto <- 38063 + vrije_winst - zvw

# Netto loon staat gelijk aan 85k loondienst