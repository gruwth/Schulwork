while True:
    try:
        e = int(input("Was möchtest du umrechnen\n1: cm in inch \n2: inch in cm \n"))
        match e:
            case 1:
                cm = float(input("Zentimeter angeben: "))
                inch = cm / 2.54
                print(f"{cm}cm sind {inch:.2f} Inches")
                break
            case 2:
                inch = float(input("Inches angeben: "))
                cm = inch * 2.54
                print(f"{inch} Inches sind {cm:.2f}cm")
                break
            case _:
                print("Bitte gib 1 oder 2 ein")
    except:
        print("Du huan machs richtig")
