
def getMessageStatus(timestamps, messages, k):
    last_msg_time = dict()
    n = len(timestamps)

    state_result = []

    for i in range(n):
        curr_time = timestamps[i]
        curr_msg = messages[i]
        if curr_msg in last_msg_time:
            prev_time = last_msg_time[curr_msg]
            if curr_time - prev_time <= k:
                state_result.append("false")
            else:
                state_result.append("true")
            last_msg_time[curr_msg] = curr_time
        else:
            last_msg_time[curr_msg] = curr_time
            state_result.append("true")
    
    return state_result

if __name__ == "__main__":
    # ans = getMessageStatus([1, 4, 5, 10, 11, 14], ["hello", "bye", "bye", "hello", "bye", "hello"], 5)
    ans = getMessageStatus([1, 1, 1, 11], ["message-2", "message-2", "message-3", "message-2"], 5)
    print(ans)