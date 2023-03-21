import numpy as np

class AES_Encrypt:
    def __init__(self, message, Key):
        self.message = message
        self.Key = Key
        self.sbox = [
                        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
                        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
                        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
                        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
                        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
                        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
                        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
                        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
                        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
                        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
                        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
                        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
                        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
                        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
                        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
                        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
                    ]
                
        self.r_con = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
    
    def get_state(self,s):
        k = len(s)%16
        if k == 0:
            k = 16
        res = s + (16 - k)*'{'

        msg = []

        for i in range(0,len(res),16):
            temp = res[i:i+16]
            msg.append(temp)

        message_np = np.array(msg)
        msg = []

        for i in range(len(message_np)):
            temp = list(message_np[i])
            temp = np.array(temp)
            temp = np.reshape(temp, (4,4))
            temp = np.transpose(temp)
            msg.append(temp)
        

        message_np = np.array(msg)

        return message_np

    
    def get_hex(self,msg_np):
        h = []
        statearray = [[0 for x in range(4)] for x in range(4)]
        h_msg_np = np.empty_like(msg_np) 
        for i in range(len(msg_np)):
            for j in range(len(msg_np[i])):
                for k in range(len(msg_np[i][j])):
                    m = hex(ord(msg_np[i][j][k]))
                    statearray[j][k] = m
            h.append(statearray)
            statearray = [[0 for x in range(4)] for x in range(4)]

        h = np.array(h)
        return h

    
    def rotateArray(self, arr, n, d):
        temp = []
        i = 0
        while (i < d):
            temp.append(arr[i])
            i = i + 1
        i = 0
        while (d < n):
            arr[i] = arr[d]
            i = i + 1
            d = d + 1
        arr[:] = arr[: i] + temp
        return arr
    
    def get_val(self,s):
        s_box = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

        for i in s_box:
            if i == s:
                return s_box[i]
        
    
    def get_s_box(self,l):
        k = l[2:]
        
        if (len(k) == 1):
            x = 0
            y = self.get_val(k)
        else:  
            x = self.get_val(k[0])
            y = self.get_val(k[1])

        return hex(self.sbox[x][y])

    
    def get_g_func(self,w3, round):
        w3 = self.rotateArray(w3, len(w3), 1)

        for i in range(len(w3)):
            w3[i] = self.get_s_box(w3[i])
        
        try:
            w3[0] = hex(int(w3[0],16) ^ self.r_con[round-1])
        except ValueError:
            pass

        return w3

    
    def get_xor(self, l1, l2):
        x = []
        for j in range(len(l1)):
                x.append(hex(int(l1[j], 16) ^ int(l2[j], 16)))
        return x
    
    def subBytes(self,state):
        ST = [[] for i in range(len(state))]
        temp = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    temp.append(self.get_s_box(state[i][j][k]))
                ST[i].append(temp)
                temp = []

        return np.array(ST)
    
    def shiftRows(self, state):
        ST = [[]]
        temp = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                k = list(state[i][j])
                k = self.rotateArray(k, len(k), j)
                ST[0].append(k)
        
        ST = np.array(ST)
        ST = np.reshape(ST, (len(state), 4, 4))
        return ST

    
    def galoisMult(self, a, b):
        p = 0
        hiBitSet = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256


    def mix_column(self, column):
        temp = column.copy()
        for i in range(len(temp)):
            temp[i] = int(temp[i], 16)

        column[0] = self.galoisMult(temp[0],2) ^ self.galoisMult(temp[3],1) ^ \
                    self.galoisMult(temp[2],1) ^ self.galoisMult(temp[1],3)
        column[1] = self.galoisMult(temp[1],2) ^ self.galoisMult(temp[0],1) ^ \
                    self.galoisMult(temp[3],1) ^ self.galoisMult(temp[2],3)
        column[2] = self.galoisMult(temp[2],2) ^ self.galoisMult(temp[1],1) ^ \
                    self.galoisMult(temp[0],1) ^ self.galoisMult(temp[3],3)
        column[3] = self.galoisMult(temp[3],2) ^ self.galoisMult(temp[2],1) ^ \
                self.galoisMult(temp[1],1) ^ self.galoisMult(temp[0],3)
        
        return column
    
    def Mixcolumns(self,state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                temp = self.mix_column(list(state[i][:,j]))
                for p in range(len(temp)):
                    temp[p] = hex(int(temp[p]))

                state[i][:,j] = np.array(temp)
        return state
    

    def get_key(self, state, key, round):
        W = []
        w = []
        next_round_key = []
        nrk = []
        for i in range(len(key)):
            for j in range(len(key[i])):
                w.append(list(key[i][j]))
            W.append(w)
            w = []

        for i in range(len(W)):
            w_3 = W[i][3].copy()
            g_w_3 = self.get_g_func(w_3, round)
        
            for j in range(len(g_w_3)):
                w.append(hex(int(W[i][0][j], 16) ^ int(g_w_3[j], 16)))


            w4 = w
            w5 = self.get_xor(w4, W[i][1])
            w6 = self.get_xor(w5, W[i][2])
            w7 = self.get_xor(w6, W[i][3])

            nrk.append(w4)
            nrk.append(w5)
            nrk.append(w6)
            nrk.append(w7)

            next_round_key.append(nrk)
            nrk = []

        return next_round_key
    
    def add_round_key(self, state, roundKey):
        res = [[] for i in range(len(state))]
        temp = []

        for i in range(len(state)):
            for j in range(len(state[i])):
                for k in range(len(state[i][j])):
                    temp.append(hex(int(state[i][j][k], 16) ^ int(roundKey[0][j][k], 16)))
                res[i].append(temp)
                temp = []

        res = np.array(res)
        return res   


    def encrypt(self):
        state = self.get_state(self.message)
        state = self.get_hex(state)
        key_state = self.get_state(self.Key)
        key = self.get_hex(key_state)

        state = self.add_round_key(state, key)

        

        for i in range(9):
            # print(f"====== Round {i+1} ======")
            state = self.subBytes(state)
            state = self.shiftRows(state)
            state = self.Mixcolumns(state)
            key = self.get_key(state, key, i+1)
            state = self.add_round_key(state, key)
        
        state = self.subBytes(state)
        state = self.shiftRows(state)
        key = self.get_key(state, key, i+1)
        state = self.add_round_key(state, key)

        return state 

msg = input("Enter the text to be encrypted: ")
Key = input("Enter the secret key: ")

if (len(Key) != 16):
    while (len(Key) != 16):
        print("As the Key size is 128 bits the secret key should be 16 characters long")
        Key = input("Enter the secret key: ")


aes = AES_Encrypt(msg, Key)
final = aes.encrypt()

s = ''
for i in range(len(final)):
    for j in range(len(final[i])):
        for k in range(len(final[i][j])):
            h_temp = final[i][j][k][2:]
            s += h_temp


print("\nThe encrypted text is: ", s)
