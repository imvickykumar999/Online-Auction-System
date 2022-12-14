
# Answered Stackoverflow Question : https://stackoverflow.com/a/74836817/11493297

def JsonPrint(response, response_Keys):
    print('\n', response_Keys)
    print('---------------------------------\n')
    for i in range(len(response_Keys)):

        if type(response[response_Keys[i]]) == list:
            print('\n===========================', response_Keys[i])
            
            for j in range(len(response[response_Keys[i]])):
                if type(response[response_Keys[i]][j]) == dict:
                    JsonPrint(response[response_Keys[i]][j], list(response[response_Keys[i]][j].keys()))

        elif type(response[response_Keys[i]]) == dict:
            JsonPrint(response[response_Keys[i]], list(response[response_Keys[i]].keys()))

        else:
            print(response_Keys[i], ':')
            for j in range(len(response[response_Keys[i]].split('\n'))):
                print('\t', response[response_Keys[i]].split('\n')[j], '\n')
