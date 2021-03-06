import pandas as pd

def code_message():
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]

        except:
            print('unrecognized character')
            coded_char = '@@@'

        coded_message = coded_message + coded_char
    return coded_message


def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]
        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word

encryptionkey = pd.read_csv(r"backend/decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

message = 'hi my name is smit'
print(f"your message : {message}")

message_split = split(message)

coded_message = code_message()
print('Your encoded message:',code_message())

coded_message_str = str(coded_message)
print('Your decoded message:', decode_message(coded_message_str))
