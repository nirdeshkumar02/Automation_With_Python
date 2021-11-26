import datetime

user_input = input("Enter your goal with a deadline separated by column: \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()
# Calculating how many days from now till deadline

time_till = deadline_date - today_date
print(f"Dear User, Time remaining for your goal: \n {time_till.days} days or {time_till.total_seconds() / 60 / 60} hours ")