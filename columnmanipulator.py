import csv

def columnmanipulator():
    # taking the extra commas off the end of each line
    edited_rows  = []
    with open('final_combined_output.csv', 'r') as infile:
        for row in csv.reader(infile):
            print(row)
            edited_rows.append(row[ : -1])

    # maiking a new file with the commas removed
    with open('final_combined_outputinputmodified.csv', 'w') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerows(edited_rows)

    # parsing the modified file to reorder
    with open('final_combined_outputinputmodified.csv', 'r') as infile, open('final_combined_output_output.csv', 'a', newline='') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Calendar Period Description','Calendar Run ID Description','Country','Country Description','Company Description','PAYROLL_STATUS','Employee ID','Name','Employee RCD','Location Description','HR Status','Business Unit','Dept Description','Step','Salary Admin Plan','Grade','Period Begin Date','Period End Date','Payment Date','Business Unit','Officer Code','Element Name','ELEMENT_CLASSIFICATION','Element Descr','Amount','Retro Amount','Currency','Position Number','Position Description','Employee Classification', 'Amount in USD ']

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)

    print("DONE")

columnmanipulator()
