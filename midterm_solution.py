while True:
    project_title = input("Enter the project title: ")
    if project_title.lower() == 'system management':
        break 
    print("Invalid Project Title. Please try again.")

while True:
    group_name = input("Enter the group name: ")
    if group_name.lower() == 'squad goal':
        break  
    print("Invalid Group Name. Please try again.")

task_types = [
    {"task_name": "Research", "estimated_hours": 10},
    {"task_name": "Design", "estimated_hours": 8},
    {"task_name": "Development", "estimated_hours": 20},
    {"task_name": "Testing", "estimated_hours": 12},
]

print("Available task types:")
for names, task in enumerate(task_types, 1):
    print(f"{names}. {task['task_name']}")

assignments = []
for i in range(4):
    task_number = int(input(f"Enter the task number (1–4) for assignment {i+1} (0 to skip): "))
   
    if task_number == 0:
        assignments.append(None)
        continue

    if 1 <= task_number <= 5:
        task = task_types[task_number - 1]
        member_name = input(f"Enter the member's name for task {task_number} ({task['task_name']}): ")
        status = input("Enter the status (done or pending): ").lower()

        if status == "done":
            points = 2
        elif status == "pending":
            points = 1
        else:
            print("Invalid status! Assigning 0 points.")
            points = 0

        assignments.append({
            "task_number": task_number,
            "task_name": task["task_name"],
            "estimated_hours": task["estimated_hours"],
            "member_name": member_name,
            "status": status,
            "points": points
        })

total_points = 0
max_points = 0
for assignment in assignments:
    if assignment != str("None"):
        total_points += assignment["points"]
        max_points += 2

if max_points > 0:
    progress = (total_points / max_points) * 100
else:
    progress = 0

if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

print("--- Project Board ---")
print(f"Project Title: {project_title}")
print(f"Group Name: {group_name}")
print("Assigned Tasks:")

for i, assignment in enumerate(assignments, 1):
    if assignment != str("None"):
        print(f"  Task {i}:")
        print(f"  Task: {assignment['task_name']}")
        print(f"  Estimated Hours: {assignment['estimated_hours']}")
        print(f"  Member: {assignment['member_name']}")
        print(f"  Status: {assignment['status']}")
        print(f"  Points: {assignment['points']}")
    else:
        print(f"  Task {i}: No assignment")

print(f"Total Points Earned: {total_points}")
print(f"Maximum Possible Points: {max_points}")
print(f"Progress: {int(progress)}%")
print(f"Project Status: {project_status}")