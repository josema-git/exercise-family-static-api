class FamilyStructure:
    def __init__(self, last_name, members = None):
        self.last_name = last_name
        self._next_id = 1
        self._members = members if members is not None else []

    # This method generates a unique 'id' when adding members into the list (you shouldn't touch this function)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['last_name'] = self.last_name
        for existing_member in self._members:
            if existing_member['id'] == member['id']:
                raise ValueError(f"Member with id {member['id']} already exists.")
            
        if 'id' not in member or member['id'] == None:
            member['id'] = self._generate_id()
        self._members.append(member)


    def delete_member(self, id):
        self._members = [member for member in self._members if member['id'] != id]
        return self._members


    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member

    def get_all_members(self):
        return self._members