from collections import Counter
test_case = int (input("Enter the number of test cases "))
count = 0
counting ={}
tweet_name = []
while count < test_case:
    each_test_case = int(input("Enter the number of each test cases "))
    n = 0
    while each_test_case > n:
        tweet = (input("Enter user name and tweet id "))
        tweet1 = tweet.split()
        tweet_name.append(tweet1)
        n += 1
    count += 1
print (tweet_name)
for i in tweet_name:
    counting_names = Counter(i)
print(counting_names)
repeat = counting_names.values()


