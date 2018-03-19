# import mystuff
#
# # mystuff = {'apple': "I am Apples!"}
# # print(mystuff['apple'])
#
# mystuff.apple()
# print(mystuff.tangerine)

class myStuff(object):

    def __init__(self):
        self.tangerine = "And a thousand years between"

    def apple(self):
        print("I am a classy apple")

ms = myStuff()
ms.apple()
print(ms.tangerine)
