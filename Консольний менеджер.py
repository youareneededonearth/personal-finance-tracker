import os
balance = 0.0
history = []

def read_file():
    
    global balance, history
    
    if os.path.exists("history.txt"):
        print("Файл знайдено, завантажую дані...")
        with open("history.txt","r",encoding = "utf-8") as file:
            for line in file:
                line = line.replace("\n","")
                history.append(line)
                
                parts = line.split(" на суму ")
                amount_str = parts[1].replace("грн", "")
                amount = float(amount_str)
                if line.startswith("Витрата"):
                    amount = -amount
                balance += amount
                print("Початковий баланс відновлено:", balance)
                
    else:
        print("Файлу немає, починаємо з нуля")



def get_safe_float(prompt_text):
    while True:
        try :
            return float(input(prompt_text))
        except ValueError:
            print("❌ Це не число! Будь ласка, введіть коректне число.")


    
def add_transaction(amount, description) :
        
    global balance
    balance += amount
    status =  "Дохд" if amount > 0 else "Витрата"
    record= f"{status} : {description} на суму {abs(amount)} грн"
    history.append(record)
    
    with open("history.txt", "a", encoding="utf-8") as file :
        file.write(record + "\n")
        print("Транзакцію успішно додано та записано у файл")


    
def show_balance() :
       
        global balance
        
        print("Ваш баланс :", balance)



def show_history() :
        for i in history :
            print (i)


def clear_history():
    global balance,history
    balance = 0.0
    history = []
    






read_file()



while True :
    print("1 - Додати дохід\n2 — Додати витрату\n3 — Історія\n4 — Баланс\n5 — Вихід")
    
    choice = get_safe_float("Будь ласка, виберіть операцію")
    if choice == 1 :
        amount = get_safe_float("Будь ласка, введіть дохід")
        description = input("Будь ласка, додайте опис транзакції")
        add_transaction(amount, description)
    elif choice == 2 :
        amount = get_safe_float("Будь ласка, введіть витрату")
        amount = - amount
        description = input("Будь ласка, додайте опис транзакції")
        add_transaction(amount, description)
    elif choice == 3 :
        show_history()
    elif choice == 4 :
        show_balance()
    elif choice == 5 :
        break
    elif choice == 6 :
        clear_history()
        
    
    
