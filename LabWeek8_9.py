# Name: Ganesh Kumar
# Date: 04/04/2025
# Instructor: Professor Andres Calle
# Week 8 & 9 Lab
# Part 1: Hash Table operations
# with detailed print statements and a method to print the table.
# Description:
# Overview
# You are developing a management system for a zoo to ensure that
# animals receive timely care and attention.
# The zoo has three types of care facilities with different care capacities:
# Basic, Advanced, and Intensive.
# To manage the animals effectively,
# you will implement a combination of hash tables and binary search trees (BST).
#
#
#
# Objectives
# Demonstrate proficiency in implementing hash tables for rapid animal lookups.
#
# Use BST structures for efficiently prioritizing animal care.
#
# Understand the benefits and limitations of different data structures.
#
#
#
# Part 1: Hash Table (Animal Lookup)
# Implement a hash table (dictionary insufficient)
# to store and quickly access animals by their unique names. Each animal will have:
#
# Name (string, unique identifier)
#
# Species (e.g., lion, penguin, elephant, etc.)
#
# Care Level (integer, initially set from 1-10)
#
# Your hash table should:
#
# Support insertion, deletion, and searching by animal name.
#
# Handle collisions through chaining or open addressing.
#
#
#
# Part 2: Binary Search Tree (Care Priority Management)
# Implement a binary search tree (BST) to prioritize animals based on their care level.
# Each node will store:
#
# Care Level (key)
#
# List of animals sharing the same care level
#
# Animals' care levels increase over time if they are not attended to, simulating the urgency of care.
#
# Your BST should:
#
# Support insertion of animals based on care level.
#
# Efficiently retrieve animals that urgently need attention within a care level range.
#
#
#
# Care Facilities:
# Basic Care: Can handle animals with care levels 1-3.
#
# Advanced: Handles animals with care levels 4-7.
#
# Intensive: Handles animals with care levels 8-10.
#
#
#
# Tasks
# Define Data Structures: Define your hash table and tree node classes clearly.
#
# Implement Hash Table Operations
#
# Implement Tree Operations
#
# Testing:
#
# Populate your structures with at least 10 sample animals.
#
# Demonstrate insertion, deletion, periodic care-level increases,
# and efficient retrieval of animals based on facility availability.
#
# Deliverables
# Your Python implementation (.py file).
#
# Hash Table with collision managment
#
# BST capable of managing animal care needs
# Demo

# Animal class.
class Animal:
    # Constructor function
    def __init__(self, animalName, speciesType, careLevel):
        self.key = animalName
        self.type = speciesType
        self.level = careLevel

    # Returning the animal name, species type, and care level.
    def __repr__(self):
        return f"Animal(name={self.key}, type={self.type}, care_level={self.level})"


