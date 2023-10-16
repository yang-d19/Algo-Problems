db = {}

payment_cnt = 0

class Account:
    def __init__(self, timestamp, accountID, amount):
        self.timestamp = timestamp
        self.accountID = accountID
        self.amount = amount
        self.outgoing = 0

class Payment:
    def __init__(self, timestamp, accountID, amount) -> None:
        self.timestamp = timestamp
        self.accountID = accountID
        self.amount = amount

payments = {}
    
def create(timestamp, accountID):
    if db.get(accountID) != None:
        return "false"
    new_account = Account(timestamp, accountID, 0)
    db[accountID] = new_account
    return "true"

def deposit(timestamp, accountID, amount):
    if db.get(accountID) == None:
        return ""
    account = db[accountID]
    account.amount += amount
    db[accountID] = account
    return str(account.amount)

def transfer(timestamp, accountID_from, accountID_to, amount):
    if accountID_from == accountID_to:
        return ""
    if db.get(accountID_from) == None or db.get(accountID_to) == None:
        return ""
    account_from = db[accountID_from]
    account_to = db[accountID_to]
    if account_from.amount < amount:
        return ""
    
    account_from.amount -= amount
    account_from.outgoing += amount

    account_to.amount += amount

    db[accountID_from] = account_from
    db[accountID_to] = account_to

    return str(account_from.amount)

def schedule_payment(timestamp, accountID, amount, delay, cnt):
    if db.get(accountID) == None:
        return ""

    pm_s = f"payment{cnt}"

    expect_ts = timestamp + delay
    payments[pm_s] = Payment(expect_ts, accountID, amount)

    return pm_s

def top_spenders(timestamp, number):
    sorted_dict = {
        k: v for k, v in sorted( 
            db.items(), 
            key=lambda item: (-item[1].outgoing, item[1].accountID) 
            )
    }

    cnt = 0
    ss = ""
    for accountID, account in sorted_dict.items():
        cnt += 1
        if cnt > number:
            break
        if ss != "":
            ss += ", "
        ss += f"{accountID}({account.outgoing})"
    return ss

def solution(queries):

    ans_list = []

    ycnt = 0

    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            ans_list.append(create(query[1], query[2]))
        elif query[0] == "DEPOSIT":
            ans_list.append(deposit(query[1], query[2], int(query[3])))
        elif query[0] == "TRANSFER":
            ans_list.append(transfer(query[1], query[2], query[3], int(query[4])))
        elif query[0] == "TOP_SPENDERS":
            ans_list.append(top_spenders(query[1], int(query[2])))
        elif query[0] == "SCHEDULE_PAYMENT":
            ycnt += 1
            ans_list.append(schedule_payment(int(query[1]), query[2], int(query[3]), int(query[4]), ycnt))
    
    return ans_list

queries = [
  ["CREATE_ACCOUNT", "1", "account1"],
  ["CREATE_ACCOUNT", "2", "account2"],
  ["CREATE_ACCOUNT", "3", "account3"],
  ["DEPOSIT", "4", "account1", "1000"],
  ["DEPOSIT", "5", "account2", "1000"],
  ["DEPOSIT", "6", "account3", "1000"],
  ["SCHEDULE_PAYMENT", "7", "account1", "300", "10"],
  ["SCHEDULE_PAYMENT", "8", "account2", "400", "10"],
  ["TOP_SPENDERS", "15", "3"],
  ["TOP_SPENDERS", "20", "3"]
]
print(solution(queries))