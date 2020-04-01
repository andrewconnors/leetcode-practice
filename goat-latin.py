def toGoatLatin(self, S: str) -> str:
        #Setup vowels in a dict for constant time checking for keys
        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
        }
        split_sentance = S.split(' ')
        for i in range(len(split_sentance)):
            word = split_sentance[i]
            #Rules
            if str.lower(word[0]) in vowels:
                #Using join to keep this operation at O(M) where M is the length of the list of operations to join (3)
                word = ''.join([word, 'ma', 'a'*(i+1)])
            else:
                word = ''.join([word[1:], word[0], 'ma', 'a'*(i+1)])
            split_sentance[i] = word
        return ' '.join(split_sentance)


if __name__=='__main__':
    example_sentence = "The quick brown fox jumped over the lazy dog"
    print(toGoatLatin(example_sentence))
    '''
    Runtime analysis:
    I am operating on every element in the array therefore we have at least O(N). Inside the
    for loop, the join operation is the most costly. Because I am only performing that on 3 items each time, and the 
    array splitting on line 18 is constant, I am running in constant time inside the loop.
    One more O(N) operation at the bottom to join the words together and we have an O(N) solution. 
    '''