# Hash table with attributes, capacity, loadAverage, and current size.
class AnimalHashTable:
    # Constructor function
    def __init__(self, capacity):
        self.capacity = capacity
        self.currSize = 0
        self.loadAverage = 0
        self.numCollisions = 0
        self.table = [None] * self.capacity
        self.deletedMarker = "DELETED"

    # Insert function inserts an animal tuple object into the hash table.
    def insert(self, animalName, speciesType, careLevel):
        print(f"Insert operation for Animal {animalName} with care level {careLevel}")
        # Create an animal object.
        animal = Animal(animalName, speciesType, careLevel)
        # Get the hash index by hashing the animal name.
        hashIndex = hash(animalName) % self.capacity
        # Save the hashIndex in originalIndex
        originalIndex = hashIndex
        print(f"Initial Hash Index: {hashIndex}")

        # Check to see if the entry is available.
        while self.table[hashIndex] is not None:
            # Replace the existing entry because the key matches and the entry already exists.
            # If it exists, we modify the entry.
            if self.table[hashIndex].key == animalName:
                print(f"Animal {animalName} already exists. Replacing existing entry.")
                # Storing animal object in the hash table.
                self.table[hashIndex] = animal
                return
            # If there is something else in the index, there is a collision.
            self.numCollisions += 1
            print(f"Collision occurred at index {hashIndex}. Trying next index.")
            # Probe the next index
            hashIndex = self.probe(hashIndex)
            # If hashed index is equal to original index, print that the hash table is full.
            if hashIndex == originalIndex:
                raise Exception("Hash Table is full")
            # If the slot is empty, insert the animal and increase the current size by 1.
            elif self.table[hashIndex] == None or self.table[hashIndex] == self.deletedMarker:
                print(f"Found empty or deleted slot at index {hashIndex}. Inserting animal here.")
                self.table[hashIndex] = animal
                self.currSize += 1
                self.loadAverage = (self.currSize / self.capacity)
                return

        print(f"No collision, inserting animal at index {hashIndex}")
        # This entry is available, now take the entry.
        self.table[hashIndex] = animal
        # Increase current size by 1.
        self.currSize += 1
        # Calculate the load average.
        self.loadAverage = (self.currSize / self.capacity)
        print(f"Animal {animalName} inserted at index {hashIndex}. Current load average: {self.loadAverage:.2f}")
        return

    # Search function searches through the hash table entries and returns the hash
    # table entry or raises an exception.
    def search(self, animalName):
        print(f"Search operation for Animal {animalName}.")
        # Get the hash index by hashing the animal name.
        hashIndex = hash(animalName) % self.capacity
        # Save the hashIndex in originalIndex
        originalIndex = hashIndex
        print(f"Initial Hash Index: {hashIndex}")

        # Start searching from the hashIndex and check to see if the hashTable entry
        # is not none and not deleted.
        while self.table[hashIndex] is not None and self.table[hashIndex] != self.deletedMarker:
            # Find the animal by going through the hash table and check the animalName.
            if self.table[hashIndex].key == animalName:
                print(f"Animal {animalName} found at index {hashIndex}.")
                # Returning the animal object that is stored in the index.
                return self.table[hashIndex]
            # If it is not found, we probe the next index.
            hashIndex = self.probe(hashIndex)
            # If the next index is the original index, we are raising an exception
            # that the animal is not found because we searched and came back to the original index.
            # We later raise an exception and return none.
            if hashIndex == originalIndex:
                raise Exception(f"Animal {animalName} not found.")
        print(f"Animal {animalName} not found.")
        return None

    # Delete function searches through the hash table entries and deletes the hash table entry
    # or raises an exception.
    def delete(self, animalName):
        print(f"Delete operation for Animal {animalName}.")
        # Get the hash index by hashing the animal name.
        hashIndex = hash(animalName) % self.capacity
        # Save the hashIndex in originalIndex
        originalIndex = hashIndex
        print(f"Initial Hash Index: {hashIndex}")

        # Start searching from the hashIndex and check to see if the hashTable entry
        # is not none.
        while self.table[hashIndex] is not None:
            # Find the animal by going through the hash table and check the animalName
            # and delete the entry.
            if self.table[hashIndex].key == animalName:
                # If the animal is found, we delete the entry.
                print(f"Animal {animalName} found at index {hashIndex}. Deleting entry.")
                # Delete the object by replacing it with the deleted marker.
                self.table[hashIndex] = self.deletedMarker
                return
            # If not, we probe the next index.
            hashIndex = self.probe(hashIndex)
            # If the next index is the original index, we are raising an exception
            # that the animal is not found because we searched and came back to the original index.
            # We later raise an exception and return.
            if hashIndex == originalIndex:
                raise Exception(f"Animal {animalName} not found.")
        print(f"Animal {animalName} not found.")
        return

    # Probe function
    def probe(self, hashIndex):
        return (hashIndex + 1) % self.capacity

    # loadAvg function
    def loadAvg(self):
        return self.loadAverage

    # Print the hash table contents.
    def print_table(self):
        print("Hash Table Contents:")
        for i, entry in enumerate(self.table):
            if entry is not None and entry != self.deletedMarker:
                print(f"Index {i}: {entry}")
        print("End of Hash Table Contents")


# Helper class for BST nodes to hold Animal and left/right children
class BSTNode:
    # Constructor function
    def __init__(self, careLevel):
        self.careLevel = careLevel
        self.left = None
        self.right = None
        self.animalsList = []  # List of animals with the same care level


