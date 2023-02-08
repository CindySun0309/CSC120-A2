Use this file to record your reflection on this assignment. 

What worked, what didn't, what advice would you give someone taking this course in the future?

My code can run successfully minimally, with all meeting all requirments. However, it is not a "smart" program because it requires people (who know how to code) to manually enter all directions in def main(). An outsider (someone who do not know coding) would be unable to use the program. I tried to make the program accessable to everyone by using the input function, but it did not work. And I do not know why. Therefore, when adding a computer to the inventory, the person can only manually type code like the one below:

c1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64, "macOS Big Sur", 2013, 1500)

Also, if any of a computer's attributes do not meet the following requirement:

description: str
processor_type: str
hard_drive_capacity: int
memory: int
operating_system: str
year_made: int
price: int

Such as typing the code below in def main():

c3 = Computer("Something", "?", "no idea", "Great", "OK", "Nice", "Any")

The computer would be unable to store into the inventory. I tried to fix this problem by using if statement in the Computer class, but it did not work. 


Advice for future students: Please study class function before taking the course. Or if you were like me (who had intro class a year ago and already forgot everything about computer science, try to find an online tutorial/video before taking the course to help you prepare for the class.)