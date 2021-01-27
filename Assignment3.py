print("Welcome MagicCopy Sdn. Bhd")
payCode = 0;
commissionRate = 5.5;
weeklyCommission = 500
salary = 0;
monthlySalary = 2000
counterLoop = 0
totalSalary = 0
previousData = []
map(int, previousData)


def calculatePayMontlyWorker(num):
    result = num * monthlySalary
    return result


def calculatePayHourlyWorker(numberWorker, hours):
    normal_hours = 40
    working_pay = 30
    overtime_rate = 1.5
    if hours <= normal_hours:
        salary_x = hours * working_pay * numberWorker
    else:
        salary_x = (((hours - normal_hours) * (working_pay * overtime_rate)) + (
                normal_hours * working_pay)) * numberWorker
    return salary_x


while payCode != -1:
    payCode = int(input("enter code: "))
    if payCode >= 4 or payCode < -1:
        print("Invalid code ")
    elif payCode in previousData:
        print("The Salary Has Been Calculated")
    else:
        previousData.append(payCode)
        if payCode == 1:
            numberWorker = int(input("Enter number workers: "))
            salary = calculatePayMontlyWorker(numberWorker)
            print("Salary is", salary)
            print(calculatePayMontlyWorker(numberWorker))

        elif payCode == 2:
            numberWorker = int(input("Enter number worker: "))
            hours = int(input("Enter number of hours: "))
            salary = calculatePayHourlyWorker(numberWorker, hours)
            print("Salary is", salary)
        elif payCode == 3:
            numberworker = int(input("Enter number worker: "))
            amount = float(input("Enter amount of weekly sales: "))
            salary = (weeklyCommission + amount * (commissionRate / 100)) * numberworker
            print("Salary is", salary)
        totalSalary = totalSalary + salary

print("Total Salary Need To Pay: ", totalSalary)
print("--------------------------------------------")
print("Thank You MagicCopy Sdn. Bhd.")
print("--------------------------------------------")