# Part 2: Binary Search Tree operations with detailed print statements and a method to print the tree.
# Creating a BinarySearchTree class.
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # BSTInsertRecursive function
    def BSTInsertRecursive(self, node, animalName, careLevel):
        # If currNode is not none and careLevel is less than currNode care level,
        # go to the left subtree.
        if careLevel < node.careLevel:
            # If left subtree is None, then insert animal in the left subtree.
            if node.left is None:
                newNode = BSTNode(careLevel)
                newNode.animalsList.append(animalName)
                node.left = newNode
                print(f"Insert left Animal {animalName} with care level {careLevel}")
                return
            # Otherwise, call the BSTInsertRecursive function.
            else:
                self.BSTInsertRecursive(node.left, animalName, careLevel)
        # If currNode is not none and careLevel is greater than currNode care level,
        # go to the right subtree.
        elif careLevel > node.careLevel:
            if node.right is None:
                newNode = BSTNode(careLevel)
                newNode.animalsList.append(animalName)
                node.right = newNode
                print(f"Insert right Animal {animalName} with care level {careLevel}")
                return
            else:
                self.BSTInsertRecursive(node.right, animalName, careLevel)
        # Otherwise, modify the node.
        else:
            # If it is equal, then modify the node.
            node.animalsList.append(animalName)
            return

    # BSTInsert function
    def BSTInsert(self, animalName, careLevel):
        print(f"Performing Binary Search Tree Insert operation for Animal {animalName} with care level {careLevel}")
        # If root is none, then add the animal to the animalsList.
        if self.root is None:
            currNode = BSTNode(careLevel)
            currNode.animalsList.append(animalName)
            # Set the root to the current node.
            self.root = currNode
        # Otherwise, call the BSTInsertRecursive function.
        else:
            self.BSTInsertRecursive(self.root, animalName, careLevel)

    # BSTSearchRecursive function
    def BSTSearchRecursive(self, node, careLevel):
        # If node is set to none, then print that no animals are found.
        if node is None:
            print(f"No animals found at care level {careLevel}")
            return None

        # Print that animals are found at care level.
        if careLevel == node.careLevel:
            print(f"Found animals at care level {careLevel}: {node.animalsList}")
            return node.animalsList
        elif careLevel < node.careLevel:
            return self.BSTSearchRecursive(node.left, careLevel)
        else:
            return self.BSTSearchRecursive(node.right, careLevel)


    # BSTSearch function performs binary search tree search operations.
    def BSTSearch(self, careLevel):
        print(f"Performing Binary Search Tree Search operation for care level {careLevel}")
        return self.BSTSearchRecursive(self.root, careLevel)

    # BSTDelete function
    def BSTDelete(self, careLevel):
        self.BSTDeleteRecursive(self.root, careLevel)

    # BSTDeleteRecursive function
    def BSTDeleteRecursive(self, root, careLevel):
        # Base case: If the tree is empty, return root
        if root is None:
            return root

        # If the careLevel to be deleted is smaller than the root's careLevel, it lies in left subtree
        if careLevel < root.careLevel:
            root.left = self.BSTDeleteRecursive(root.left, careLevel)

        # If the careLevel to be deleted is larger than the root's careLevel, it lies in right subtree
        elif careLevel > root.careLevel:
            root.right = self.BSTDeleteRecursive(root.right, careLevel)

        # If the careLevel is the same as root's careLevel, then this is the node to be deleted
        else:
            # Case 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None

            # Case 2: Node has only one child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            else:
                # Get the inorder successor (smallest in the right subtree)
                min_node = self._min_value_node(root.right)

                # Copy the inorder successor's content to this node
                root.careLevel = min_node.careLevel
                root.animalsList = min_node.animalsList

                # Delete the inorder successor
                root.right = self.BSTDeleteRecursive(root.right, min_node.careLevel)

        return root

    # _min_value_node function
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Optional: A method to call delete on the root of the tree
    def delete_root(self, careLevel):
        self.root = self.delete(self.root, careLevel)

    # BSTinOrderSuc function
    def BSTinOrderSuc(self, node):
        currNode = node
        while currNode.left is not None:
            currNode = currNode.left
        return currNode

    # BSTinOrderSucPrint function
    def BSTinOrderSucPrint(self, node):
        currNode = node
        if (currNode != None):
            self.BSTinOrderSucPrint(node.left)
            print(f"{node.careLevel} {node.animalsList}")
            self.BSTinOrderSucPrint(node.right)

    # BSTIncreaseCareLevel function
    def BSTIncreaseCareLevel(self, animalName):
        print(f"Performing Binary Search Tree Increase Care Level operation for Animal {animalName}")
        self.BSTIncreaseCareLevelRecursive(self.root, animalName)

    # BSTIncreaseCareLevelRecursive function
    def BSTIncreaseCareLevelRecursive(self, node, animalName):
        if node is None:
            return
        for animal in node.animalsList:
            if animal.key == animalName:
                animal.level += 1
                self.BSTDelete(animal.key, node.animal.level)
                self.BSTInsert(animal.key, animal.type, animal.level)
                return
        self.BSTIncreaseCareLevelRecursive(node.left, animalName)
        self.BSTIncreaseCareLevelRecursive(node.right, animalName)

    # BSTDecreaseCareLevel function
    def BSTDecreaseCareLevel(self, animalName):
        print(f"Performing Binary Search Tree Decrease Care Level operation for Animal {animalName}")
        self._decreaseCareLevelHelper(self.root, animalName)

    # BSTDecreaseCareLevelRecursive function
    def BSTDecreaseCareLevelRecursive(self, node, animalName):
        if node is None:
            return
        for animal in node.animalsList:
            if animal.key == animalName:
                animal.level -= 1
                self.BSTDelete(animal.key, node.animal.level)
                self.BSTInsert(animal.key, animal.type, animal.level)
                return
        self.BSTDecreaseCareLevelRecursive(node.left, animalName)
        self.BSTDecreaseCareLevelRecursive(node.right, animalName)

    # Method to print the final Binary Search Tree in-order
    def print_tree(self):
        print("Final Binary Search Tree Contents:")
        print(self.BSTinOrderSucPrint(self.root))
        print("End of Binary Search Tree Contents")



