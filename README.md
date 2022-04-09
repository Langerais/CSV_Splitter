#   Takes ',' delimited .csv from 'IN' folder. / Loops through every file in the folder
#   Splits it randomly to 2 .csv files according to provided share percentage
#   Saves in 2 separate files in the 'OUT' folder like splitFile_Body_* and splitFile_Share_* with * bring the number of input file
#   Share can be passed as cmd arg or, if not provided, prompts for share. If left blank - set to default
#   Prints the summary of the files after each input file
#   Since the pick is random, the size of final share files may not be 100% as specified by share (+/- 3% for our datasets)
#   Adds headers to both files