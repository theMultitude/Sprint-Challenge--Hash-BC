#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #add tickets to hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #grab first stop
    preceding_stop = hash_table_retrieve(hashtable, 'NONE')

    # Create the route array by linking preceding_stop with it's pair
    for i, nada in enumerate(route):
        route[i] = preceding_stop
        preceding_stop = hash_table_retrieve(hashtable, preceding_stop)

    return route
