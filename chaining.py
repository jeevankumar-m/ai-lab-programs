# Rule-Based Expert System
# Forward and Backward Chaining

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"flu"}, "drink_water")
]

# ---------- Forward Chaining ----------

facts = {"fever", "cough"}

print("FORWARD CHAINING")
print("Initial Facts:", facts)

changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            print("Rule Applied:", conditions, "->", conclusion)
            changed = True

print("Final Facts:", facts)


# ---------- Backward Chaining ----------

# Reset facts for independent backward chaining
facts = {"fever", "cough"}

def backward_chain(goal):
    if goal in facts:
        print(goal, "is a known fact.")
        return True

    for conditions, conclusion in rules:
        if conclusion == goal:
            print("Checking:", goal)

            if all(backward_chain(condition) for condition in conditions):
                print("Rule Proved:", conditions, "->", conclusion)
                return True

    return False


print("\nBACKWARD CHAINING")
goal = input("Enter goal: ")

if backward_chain(goal):
    print("Goal", goal, "is proved.")
else:
    print("Goal", goal, "cannot be proved.")