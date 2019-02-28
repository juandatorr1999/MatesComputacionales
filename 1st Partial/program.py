#
# def initialize_automata(m,alphabet):
#     automata=[]
#     dictionary={}
#     for i in range(0,m):
#         for a in alphabet:
#             dictionary[letter]=0
#         automata.append(dictionary)
#         dictionary={}
#     return automata
#
# def transition_function(p,alphabet):
#     m=len(p)
#     automata=initialize_automata(m,alphabet)
#     for q in range(0,m):
#         for a in alphabet:
#             k=min(m+1,q+2)
#             pqa=p[0:q]+a
#             pqa_length=len(pqa)
#             while true:
#                 k=k-1
#                 if ((k>=1 and k<=m+1)and (p[0:k]!=pqa[pqa_length-k:pqa_length+1])):
#                     break
#             automata[q][a]=k
#     return automata
#
# def automata_matcher(T,automata,m):
#     T_length=len(T)
#     counter=0
#     for i in range(1,T_length):
#         q=automata[q][T[i]]
#         if q==m:
#             counter=counter+1
#
#     return counter
#
# def main():
#     alphabet=input()
#     p=input()
#     T=input()
#     alphabet=list(alphabet)
#     automata=automata_matcher(p,alphabet)
#     print(automata);
#     print(automata_matcher(T,automata,len(p)))
#
# main()
# your code goes here
def initialize_automata(m,alphabet):
    automata=[]
    dictionary={}
    for i in range(0,m+1):
        for a in alphabet:
            dictionary[letter]=0
        automata.append(dictionary)
        dictionary={}
    return automata

def transition_function(p,alphabet):
    m=len(p)
    automata=initialize_automata(m,alphabet)

    for q in range(0,m+1):
        for a in alphabet:
            k=min(m+1,q+2)
            pqa=p[0:q]+a
            pqa_length=len(pqa)
            while true:
                k=k-1
                if ((k>=1 and k<=m+1)and (p[0:k]!=pqa[pqa_length-k:pqa_length+1])):
                    break
            automata[q][a]=k
    return automata

def automata_matcher(T,automata,m):
    T_length=len(T)
    counter=0
    for i in T:
        q=automata[q][i]
        if q==m:
            counter=counter+1
    return counter

def main():
    alphabet=input()
    p=input()
    T=input()
    p_length=len(p)
    alphabet=list(alphabet)
    automata=automata_matcher(p,alphabet)
    print(automata);
    print(automata_matcher(T,automata,p_length)

main()
