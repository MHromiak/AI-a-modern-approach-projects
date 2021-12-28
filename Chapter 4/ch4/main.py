from NQueensHillSearch import NQueensHillSearch as NQHS
from NQueensRandomRestartHillSearch import NQueensRandomRestartHillSearch as NQRRHS



def main():
    ## Uncomment to run a regular hill search
    # queens_hill_search : NQHS = NQHS(8, 30000)
    # queens_hill_search.execute()

    #Uncomment to run a random-restart hill search
    queens_random_restart_hill_search : NQRRHS = NQRRHS(8, 10000, 4, 150)
    while queens_random_restart_hill_search.restarts_remaining > 0:
        queens_random_restart_hill_search.execute()





if __name__ == "__main__":
    main()