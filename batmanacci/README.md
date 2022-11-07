My attempt at the Batmanacci problem. The algorithm was rather simple to come up with, ironically the implementation was slightly more troublesome.

Honestly not the most optimal code for the algorithm, but it works. In short, since every word is the concatenation of the last two words, then:

The Kth letter of the Nth word, would also be the Kth letter of ( word_(N-2) + word_(N-1)). Meaning that depending on the length of word_(N-2), 
the Kth letter of the Nth word is either the Kth letter of the (N-2)th word or the (K-|word_(N-2)|)th letter of the (N-1)th word. The algorithm is simple
and based on the fundamental property of fibonacci. However, as addressed earlier, the code can definitely be improved.

