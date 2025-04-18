import json
with open("bank_data.json","r") as f:
    data=json.load(f)
    # print(data["customers"][0])
# Display a mini statement-style format for each customer:

# Show customer name

# For each account:

# Account number

# Account type

# Opening and closing balance

# List of transactions (date, description, amount, type)

# output format:
# Customer Name: Rajesh R
# Account Number: SB1234567890 (Savings)
# Opening Balance: 15000
# Closing Balance: 22000

# Transactions:
# [2025-03-02] Credit of 50000 for Salary Credit
# [2025-03-05] Debit of 8000 for Flipkart Purchase

# def bank_statement():
#     u=int(input("Enter user id: "))
#     print("Customer Name: ",data["customers"][u-1]["name"])
#     for i in data["customers"][u-1]["accounts"]:
#         print("Account Number: ",i["account_number"],f"({i["type"]})")
#         print("Opening Balance: ",i["opening_balance"])
#         print("Closing Balance: ",i["closing_balance"])
#         print("Transcations:")
#         for j in i["transactions"]:
#             print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")

# bank_statement()  

#  Think Before You Code:
# You already have the loop that prints all transactions. Now:

# Ask the user what kind of transactions they want: "credit", "debit", or "all".

# Inside your transaction loop:

# Check if the type of transaction matches the user's input.

# If yes, display it.

# If the user chose "all", show everything.

# ❓Things to consider:
# How will you get and store the user’s choice?

# What happens if the user types something unexpected?

# Do you want to allow "All" in uppercase or lowercase or both?

# Next Step (Step 3):
# 🧮 Filter transactions based on a specific date range

# You'll guide the user to:

# Enter a start date and end date

# Then display only the transactions that fall between those dates (inclusive)

# 📌 What you’ll focus on learning:
# Parsing and comparing dates in Python

# Using conditional checks (if) to filter by date range

# Making your output look clean and clear

def bank_statement():
    u=int(input("Enter user id: "))
    trans_type=input("Enter you want all transcation or credit or debit").lower()
    date_preference=(input("If you want specific transcation: Type Yes If you don't want Type NO")).lower()
    if date_preference=="yes":
        print("Date format: YYYY-MM-DD")
        start_date=(input("Enter the starting date: "))
        end_date=(input("Enter the ending date: "))
    print("Customer Name: ",data["customers"][u-1]["name"])
    for i in data["customers"][u-1]["accounts"]:
        print("Account Number: ",i["account_number"],f"({i["type"]})")
        print("Opening Balance: ",i["opening_balance"])
        print("Closing Balance: ",i["closing_balance"])
        print("Transcations:")
        count=0
        for j in i["transactions"]:
            
            if trans_type=="all":
               if date_preference=="yes":
                   if start_date<=j["date"] and end_date>=j["date"]:
                        
                        print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
                        count+=1
               else:
                   count+=1
                   print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
                   
              

            elif(trans_type=="credit"):
                    
                    if j["type"]=="credit":
                       if date_preference=="yes":
                           if start_date<=j["date"] and end_date>=j["date"]:
                                count+=1
                                print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
                       else:
                            count+=1
                            print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
                          
            elif(trans_type=="debit"):
                if j["type"]=="debit":
                   if date_preference=="yes":
                       if start_date<=j["date"] and end_date>=j["date"]:
                        count+=1
                        print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
                      
                   else:
                        count+=1
                        print(f"[{j["date"]}] {j["type"]} of {j["amount"]} for {j["description"]}")
            
        if count==0:
                    print("No transaction found")
        
                
                
            

                
bank_statement()  
                

                    
                       
                       
                          
                           
                      
                           

                       
                    
                

            
            




    
        
           
    