# Example usage for testing:

# Create the hash table object.
# Set the capacity to a prime number greater than the size of the hash table.
ht = AnimalHashTable(capacity=53)

# Create the binary search tree object.
bst = BinarySearchTree()

# Insert animals into the BST and hash table with care levels
animals = [
    # Name, species type, care level
    ("Tiger", "mammal", 10),
    ("Deer", "mammal", 8),
    ("Lemur", "mammal", 3),
    ("Wallaby", "mammal", 1),
    ("Cheetah", "mammal", 7),
    ("Otter", "mammal", 4),
    ("Albino Monkey", "mammal", 2),
    ("Lion", "mammal", 8),
    ("Leech", "insect", 6),
    ("Leopard", "mammal", 5),
    ("Lynx", "mammal", 9),
    ("Ladybug", "insect", 2)
]

# Insert animals into the hash table
for i, (name, species, careLevel) in enumerate(animals):
    ht.insert(name, species, careLevel)  # Insert into hash table
    bst.BSTInsert(name, careLevel)  # Insert into BST

# Search for some animals in the hash table and BST
print(ht.search("Lion"))  # Search in hash table
bst.BSTSearch(2)  # Search in BST

# Delete animal from the hash table and BST
ht.delete("Lion")  # Delete from hash table
bst.BSTDelete(8)  # Delete from BST

# Search again for the deleted animal in the hash table and BST
print(ht.search("Lion"))  # Search in hash table after deletion
bst.BSTSearch(8)  # Search in BST after deletion

# Print the load average of the hash table
print("Load Average:", ht.loadAvg())

# Display the final hash table contents
ht.print_table()

