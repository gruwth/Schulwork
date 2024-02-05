def steuer(gehalt, familienstand):
    if gehalt > 4000 and familienstand == "ledig":
        steuersatz = 0.26
    elif gehalt > 4000 and familienstand == "verheiratet":
        steuersatz = 0.22
    elif gehalt <= 4000 and familienstand == "ledig":
        steuersatz = 0.22
    else:
        steuersatz = 0.18
    steuer = gehalt * steuersatz
    print("Sie müssen", str(steuer), "€ als Steuer bei einem Steuersatz von", str(steuersatz*100), "% entrichten")

for i in 1800, 2200, 2500, 2900:
    steuer(i, "ledig")
    steuer(i, "verheiratet")
    print("")
