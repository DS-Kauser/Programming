import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')             # helps in importing function from utility

# importing show_array from utility
from Utility.utility import show_array                                  

if __name__ == '__main__':                                              
    
    while True:                                                         
        try:
            # taking user-input for rows and columns                                                            
            row = int(input("Enter number of rows : "))                 
            col = int(input("Enter number of columns : "))              
            
            # passing the argument in show_array function
            array2D = show_array(row,col)                               
            print(array2D)                                      
            break                                                       

        except:
            print("Enter Valid Input")                                  