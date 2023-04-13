print(" ::Welcome to Secure Chatting Application::  ")
while(True):
    st= input("Enter your message: ")
    words = st.split(" ")
    # 1st way
    coding = input("Press '1' for coding & Press '0' for Decoding: ")
    if((coding=="1")):
        coding = True
    elif((coding=='0')):
        coding = False
    else:
        print("Invalid input.")

    # 2nd way short way (if else  condition)
    # coding = True if (coding=="1") else False if (coding=='0') else print("Invalid input.")


    if(coding==True):
        nwords = []
        for word in words:
            if(len(word)>=3):
                r1="asd"
                r2="jkl"
                stnew = r1 + word[1:] + word[0] + r2 
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
    else:
        nwords = []
        for word in words:
            if(len(word)>=3):
                stnew = word[3:-3]
                stnew = stnew[-1]+stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
