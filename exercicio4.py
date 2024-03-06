def find_switches_lamps():

    switches = [False, False, False]
    lamps = [False, False, False]

    switches[0] = True
    switches[1] = True

    for i in range(3):
        lamps[i] = switches[0] or (not switches[1] and switches[2])

    print("estado das lampadas:", lamps)


find_switches_lamps()
