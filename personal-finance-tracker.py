balance = 0.0
history = []

def get_safe_float(prompt_text):
    while True:
        try :
            return float(input("prompt_text"))
        except ValueError:
            print("❌ Це не число! Будь ласка, введіть коректне число.")
    

def add_transaction(amount, description) :
        
    global balance
    balance += amount
    status =  "Дохд" if amount > 0 else "Витрата"
    #making pretty history change message        
    history.append(f"{status} : {description} на суму {abs(amount)} грн" )
    print("Транзакцію успішно додано")


def show_balance() :
        
        global balance
        print("Ваш баланс :", balance)


def show_history() :
        for i in history :
            print (i)


while True :
    print('''1 - Додати дохід\n2 — Додати витрату\n3 — Історія\n4 — Баланс\n5 — Вихід''')
    choice = int(input("Будь ласка, виберіть операцію"))
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
        
    
    
