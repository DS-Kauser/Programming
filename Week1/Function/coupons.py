import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')                         # hepls in importing function from utility

# importing coupon_number function
from Utility.utility import gen_coupon_number                                           

if __name__ == '__main__':                                                          
    while True:                                                                     
        try:                                                                        
            # user-input for number of coupons required
            num_of_coupons = int(input("Enter number of coupons you need : "))      
            
            # passing argument in function
            coupons = gen_coupon_number(num_of_coupons)                                 
            print(coupons)
            break                                                                   
        
        except:
            print("Enter a valid input")                                            