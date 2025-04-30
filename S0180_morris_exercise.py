# S0185_morris_solution.py

def buy_whisky(morris):
    # forudsæt at morris["gold"] >= 1 og morris["whisky"] < 10
    morris["sleepiness"] += 5
    morris["thirst"]    += 1
    morris["hunger"]    += 1
    morris["whisky"]    += 1
    morris["gold"]      -= 1

def mine(morris):
    morris["sleepiness"] += 5
    morris["thirst"]    += 5
    morris["hunger"]    += 5
    morris["gold"]      += 5

def drink(morris):
    # forudsæt at morris["whisky"] >= 1
    morris["sleepiness"] += 5
    morris["thirst"]    -= 15
    morris["hunger"]    -= 1
    morris["whisky"]    -= 1

def sleep(morris):
    morris["sleepiness"] -= 10
    morris["thirst"]     -= 5
    morris["hunger"]     += 1

def eat(morris):
    # forudsæt at morris["gold"] >= 2
    morris["sleepiness"] += 5
    morris["thirst"]    -= 5
    morris["hunger"]    -= 20
    morris["gold"]      -= 2

def dead(morris):
    return (morris["sleepiness"] > 100 or
            morris["thirst"]     > 100 or
            morris["hunger"]     > 100)

def clamp(morris):
    # ingen attributter under 0, whisky maks 10
    for attr in ("sleepiness","thirst","hunger","gold"):
        if morris[attr] < 0:
            morris[attr] = 0
    if morris["whisky"] < 0:
        morris["whisky"] = 0
    if morris["whisky"] > 10:
        morris["whisky"] = 10

def choose_action(morris):
    # 1) undgå at dø på grund af søvn
    if morris["sleepiness"] > 90:
        return "sleep"
    # 2) tørst
    if morris["thirst"] > 60:
        if morris["whisky"] > 0:
            return "drink"
        elif morris["gold"] > 0 and morris["whisky"] < 10:
            return "buy_whisky"
        else:
            return "sleep"
    # 3) sult
    if morris["hunger"] > 60:
        if morris["gold"] >= 2:
            return "eat"
        else:
            # ikke råd til at spise: mine for at få penge
            return "mine"
    # ellers: mine for guld
    return "mine"

def simulate(turns=1000):
    morris = {
        "turn": 0,
        "sleepiness": 0,
        "thirst": 0,
        "hunger": 0,
        "whisky": 0,
        "gold": 0
    }

    for _ in range(turns):
        if dead(morris):
            print(f"Morris døde på tur {morris['turn']} 😢")
            break

        morris["turn"] += 1
        action = choose_action(morris)

        # udfør valgt handling
        if action == "sleep":
            sleep(morris)
        elif action == "drink":
            drink(morris)
        elif action == "buy_whisky":
            buy_whisky(morris)
        elif action == "eat":
            eat(morris)
        elif action == "mine":
            mine(morris)

        clamp(morris)

        # (valgfrit) debug print:
        # print(f"Turn {morris['turn']:3}: {action:11} → {morris}")

    else:
        # hvis loopet ikke blev brudt af død
        print("Simulation færdig uden død.")
    print("Slutstatus:", morris)
    return morris

if __name__ == "__main__":
    simulate()
