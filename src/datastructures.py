class FamilyStructure:
    def __init__(self, last_name, members = []):
        self.last_name = last_name
        self._next_id = 1
        self._members = members

    # This method generates a unique 'id' when adding members into the list (you shouldn't touch this function)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['last_name'] = self.last_name
        self._members.append(member)
        ## You have to implement this method
        ## Append the member to the list of _members

    def delete_member(self, id):
        self._members = [member for member in self._members if member['id'] != id]
        return self._members


    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member

    def get_all_members(self):
        return self._members