# Print the final BST contents
bst.print_tree()
# Options 1 - 7
while True:
    print("Add new animal: Enter 1")
    print("Delete animal: Enter 2")
    print("Increase care level: Enter 3")
    print("Decrease care level: Enter 4")
    print("Display hash table: Enter 5")
    print("Display binary search tree: Enter 6")
    print("Exit: Enter 7")
    # Prompts the user to make a selection
    choice = int(input("Make a selection:"))
    # If the user enters an invalid input, print invalid selection.
    if choice < 1 or choice > 7:
        print("Invalid selection")
    # If the user enters 1, the program will ask the user to enter the name, species type,
    # and care level of the animal.
    elif choice == 1:
        animal_name = str(input("Please enter the name of the animal:"))
        species = str(input("Please enter the species type of the animal:"))
        careLevel = int(input("Please enter the care level of the animal:"))
        ht.insert(animal_name, species, careLevel)
        bst.BSTInsert(animal_name, careLevel)
    # If the user enters 2, the program will ask the user to enter the name of the animal to delete.
    elif choice == 2:
        animal_name = str(input("Please enter the name of the animal to delete:"))
        animal = ht.search(animal_name)
        # If animal is set to none, print that the animal is not found.
        if animal == None:
            print("Animal not found.")
        # Otherwise, delete the animal in the hash table and binary search tree.
        else:
            ht.delete(animal.key)
            bst.BSTDelete(animal.level)
    # If the user enters 3, the program will ask the user to enter the animal name and new care level,
    # and increase the care level.
    elif choice == 3:
        animal_name = str(input("Please enter the name of the animal:"))
        animal = ht.search(animal_name)
        if animal == None:
            print("Current care level", animal.level)
            currentcareLevel = int(input("Enter the new care level."))
            # If the level is less than the currentcareLevel, give an error.
            if animal.level < currentcareLevel:
                print("Error: New level ", currentcareLevel, "is less than current level.", animal.level)
            # Otherwise, delete the animal and the care level.
            else:
                ht.delete(animal.key)
                bst.BSTDelete(animal.level)
                ht.insert(animal.key, animal.type, animal.level)
                bst.BSTInsert(animal.key, animal.level)
    # If the user enters 4, the program will ask the user to enter the name
    # of the animal and the new care level,
    # and decrease the care level.
    elif choice == 4:
        animal_name = str(input("Please enter the name of the animal:"))
        animal = ht.search(animal_name)
        if animal == None:
            print("Current care level", animal.level)
            currentcareLevel = int(input("Enter the new care level."))
            if currentcareLevel < animal.level:
                print("New care level ", currentcareLevel, "is less than current level.", animal.level)
            else:
                ht.delete(animal.key)
                bst.BSTDelete(animal.level)
                ht.insert(animal.key, animal.type, animal.level)
                bst.BSTInsert(animal.key, animal.level)
    # If the user enters 5, it will display the hash table.
    elif choice == 5:
        ht.print_table()
    # If the user enters 6, it will display the binary search tree.
    elif choice == 6:
        bst.print_tree()
    # If the user enters 7, the program will terminate.
    else:
        print("Goodbye!")
        break

