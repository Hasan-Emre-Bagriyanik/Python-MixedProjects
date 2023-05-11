

import random
import time



class Control():
    def __init__(self,tv_state = "Closed",tv_sound = 0, tv_ChannelList = ["TRT"], tv_channel = "TRT"):
        
        self.tv_state = tv_state
        self.tv_sound = tv_sound
        self.tv_ChannelList = tv_ChannelList
        self.tv_Channel = tv_channel


    def tv_open(self):

        if(self.tv_state == "Open"):
            print("Already open...")
        else:
            print("TV turns on...")
            self.tv_state = "Open"


    def tv_Closed(self):

        if(self.tv_state == "Closed"):
            print("Already closed...")
        else:
            print("TV turns off...")
            self.tv_state = "Closed"


    def tv_sounda(self):

        while True:

            reply = input("Turn down the volume: '<'\nTurn up the volume: '>'\nOut: out" )


            if(reply == "<"):
                if(self.tv_sound != 0):
                    self.tv_sound -= 1
                    print("Volume: " ,self.tv_sound)

            elif(reply == ">"):
                if(self.tv_sound != 30):
                    self.tv_sound += 1
                    print("Volume: " ,self.tv_sound)

            else:
                print("The sound has been updated: ",self.tv_sound)
                break

    def add_channel(self,channel_name):
        print("Adding the channel...")
        time.sleep(1)

        self.tv_ChannelList.append(channel_name)

        print("The channel list has been update: ",self.tv_ChannelList)

    
    def random_channel(self):

        Random = random.randint(0,len(self.tv_ChannelList)-1)

        self.tv_Channel = self.tv_ChannelList[random]

        print("current channnel: " , self.tv_Channel)


    
    def __len__(self):
        return len(self.tv_ChannelList)


    def __str__(self):
        return ("tv_state: {}\ntv_sound: {}\ntv_channelList: {}\nCurrent_channel: {}\n".format(self.tv_state, self.tv_sound, self.tv_ChannelList, self.tv_Channel))


control = Control()


print("""

    TV APPLİCATİON (TELEVİZYON UYGULAMASI)

    1-TV Open

    2-TV Closed

    3-Sound Settings

    4-Add Channel

    5-Find out the number of channels

    6-Switch to random channel

    7-TV informations

    Press 'q' to log out...



""")


while True:

    process = input("Enter a process: ")


    if(process == "q"):
        print("Exiting the program...")
        break

    elif(process == '1'):
        control.tv_open()

    elif(process == "2"):
        control.tv_Closed()

    elif(process == "3"):
        control.tv_sounda()

    elif(process == "4"):

        channel_name = input("Enter channel names separated by ',': ")

        channel_list = channel_name.split(",")

        for adding in channel_list:
            control.add_channel(adding)


    elif(process == "5"):
        print("Channel list: ",len(control))

    elif(process == "6"):
        control.random_channel()

    elif(process == "7"):
        print(control)

    else:
        print("you have made an illegal transaction...")
        


                    



