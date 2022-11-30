from tally_counter import TallyCounter
from building import Building

def main() -> None:
    tallyCounter = TallyCounter()
    building = Building()

    num_times = 0
    while num_times < 10:
        person = building.get_person()
        if person == "green shirt":
            tallyCounter.click()
        num_times += 1

    print("Num green shirts seen:", tallyCounter.count())

main()