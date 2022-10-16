from collections import defaultdict


# def best_sender(messages, senders):
#     message_sender_dict = defaultdict(int)
#     for s, m in zip(senders, messages):
#         if message_sender_dict[s] < len(m.split()):
#             message_sender_dict[s] = len(m.split())
#     list_result = [key for key, values in message_sender_dict.items() if values == message_sender_dict[sorted(message_sender_dict, key=lambda k: (message_sender_dict[k]))[-1]]]
#     return sorted(list_result)

def best_sender(messages, senders):
    message_sender_dict = defaultdict(int)
    for s, m in zip(senders, messages):
        if message_sender_dict[s] < len(m.split()):
            message_sender_dict[s] = len(m.split())
    return sorted(message_sender_dict, key=lambda k: (message_sender_dict[k], k))

messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
senders = ['Alice', 'userTwo', 'userThree', 'Alice']

print(best_sender(messages, senders))


