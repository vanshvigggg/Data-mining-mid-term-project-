from collections import defaultdict
from itertools import combinations

def BruteForceAssociation(dataset, min_support, min_confidence):
    item_list = list(dataset.columns)
    item_count = dict()

    for i, item in enumerate(item_list):
        item_count[item] = i + 1

    transaction_list = list()

    for index, record in dataset.iterrows():
        current_transaction = set()
        
        for key in item_count:
            if record[key] == 't':
                current_transaction.add(item_count[key])
        transaction_list.append(current_transaction)


    def get_support(transaction_list, item_set):
        match_count = 0
        for transaction in transaction_list:
            if item_set.issubset(transaction):
                match_count += 1
                
        return float(match_count/len(transaction_list))

    def self_join_candidates(frequent_item_sets_per_level, level):
        current_level_candidates = list()
        last_level_items = frequent_item_sets_per_level[level - 1]
        
        if len(last_level_items) == 0:
            return current_level_candidates
        
        for i in range(len(last_level_items)):
            for j in range(i+1, len(last_level_items)):
                itemset_i = last_level_items[i][0]
                itemset_j = last_level_items[j][0]
                union_set = itemset_i.union(itemset_j)
                
                if union_set not in current_level_candidates and len(union_set) == level:
                    current_level_candidates.append(union_set)
                    
        return current_level_candidates

    def get_single_drop_subsets(item_set):
        single_drop_subsets = list()
        for item in item_set:
            temp = item_set.copy()
            temp.remove(item)
            single_drop_subsets.append(temp)
            
        return single_drop_subsets

    def is_valid_set(item_set, prev_level_sets):
        single_drop_subsets = get_single_drop_subsets(item_set)
        
        for single_drop_set in single_drop_subsets:
            if single_drop_set not in prev_level_sets:
                return False
        return True

    def prune_candidates(frequent_item_sets_per_level, level, candidate_set): 
        post_pruning_set = list()
        if len(candidate_set) == 0:
            return post_pruning_set
        
        prev_level_sets = list()
        for item_set, _ in frequent_item_sets_per_level[level - 1]:
            prev_level_sets.append(item_set)
            
        for item_set in candidate_set:
            if is_valid_set(item_set, prev_level_sets):
                post_pruning_set.append(item_set)
                
        return post_pruning_set

    def get_frequent_itemsets(min_support):
        frequent_item_sets_per_level = defaultdict(list)
        print("level : 1", end = " ")
        
        for item in range(1, len(item_list) + 1):
            support = get_support(transaction_list, {item})
            if support >= min_support:
                frequent_item_sets_per_level[1].append(({item}, support))
            
        for level in range(2, len(item_list) + 1):
            print(level, end = " ")
            current_level_candidates = self_join_candidates(frequent_item_sets_per_level, level)

            post_pruning_candidates = prune_candidates(frequent_item_sets_per_level, level, current_level_candidates)
            if len(post_pruning_candidates) == 0:
                break

            for item_set in post_pruning_candidates:
                support = get_support(transaction_list, item_set)
                if support >= min_support:
                    frequent_item_sets_per_level[level].append((item_set, support))
                    
        return frequent_item_sets_per_level


    # # Entering the Minimum Support Value
    frequent_item_sets_per_level = get_frequent_itemsets(min_support)
    print("\n")

    # # The below code produces a dictionary called item_support_dict which from frequent_item_sets_per_level that maps items to their support values
    item_support_dict = dict()
    item_list = list()

    key_list = list(item_count.keys())
    val_list = list(item_count.values())

    for level in frequent_item_sets_per_level:
        for set_support_pair in frequent_item_sets_per_level[level]:
            for i in set_support_pair[0]:
                item_list.append(key_list[val_list.index(i)])
            item_support_dict[frozenset(item_list)] = set_support_pair[1]
            item_list = list()


    # # The find_subset function takes the item and item_length as parameter and it returns all the possible combinations of elements inside the items
    def subset_finder(item, item_length):
        combs = [list(combinations(item, i)) for i in range(1, item_length + 1)] 
        subsets = [elt for comb in combs for elt in comb]      
        return subsets


    # # This function generates the association rules in accordance withe the minimum confidence value and the provided dictionary of itemsets against their support values. It takes the mininmum confidence value and support_dict as a parameter, and returns rules as a list.
    def get_association_rules(min_confidence, support_dict):
        rules = []
        for item, support in support_dict.items():
            if len(item) > 1:
                subsets = subset_finder(item, len(item))
                for subset in subsets:
                    complement = item.difference(subset)
                    if complement:
                        subset = frozenset(subset)
                        rule = (subset, frozenset(complement), support_dict[frozenset(item)] / support)
                        if rule[2] >= min_confidence:
                            rules.append(rule)
        
        return rules

    return  get_association_rules(min_confidence, item_support_dict)


