# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


test_case = int (input("Enter the number of test cases "))
count = 0
tweet_name = []
while count < test_case:
    each_test_case = int(input("Enter the number of each test cases "))
    n = 0
    while each_test_case > n:
        tweet = (input("Enter user name and tweet id "))
        tweet_name.append(tweet)
        n += 1
    count += 1
print (tweet_name)
