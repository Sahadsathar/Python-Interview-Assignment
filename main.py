from collections import Counter
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
uniq_names = [pref_names.split()[0] for pref_names in tweet_name]
times = Counter(uniq_names)

repeat = times.values()

for element in set(repeat):
    dupl = ([(key, value) for key, value in sorted(times.items()) if value == element])
    if len(dupl) > 1:
        for (key, value) in dupl:
            print (key,'',value)
    max_value = max(times.values())
    temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

    if temp_max_result != dupl:
        for (key,value) in temp_max_result:
            print (key,'',value)