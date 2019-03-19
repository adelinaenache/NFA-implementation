from Nfa import Nfa

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
    print(nfa.match_word("bbabaaa"))
    print(nfa.match_word("baabbbaaababbababb"))
    print(nfa.match_word("bbbabb"))

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
    print(nfa.match_word("b"))
    print(nfa.match_word("bbababbba"))
    print(nfa.match_word("aa"))


print ("******** Example 1 ********")
example1()

print ("******** Example 2 ********")
example2()