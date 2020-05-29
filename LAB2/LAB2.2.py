def packet_size(packet):
    '''
    (list) -> int
    takes in list and returns the length of the list
    '''
    return len(packet)
def error_indices(packet1, packet2):
    '''
    (list, list) -> list
    takes two lists as inputs and outputs a list with indices of which indices were different in the two input lists
    '''
    q = []
    for i in range(0, len(packet1)):
        if packet1[i] != packet2[i]:
            q.append(i)
    return q

def packet_diff(packet1, packet2):
    '''
    (list, list) -> int
    takes two list inputs and outputs the amount of differences there are as an integer
    '''
    q = 0
    for i in range(0, len(packet1)):
        if packet1[i] != packet2[i]:
            q += 1
    return q

if __name__ == "__main__":
    # test your bit error rate detector here
    packet_sent = [0, 1, 1, 1]
    packet_received = [1, 1, 1, 1]
    print(packet_size([0, 1, 0, 1]))
    print(error_indices([0, 1, 1, 1], [0, 1, 1, 1]))
    print(packet_diff([1, 1, 0, 0], [0, 1, 1, 0]))