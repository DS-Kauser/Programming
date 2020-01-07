import sys
sys.path.append("/home/user/Desktop/BridgeLabz")
from Week2.Utility.utility import queue

#Suppose minimum bank balance is Rs.10000

def bank_counter():
    while True:
        try:
            num_of_people = int(input("Enter number of people in queue : "))
            bank_que = queue()
            for i in range(num_of_people):
                bank_que.enqueue(i)
            while bank_que.is_empty() is not True:
                file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/balance.txt'
                file_op = open(file_path, 'r')
                bal = int(file_op.readline().split()[0])
                file_op.close()
                
                print("\nWelcome")
                print("choose\n1. Deposite\n2. Withdrawal")
                option = int(input("Enter your choice : "))
                
                if option == 1:
                    dep_amount = int(input("Enter your amount : "))
                    if dep_amount >= 0:
                        file_op = open(file_path, 'w')
                        file_op.write("{0}".format(dep_amount+bal))
                        file_op.close()
                        bank_que.dequeue()
                        continue
                    print("Enter a valid amount")
                    continue

                if option == 2:
                    with_amount = int(input("Enter your withdrawal amount : "))
                    if with_amount >= 0:
                        min_bal = 10000
                        if bal-min_bal >= with_amount:
                            bal = bal - with_amount
                            file_op = open(file_path, 'w')
                            file_op.write('{0}'.format(bal))
                            file_op.close() 
                            bank_que.dequeue()
                            continue
                        print("Empty Balance")
                        break                  
                    print("Enter a valid amount")
                    continue
                
                print("\nChoose Wisely")
            break
        except:
            print("Enter valid input")

if __name__ == "__main__":
    bank_counter()    