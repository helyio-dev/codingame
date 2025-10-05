import sys
import math

class Robot:
    def __init__(self, target, score, storage, expertise, is_me):
        self.target = target
        self.score = score
        self.storage = storage
        self.expertise = expertise
        self.is_me = is_me
        self.total_storage = sum(storage.values())
        self.sample_files = []

class Sample:
    def __init__(self, id, carried_by, health, costs):
        self.id = id
        self.carried_by = carried_by
        self.health = health
        self.costs = costs

    def get_missing_molecules(self, robot_storage):
        missing = {}
        for mol_type, cost in self.costs.items():
            needed = cost - robot_storage.get(mol_type, 0)
            if needed > 0:
                missing[mol_type] = needed
        return missing
        
    def get_total_cost(self):
        return sum(self.costs.values())
        
project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

while True:
    robots = []
    robot_data_me = None
    
    for i in range(2):
        inputs = input().split()
        target = inputs[0]
        score = int(inputs[2])
        
        storage = {
            'A': int(inputs[3]), 'B': int(inputs[4]), 'C': int(inputs[5]),
            'D': int(inputs[6]), 'E': int(inputs[7])
        }
        expertise = {
            'A': int(inputs[8]), 'B': int(inputs[9]), 'C': int(inputs[10]),
            'D': int(inputs[11]), 'E': int(inputs[12])
        }
        
        robot = Robot(target, score, storage, expertise, is_me=(i==0))
        robots.append(robot)
        if i == 0:
            robot_data_me = robot

    available_A, available_B, available_C, available_D, available_E = [int(i) for i in input().split()]
    
    samples_in_game = []
    sample_count = int(input())
    for i in range(sample_count):
        inputs = input().split()
        sample_id = int(inputs[0])
        carried_by = int(inputs[1])
        rank = int(inputs[2])
        expertise_gain = inputs[3]
        health = int(inputs[4])
        cost_a = int(inputs[5])
        cost_b = int(inputs[6])
        cost_c = int(inputs[7])
        cost_d = int(inputs[8])
        cost_e = int(inputs[9])
        
        costs = {'A': cost_a, 'B': cost_b, 'C': cost_c, 'D': cost_d, 'E': cost_e}
        sample = Sample(sample_id, carried_by, health, costs)
        samples_in_game.append(sample)
        
        if carried_by == 0:
            robot_data_me.sample_files.append(sample)

    my_target = robot_data_me.target
    my_samples = robot_data_me.sample_files
    my_storage = robot_data_me.storage
    my_total_storage = robot_data_me.total_storage
    
    validatable_samples = []
    for sample in my_samples:
        missing = sample.get_missing_molecules(my_storage)
        if not missing:
            validatable_samples.append(sample)
            
    if validatable_samples:
        best_sample_to_connect = max(validatable_samples, key=lambda s: s.health)
        
        if my_target == "LABORATORY":
            print(f"CONNECT {best_sample_to_connect.id}")
            continue
        else:
            print("GOTO LABORATORY")
            continue

    cloud_samples = [s for s in samples_in_game if s.carried_by == -1]
    
    if len(my_samples) < 3 and cloud_samples:
        best_cloud_sample = max(cloud_samples, key=lambda s: s.health)
        
        if my_target == "DIAGNOSIS":
            print(f"CONNECT {best_cloud_sample.id}")
            continue
        else:
            print("GOTO DIAGNOSIS")
            continue

    needed_molecules = {}
    for sample in my_samples:
        missing = sample.get_missing_molecules(my_storage)
        for mol_type, count in missing.items():
            needed_molecules[mol_type] = needed_molecules.get(mol_type, 0) + count

    if needed_molecules and my_total_storage < 10:
        mol_type_to_get = max(needed_molecules, key=needed_molecules.get)
        
        if my_target == "MOLECULES":
            print(f"CONNECT {mol_type_to_get}")
            continue
        else:
            print("GOTO MOLECULES")
            continue

    print("GOTO DIAGNOSIS")