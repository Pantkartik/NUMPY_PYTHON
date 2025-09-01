'''
Aggregation function means to find the summary of data 

'''


# np.sum(array)  ----> adds all elements
# np.mean(array)  ----> returns means
# mp.min(array)     ----> minimum
# np.max(array)    ----> to find the max
# np.std(array)    ----->  to find the standard deviation
# np.var(array)    ----->  to find the variance


'''
Variance (विचरण): Data की values mean से कितनी दूर-दूर हैं, इसका average है variance. जितनी ज्यादा values mean से दूर होंगी, variance उतना बढ़ जाएगा.

Standard Deviation (प्रमाण विचलन): Variance का square root है standard deviation. यह सीधे बताता है कि data की हर value औसत से कितनी दूर होती है. अगर standard deviation कम है, तो values mean के आसपास हैं; अगर ज्यादा है, तो values बिखरी हुई हैं.

'''

import numpy as np 

arr=np.array([10,20,30,40,50])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
