import pathlib
import csv
csvpath = pathlib.Path("election_data.csv")
TotalNumber_votesCasted = 0

Votes = []
Candidates = []


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        TotalNumber_votesCasted += 1
        Votes.append(row[0])
        Candidates.append(row[2])
    #print(TotalNumber_votesCasted)
    
    Khan_vote = int(Candidates.count("Khan"))
    #print(Khan_vote)
    Correy_vote = int(Candidates.count("Correy"))
    #print(Correy_vote)
    Li_vote = int(Candidates.count("Li"))
    #print(Li_vote)
    O_Tooley_vote = int(Candidates.count("O\'Tooley"))
    #print(O_Tooley_vote)
   
   
    #Percentage vote for each candidate

    Khan_percentage = (Khan_vote  / TotalNumber_votesCasted) * 100
    #print(Khan_percentage)
    Correy_percentage = (Correy_vote / TotalNumber_votesCasted) * 100
    Li_percentage= (Li_vote / TotalNumber_votesCasted) * 100
    O_Tooley_percentage = (O_Tooley_vote / TotalNumber_votesCasted) * 100
    #print(O_Tooley_percentage)
   

    Votes = [Khan_vote, Correy_vote, Li_vote, O_Tooley_vote]

    # if the maximum of votes corresponds to an index from the list of votes, the object with that index is winner 

    if Votes.index(max(Votes)) == 0:
        Winner = "Khan"
    elif Votes.index(max(Votes)) == 1:
        Winner = "Correy"
    elif Votes.index(max(Votes)) == 2:
        Winner = "Li"
    else:
        Winner = "O'Tooley"
   
   

    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {TotalNumber_votesCasted}")
    print("---------------------")
    print(f"Khan: {Khan_percentage:.2f}% ({Khan_vote })")
    print(f"Correy: {Correy_percentage:.2f}% ({Correy_vote})")
    print(f"Li: {Li_percentage:.2f}% ({Li_vote})")
    print(f"O'Tooley: {O_Tooley_percentage:.2f}% ({O_Tooley_vote})")
    print("---------------------")
    print(f"Winner: {Winner}")
    print("---------------------")
   
   
output_path = pathlib.Path("PyPoll_output.txt")

with open(file=output_path, mode='w', newline='') as txtfile:
        txtfile.write("Election Results: \n")
        txtfile.write("------------------- \n")
        txtfile.write(f"Total Votes: {TotalNumber_votesCasted} \n")
        txtfile.write(f"Khan: {Khan_percentage:.2f}% ({Khan_vote }) \n")
        txtfile.write(f"Correy: {Correy_percentage:.2f}% ({Correy_vote}) \n")
        txtfile.write(f"Li: {Li_percentage:.2f}% ({Li_vote}) \n")
        txtfile.write(f"O'Tooley: {O_Tooley_percentage:.2f}% ({O_Tooley_vote}) \n")
        txtfile.write(f"Winner: {Winner}")
        txtfile.close()
   
   
   
   
   
   
   
   
   

    