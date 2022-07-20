def is_term_diffused_in_sequence(term: str, sequence: str) -> bool:
    seek_index = 0
    
    for character in term:
        seek_index = sequence.find(character, seek_index)
        if seek_index == -1:
            return False    
        seek_index += 1
    
    return True


term = input()
sequence = input()

term_diffused_in_sequence = is_term_diffused_in_sequence(term, sequence)

if term_diffused_in_sequence:
    print('Yes')
else:
    print('No')
 