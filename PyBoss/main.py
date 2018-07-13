import sys
import csv
from datetime import datetime

# State name to abbreviation mapping table
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#  Function to generate row ready to be written to CSV file
def gen_row(emp_id, name, fmt_date, ssn_part, state):
  name_part = name.strip().split()
#  print("{}, {}, {}, {}, ***-**-{}, {}".
#      format(emp_id, name_part[0], name_part[1], fmt_date.strftime('%m/%d/%y'),
#      ssn_part, us_state_abbrev[state]))
  return [emp_id, name_part[0], name_part[1], fmt_date.strftime('%m/%d/%y'),
      "***-**-" + ssn_part, us_state_abbrev[state]]



#  open data file and output file
with open("employee_data.csv", 'r', encoding="utf8") as infile, \
     #  Without newline="" csvwriter writes \r\r\n for every \n
     open("processed_emp_data.csv", 'w', newline="") as outfile:
       reader = csv.reader(infile, delimiter=",")
       writer = csv.writer(outfile)

       #  Read the header row first (skip this step if there is no header)
       csv_header = next(reader)

       #  Write CSV header only if the current file has atleast one input row
       if csv_header:
         writer.writerow(["Emp ID", "First Name",
                          "Last Name", "DOB", "SSN", "State"])

       #  Initialize ssn list
       ssn_list = []

       #  Step thru each row of CSV file
       for row in reader:
         # Do not process empty line in CSV file
         if row:
           #  Extract values from a tuple
           emp_id, name, dob, ssn, state = row
           ssn_list = ssn.split("-")
           state = state.strip()
           fmt_date = datetime.strptime(dob, "%Y-%m-%d")
           writer.writerow(gen_row(emp_id, name, fmt_date, ssn_list[2], state))
         # else:
           # print("Empty line")

#
