import csv
import json


def main():
    
    file_name = collect_all_csv_filenames()
    class_info,team_name_spaces_count,team_name_camel_count = read_csv(file_name)
    write_data(class_info)
    
    
    
    print 'People who used camelCase'
    print team_name_camel_count
    
    STDOUT = team_name_camel_count/3
    print 'STDOUT'
    print STDOUT


def collect_all_csv_filenames(): # complete
    import glob
    file_name = []
    for files in glob.glob("*.csv"):
        if files!='mlp6.csv':
            file_name.append(files)
    return file_name


def read_csv(file_name): # complete
    # read in CSV
    class_info = []
    for i in range(0,len(file_name)): #  loop over total number of .csv files 
        individual_info = []
        with open(file_name[i]) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            row = next(csvReader)
            for j in range(0, 5):
                if (' ' == row[j][0]) == True: # checks for a space at the beginning of the string, cuts it off if it exists
                    individual_info.append(row[j][1:])
                else: # else, dont cut it off
                    individual_info.append(row[j])
        class_info.extend(individual_info)
        json_write(individual_info)
        
    team_name_spaces_count = check_no_spaces(class_info[4::5])
    team_name_camel_count = check_camel_case(class_info[4::5])
    return class_info, team_name_spaces_count, team_name_camel_count

    
def json_write(individual_info): # complete
    # create file name
    new_file_name = []
    new_file_name.append(individual_info[2])
    new_file_name.append('.json')
    new_file_name = ''.join(new_file_name)
    
    #convert to json format
    json_class_info = json.dumps(individual_info)
    
    # write to file
    with open(new_file_name, 'w') as outfile:
        json.dump(json_class_info, outfile)
    pass
 

def write_data(class_info): # complete
    # write class_info to one large file
    with open("everyone.csv", 'w') as outfile:
        writer = csv.writer(outfile,lineterminator = '\n')
        
        for i in range(len(class_info)/5): # loop through data and write
            writer.writerow(class_info[0+i*5:5+i*5])
        
    pass


def check_no_spaces(team_name): # complete
    team_name_spaces_count = 0
    if (' ' in team_name) == True:
        team_name_spaces_count = team_name_spaces_count+1
    return team_name_spaces_count


def check_camel_case(team_name): # complete, returns the number of people who used camelCase
    team_name_camel_count = 0
    for team_name_individual in team_name:
        if (team_name_individual != team_name_individual.lower() and team_name_individual != team_name_individual.upper()) == True:
            team_name_camel_count = team_name_camel_count+1
    return team_name_camel_count
    

if __name__ == "__main__":
    main()
    
  