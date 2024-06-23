#### Problem: Simple Analysis on NBA 2022-23 Standings

def open_csv_file(filename) :
    with open(filename,"r") as fr :
        lines = fr.readlines()

        header = lines[0].strip().split(",")

        dataset = []
        for line in lines[1:] :
            value = line.strip().split(",")
            observed_value = {header[i]: value[i] for i in range(len(header))}

            dataset.append(observed_value)
    
    return dataset

    ''' dataset = [{observed value 1.},
                   {observed value 2.},
                   {observed value 3.},
                                .
                                .
                                .
                   {observed value 30.}] '''
    # where observed_value = {"Conference":"Eastern", "Team":"Bucks", "W-L":"58-24", ... , "STRK":"L2" }

## Question 1. Which teams from the Eastern Conference had the win-loss percentage of Home lower than the win-loss percentage of Away?
def Q1(dataset) :
    # Collect the teams with "Eastern Conference"
    East_conf = []
    for team in dataset :
        if team["Conference"] == "Eastern" :
            East_conf.append(team)
    
    # Collect those Eastern Conference teams with  win-loss percentage of Home lower than the win-loss percentage of Away
    East_conf_lower_home_win_rate = []
    for team in East_conf :
        home_record = team["HOME"].split("-") # eg. home_record = [23,18]
        home_win_rate = float(home_record[0])/float(home_record[1])

        away_record = team["AWAY"].split("-") # eg. away_record = [25,16]
        away_win_rate = float(away_record[0])/float(away_record[1])

        if home_win_rate < away_win_rate :
            team["home wr"] = home_win_rate
            team["away wr"] = away_win_rate
            East_conf_lower_home_win_rate.append(team)
    
    for team in East_conf_lower_home_win_rate :
        print("\'%s\' has the win-loss percentage of Home lower than Away"%team["Team"])


## Question 2. Which conference had a higher average difference about “PF minus PA”?
def Q2(dataset) :
    # Collect the teams with "Western Conference"
    West_conf = []
    for team in dataset :
        if team["Conference"] == "Western" :
            West_conf.append(team)
            
    # # Collect the teams with "Eastern Conference"
    East_conf = []
    for team in dataset :
        if team["Conference"] == "Eastern" :
            East_conf.append(team)

    # Calculate the average difference between points scored (PF) and points allowed (PA)
    sum = 0
    count = 0
    if West_conf :
        for team in West_conf :
            PF = float(team["PF"])
            PA = float(team["PA"])
            diff = PF-PA
            sum += diff
            count += 1

        ave_diff_w = sum/count
    else :
        ave_diff_w = 0  
    
    sum = 0
    count = 0
    if East_conf :
        for team in East_conf :
            PF = float(team["PF"])
            PA = float(team["PA"])
            diff = PF-PA
            sum += diff
            count += 1

        ave_diff_e = sum/count
    else :
        ave_diff_e = 0

    # Decide Which conference had a higher average difference about PF minus PA
    if ave_diff_w > ave_diff_e :
        print("Western")
    elif ave_diff_w < ave_diff_e :
        print("Eastern")
    else :
        print("Tie!")

## Question 3. Generate a ranking list of all teams such that a team wins more against the other conference’s team gets higher rank position. 
def Q3(dataset):
    inter_conf_win_rates = []

    # Calculate the win rate
    for team in dataset:
        wl_record = team["W-L"].split("-")  # e.g., "10-5" -> [10, 5]
        wins = int(wl_record[0])
        losses = int(wl_record[1])
        total_games = wins + losses

        win_rate = wins / total_games if total_games != 0 else 0

        inter_conf_win_rates.append((team["Team"], win_rate))

    # Sort the teams based on the win rate against the other conference
    inter_conf_win_rates.sort(key=lambda x: x[1], reverse=True)

    # Print the ranking
    for rank, (team, win_rate) in enumerate(inter_conf_win_rates, start=1):
        print(f"{rank}. \'{team}\' with win rate {win_rate:.2f}")

if __name__ == "__main__":
    filename = "C:/Users/yenwe/Desktop/PE8/pe8_data.csv"
    dataset = open_csv_file(filename)

    print("=" * 60)

    print("Question 1.")
    Q1(dataset)

    print()
    print("=" * 60)

    print()
    print("=" * 60)

    print("Question 2.")
    Q2(dataset)

    print("=" * 60)

    print()
    print("=" * 60)

    print("Question 3.")
    Q3(dataset)

    print("=" * 60)
    print()


