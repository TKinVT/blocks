import blocks_data

def phraser(search_term):
    # Declare the blocks we have available to use in spelling our search term
    #blocks = [blocks_data.a,blocks_data.b,blocks_data.c,blocks_data.d,blocks_data.e,blocks_data.f,blocks_data.g,blocks_data.h,blocks_data.i,blocks_data.j,blocks_data.k,blocks_data.l,blocks_data.m,blocks_data.n,blocks_data.o,blocks_data.p]
    blocks = [block for block in blocks_data.block_set]

    if len(search_term) < 1 or len(search_term) > len(blocks):
        return False, None

    search_term = search_term.replace(' ','').upper()

    if '<3' in search_term:
        search_term= search_term.replace('<3', '')
        search_term = [char for char in search_term]
        search_term.append('<3')
    else:
        search_term = [char for char in search_term]

    for char in search_term:
        if char not in set(blocks_data.all_faces):
            return False, None

    search_term = blocks_data.ordered_term(search_term)

    # Initialize this counting variable, which will keep our place while
    # running through the possibilities.
    letter_index = 0

    # Create a memory store, such that we can explore alternate paths when an
    # index value has mutliple possible blocsk.
    block_memories = {}

    # Let's start our search. Can we make 'search_term' with our blocks?
    #
    # This loop will contain a search algorithm, so we'll approach it one letter
    # at a time, using our counting variable (letter_index) to indicate the
    # loop's location within the search_term. The loop ends if the index becomes
    # greater than the search_term's lengh, indicating the search is successful,
    # or if the index becomes less than 0, indeicating all possibilities have
    # been tried unsuccessfully (more or less).
    #
    # In order to avoid an infinite loop, it's important to ensure that all
    # paths increment the index
    while letter_index < len(search_term) and letter_index > -1:

        # Declare empty list to store the blocks which have the index value we're
        # loooking for
        good_blocks = []

        # Check to see if this letter index has been searched before, and if
        # so, are there more possibilities or should we keept this train moving
        # back up the line?
        if letter_index in block_memories:

            # Use same good blocks as before, less our previous candidate
            good_blocks = block_memories[letter_index]['good_blocks']

            # Name object that is the previously used block
            previous_candidate = block_memories[letter_index]['block_used']

            # Put the previous candidate back in the mix
            blocks.append(previous_candidate)

            if len(good_blocks) == 0:
                del block_memories[letter_index]

        else:
            # Let's look at each block in our list of possible blocks
            for block in blocks:

                # If this index value is found on the block ...
                if search_term[letter_index] in block:
                    # We'll add it to our list of possible blocks
                    good_blocks.append(block)

        # If there were no matching blocks...
        if len(good_blocks) == 0:
            # Decrement the letter index by one
            letter_index = letter_index - 1

        # We have at least one matching block
        else:
            # Declare the block we'll use for our index value
            # There's always an index-zero
            block_of_use = good_blocks[0]

            # Take this block out of circulation so it doesn't get used twice
            blocks.remove(block_of_use)
            good_blocks.remove(block_of_use)

            # Record data to memory, in case we traverse this letter index again
            block_memories[letter_index] = {'block_used':block_of_use,'good_blocks':good_blocks, 'letter':search_term[letter_index]}

            letter_index = letter_index + 1

    if letter_index == -1:
        return False, ["butt","stuff"]
    else:
        block_result = []
        for memory in range(len(block_memories)):
            block_used = block_memories[memory]['block_used']
            block_letter = block_memories[memory]['letter']
            block_result.append((block_used, block_letter))
        for block in blocks:
            block_result.append((block, None))
        return True, block_result


if __name__ == '__main__':
    import sys
    print(phraser("test"))
