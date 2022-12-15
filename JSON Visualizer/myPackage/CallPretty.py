
def JsonPrint(response, response_Keys):
    print()
    print(response_Keys)
    for i in range(len(response_Keys)):

        if type(response[response_Keys[i]]) == dict:
            JsonPrint(response[response_Keys[i]], list(response[response_Keys[i]].keys()))

        elif type(response[response_Keys[i]]) == list:
            print()
            
            for j in range(len(response[response_Keys[i]])):
                if type(response[response_Keys[i]][j]) == dict:
                    JsonPrint(response[response_Keys[i]][j], list(response[response_Keys[i]][j].keys()))

        else:
            print(response_Keys[i], ':')
            for j in range(len(response[response_Keys[i]].split('\n'))):
                print('\t', response[response_Keys[i]].split('\n')[j])
