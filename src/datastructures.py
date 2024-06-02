
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members =   [{'id': self._generateId(),
                          'first_name': 'John',
                          'last_name': self.last_name,
                          'age': 33,
                          'lucky_numbers': [7, 13, 22]},
                         {'id': self._generateId(),
                          'first_name': 'Jane',
                          'last_name': self.last_name,
                          'age': 35,
                          'lucky_numbers': [10, 14, 3]},
                         {'id': self._generateId(),
                          'first_name': 'Jimmy',
                          'last_name': self.last_name,
                          'age': 5,
                          'lucky_numbers': [1]}] # example list of members

    def _generateId(self):
        # read-only: Use this method to generate random members ID's when adding members into the list
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        print(member)
        pass

    def delete_member(self, deleted_id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]['id'] == deleted_id:
                del self._members[i]
                return self._members[i]
                break


    def get_member(self, id):
        # fill this method and update the return
        for row in self._members:
            if row['id'] == id:
                return row
    

    def get_all_members(self):
        # this method is done, it returns a list with all the family members
        return self._members
