
def initialize_automata(m,alphabet):
    automata=[]
    dictionary={}
    for i in range(0,m+1):
        for a in alphabet:
            dictionary[a]=0
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
            while True:
                if (k>=1 and k<=m+1):
                    k=k-1
                if  (p[0:k]==pqa[pqa_length-k:pqa_length+1]):
                    break

            automata[q][a]=k
    return automata

def automata_matcher(T,automata,m):
    T_length=len(T)
    counter=0
    q=0
    for i in T:
        q=automata[q][i]
        if q==m:
            counter=counter+1
    return counter

def main():
    alphabet=input()
    p=input()
    T=input()
    alphabet=list(alphabet)
    automata=transition_function(p,alphabet)

    print(automata_matcher(T,automata,len(p)))

main()
