#FreeCodeCamp - Introduction to python 
# VISUAL EXERCISE: Task Management System with Arrays

print("=" * 50)
print("TASK MANAGEMENT SYSTEM")
print("=" * 50)

# 01 Create an initial array of tasks
tasks = ["Study Python", "Exercise", "Read book"]
print("\nInitial tasks:")
for i, task in enumerate(tasks, 1):
    print(f"   {i}. {task}")

# 02 Add new tasks at the end
print("\nAdding new tasks...")
tasks.append("Go to supermarket")
tasks.append("Programming project")
print("   Tasks added successfully")

# 03 Show all current tasks
print("\nComplete task list:")
for i, task in enumerate(tasks, 1):
    print(f"   {i}. {task}")

# 04 Access specific elements
print("\nAccessing specific tasks:")
print(f"   First task: {tasks[0]}")
print(f"   Last task: {tasks[-1]}")
print(f"   Third task: {tasks[2]}")

# 05 Insert a task at a specific position
print("\nInserting priority task at position 2...")
tasks.insert(1, "URGENT Task")
print("   Task inserted")

# 06 Show current state
print("\nCurrent system state:")
print(f"   Total tasks: {len(tasks)}")
print("\n   Updated list:")
for i, task in enumerate(tasks, 1):
    print(f"   {i}. {task}")

# 07 Remove a completed task
print("\nCompleting first task...")
completed_task = tasks.pop(0)
print(f"   Completed: {completed_task}")

# 08 Final state
print("\nFINAL STATE:")
print(f"   Remaining tasks: {len(tasks)}")
for i, task in enumerate(tasks, 1):
    print(f"   {i}. {task}")

print("\n" + "=" * 50)
print("Exercise completed successfully!")
print("=" * 50)
