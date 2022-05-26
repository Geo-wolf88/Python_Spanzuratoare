puzzle = "Divizibilitate"
solutie = "**************"
viata = 10
litere_corecte = []
litere_incorecte = []
while viata > 0 and puzzle != solutie:
    print(solutie)
    tip = input("Scrie o noua litera:\n")
    if len(tip) == len(puzzle):
        temp = solutie
        solutie = tip
        print("Ai incercat sa ghicesti solutia...si raspunsul tau e...")
        if solutie == puzzle:
            print("Correct.")
        else:
            print("Incorect.")
            viata -= 1
            print("Asta nu e din cuvantul cautat.Mai ai " + str(viata) + " vieti ramase.")
            solutie = temp
    else:
        gaseste_ceva = False
        for i in range(len(puzzle)):
            if puzzle[i] == tip:
                my_solution_list = list(solutie)
                my_solution_list[i] = tip
                solutie = "".join(my_solution_list)
                gaseste_ceva = True
        if not gaseste_ceva:
            litere_incorecte.append(tip)
            viata -= 1
            print("Asta nu e din cuvantul cautat.Mai ai " + str(viata) + " vieti ramase.")
        else:
            litere_corecte.append(tip)
        print("Lista literelor corecte: " + str(litere_corecte))
        print("List literelor incorecte: " + str(litere_incorecte))
if viata > 0:
    print("Felicitari!")
else:
    print("Poate reusesti data viitoare..\n")