# Result:
# C:\AdvancedPython\ADVANCEDPYTHON-2025\.venv\Scripts\python.exe C:\AdvancedPython\ADVANCEDPYTHON-2025\Week8Lab-WithComments.py
# Insert operation for Animal Tiger with care level 10
# Initial Hash Index: 25
# No collision, inserting animal at index 25
# Animal Tiger inserted at index 25. Current load average: 0.02
# Performing Binary Search Tree Insert operation for Animal Tiger with care level 10
# Insert operation for Animal Deer with care level 8
# Initial Hash Index: 28
# No collision, inserting animal at index 28
# Animal Deer inserted at index 28. Current load average: 0.04
# Performing Binary Search Tree Insert operation for Animal Deer with care level 8
# Insert left Animal Deer with care level 8
# Insert operation for Animal Lemur with care level 3
# Initial Hash Index: 41
# No collision, inserting animal at index 41
# Animal Lemur inserted at index 41. Current load average: 0.06
# Performing Binary Search Tree Insert operation for Animal Lemur with care level 3
# Insert left Animal Lemur with care level 3
# Insert operation for Animal Wallaby with care level 1
# Initial Hash Index: 36
# No collision, inserting animal at index 36
# Animal Wallaby inserted at index 36. Current load average: 0.08
# Performing Binary Search Tree Insert operation for Animal Wallaby with care level 1
# Insert left Animal Wallaby with care level 1
# Insert operation for Animal Cheetah with care level 7
# Initial Hash Index: 24
# No collision, inserting animal at index 24
# Animal Cheetah inserted at index 24. Current load average: 0.09
# Performing Binary Search Tree Insert operation for Animal Cheetah with care level 7
# Insert right Animal Cheetah with care level 7
# Insert operation for Animal Otter with care level 4
# Initial Hash Index: 38
# No collision, inserting animal at index 38
# Animal Otter inserted at index 38. Current load average: 0.11
# Performing Binary Search Tree Insert operation for Animal Otter with care level 4
# Insert left Animal Otter with care level 4
# Insert operation for Animal Albino Monkey with care level 2
# Initial Hash Index: 27
# No collision, inserting animal at index 27
# Animal Albino Monkey inserted at index 27. Current load average: 0.13
# Performing Binary Search Tree Insert operation for Animal Albino Monkey with care level 2
# Insert right Animal Albino Monkey with care level 2
# Insert operation for Animal Lion with care level 8
# Initial Hash Index: 30
# No collision, inserting animal at index 30
# Animal Lion inserted at index 30. Current load average: 0.15
# Performing Binary Search Tree Insert operation for Animal Lion with care level 8
# Insert operation for Animal Leech with care level 6
# Initial Hash Index: 25
# Collision occurred at index 25. Trying next index.
# Found empty or deleted slot at index 26. Inserting animal here.
# Performing Binary Search Tree Insert operation for Animal Leech with care level 6
# Insert right Animal Leech with care level 6
# Insert operation for Animal Leopard with care level 5
# Initial Hash Index: 5
# No collision, inserting animal at index 5
# Animal Leopard inserted at index 5. Current load average: 0.19
# Performing Binary Search Tree Insert operation for Animal Leopard with care level 5
# Insert left Animal Leopard with care level 5
# Insert operation for Animal Lynx with care level 9
# Initial Hash Index: 29
# No collision, inserting animal at index 29
# Animal Lynx inserted at index 29. Current load average: 0.21
# Performing Binary Search Tree Insert operation for Animal Lynx with care level 9
# Insert right Animal Lynx with care level 9
# Insert operation for Animal Ladybug with care level 2
# Initial Hash Index: 21
# No collision, inserting animal at index 21
# Animal Ladybug inserted at index 21. Current load average: 0.23
# Performing Binary Search Tree Insert operation for Animal Ladybug with care level 2
# Search operation for Animal Lion.
# Initial Hash Index: 30
# Animal Lion found at index 30.
# Animal(name=Lion, type=mammal, care_level=8)
# Performing Binary Search Tree Search operation for care level 2
# Found animals at care level 2: ['Albino Monkey', 'Ladybug']
# Delete operation for Animal Lion.
# Initial Hash Index: 30
# Animal Lion found at index 30. Deleting entry.
# Search operation for Animal Lion.
# Initial Hash Index: 30
# Animal Lion not found.
# None
# Performing Binary Search Tree Search operation for care level 8
# No animals found at care level 8
# Load Average: 0.22641509433962265
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 21: Animal(name=Ladybug, type=insect, care_level=2)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 29: Animal(name=Lynx, type=mammal, care_level=9)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 2 ['Albino Monkey', 'Ladybug']
# 3 ['Lemur']
# 4 ['Otter']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 9 ['Lynx']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:1
# Please enter the name of the animal:Walrus
# Please enter the species type of the animal:mammal
# Please enter the care level of the animal:4
# Insert operation for Animal Walrus with care level 4
# Initial Hash Index: 16
# No collision, inserting animal at index 16
# Animal Walrus inserted at index 16. Current load average: 0.25
# Performing Binary Search Tree Insert operation for Animal Walrus with care level 4
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:1
# Please enter the name of the animal:Giraffe
# Please enter the species type of the animal:mammal
# Please enter the care level of the animal:8
# Insert operation for Animal Giraffe with care level 8
# Initial Hash Index: 15
# No collision, inserting animal at index 15
# Animal Giraffe inserted at index 15. Current load average: 0.26
# Performing Binary Search Tree Insert operation for Animal Giraffe with care level 8
# Insert right Animal Giraffe with care level 8
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 21: Animal(name=Ladybug, type=insect, care_level=2)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 29: Animal(name=Lynx, type=mammal, care_level=9)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 2 ['Albino Monkey', 'Ladybug']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 9 ['Lynx']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:2
# Please enter the name of the animal to delete:Lynx
# Search operation for Animal Lynx.
# Initial Hash Index: 29
# Animal Lynx found at index 29.
# Delete operation for Animal Lynx.
# Initial Hash Index: 29
# Animal Lynx found at index 29. Deleting entry.
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 21: Animal(name=Ladybug, type=insect, care_level=2)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 2 ['Albino Monkey', 'Ladybug']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:1
# Please enter the name of the animal:Slug
# Please enter the species type of the animal:gastropod mollusc
# Please enter the care level of the animal:9
# Insert operation for Animal Slug with care level 9
# Initial Hash Index: 15
# Collision occurred at index 15. Trying next index.
# Collision occurred at index 16. Trying next index.
# Found empty or deleted slot at index 17. Inserting animal here.
# Performing Binary Search Tree Insert operation for Animal Slug with care level 9
# Insert right Animal Slug with care level 9
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 17: Animal(name=Slug, type=gastropod mollusc, care_level=9)
# Index 21: Animal(name=Ladybug, type=insect, care_level=2)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 2 ['Albino Monkey', 'Ladybug']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 9 ['Slug']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:2
# Please enter the name of the animal to delete:Ladybug
# Search operation for Animal Ladybug.
# Initial Hash Index: 21
# Animal Ladybug found at index 21.
# Delete operation for Animal Ladybug.
# Initial Hash Index: 21
# Animal Ladybug found at index 21. Deleting entry.
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 17: Animal(name=Slug, type=gastropod mollusc, care_level=9)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 9 ['Slug']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:3
# Please enter the name of the animal:Walrus
# Search operation for Animal Walrus.
# Initial Hash Index: 16
# Animal Walrus found at index 16.
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 17: Animal(name=Slug, type=gastropod mollusc, care_level=9)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 9 ['Slug']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:4
# Please enter the name of the animal:Slug
# Search operation for Animal Slug.
# Initial Hash Index: 15
# Animal Slug found at index 17.
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:5
# Hash Table Contents:
# Index 5: Animal(name=Leopard, type=mammal, care_level=5)
# Index 15: Animal(name=Giraffe, type=mammal, care_level=8)
# Index 16: Animal(name=Walrus, type=mammal, care_level=4)
# Index 17: Animal(name=Slug, type=gastropod mollusc, care_level=9)
# Index 24: Animal(name=Cheetah, type=mammal, care_level=7)
# Index 25: Animal(name=Tiger, type=mammal, care_level=10)
# Index 26: Animal(name=Leech, type=insect, care_level=6)
# Index 27: Animal(name=Albino Monkey, type=mammal, care_level=2)
# Index 28: Animal(name=Deer, type=mammal, care_level=8)
# Index 36: Animal(name=Wallaby, type=mammal, care_level=1)
# Index 38: Animal(name=Otter, type=mammal, care_level=4)
# Index 41: Animal(name=Lemur, type=mammal, care_level=3)
# End of Hash Table Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:6
# Final Binary Search Tree Contents:
# 1 ['Wallaby']
# 3 ['Lemur']
# 4 ['Otter', 'Walrus']
# 5 ['Leopard']
# 6 ['Leech']
# 7 ['Cheetah']
# 8 ['Giraffe']
# 9 ['Slug']
# 10 ['Tiger']
# None
# End of Binary Search Tree Contents
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:11
# Invalid selection
# Add new animal: Enter 1
# Delete animal: Enter 2
# Increase care level: Enter 3
# Decrease care level: Enter 4
# Display hash table: Enter 5
# Display binary search tree: Enter 6
# Exit: Enter 7
# Make a selection:7
# Goodbye!
#
# Process finished with exit code 0