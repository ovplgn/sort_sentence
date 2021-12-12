if __name__=='__main__':
    sentence = "Keep calm and carry on"
def sort_sentence(sentence):
    output = sentence.lower().split()
    output.sort(key = len)
    output[0] = output[0].capitalize()
    return print(*output)
sort_sentence(sentence)
