from Nfa import Nfa

def prettyprint(word, nfa):
    print ('The word {} is {}'.format(word, "accepted" if nfa.accepts(word) else "rejected"))

def example1():
    alphabet = set(['a', 'b'])
    states = set(['p', 'q', 's', 'r'])
    initial_states = (['s'])
    accepting_states = (['r'])
    transitions = {
        ('s', 'b'): 's',
        ('s', 'a'): 'p',
        ('p', 'a'): 'p',
        ('p', 'b'): 'q',
        ('q', 'b'): 's',
        ('q', 'a'): 'r',
        ('r', 'a'): 'r',
        ('r', 'b'): 'r',
    };

    nfa = Nfa(alphabet, states, initial_states, accepting_states, transitions)
    prettyprint("bbabaaa", nfa)
    prettyprint("baabbbaaababbababb", nfa)
    prettyprint("bbbabb", nfa)

def example2(): 
    alphabet = set(['a', 'b'])
    states = set(['0', '1' '2'])
    initial_states = (['0'])
    accepting_states = (['0', '1'])
    transitions = {
        ('0', 'a'): '1',
        ('0', 'b'): '0',
        ('1', 'a'): '2',
        ('1', 'b'): '0',
        ('2', 'a'): '2',
        ('2', 'b'): '2',
    };

    nfa = Nfa(alphabet, states, initial_states, accepting_states, transitions)
    prettyprint("b", nfa)
    prettyprint("bbababbba", nfa)
    prettyprint("aa", nfa)


print ("\n\n******** Example 1 ********\n")
example1()

print ("\n\n******** Example 2 ********\n")
example2()