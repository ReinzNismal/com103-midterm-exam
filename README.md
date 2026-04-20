#This program is a Project Milestone Tracker designed for academic squads to manage specific task allocations and calculate real-time project readiness based on completion status and estimated effort.
##What the Program Does
Validates Identity: It requires a specific Project Title ("System Management") and Group Name ("Squad Goal") before proceeding, acting as a simple access control.
#Defines Task Scope: 
It categorizes work into four core areas (Research, Design, Development, Testing), each with predefined estimated hours to reflect workload.
#Tracks Assignments: 
It records four distinct assignments, capturing the member's name, the task selected, and the current progress status.
#Quantifies Progress: 
It converts qualitative status into quantitative data:
#Done: 
2 Points
#Pending: 
1 Point
#Determines Readiness: 
It calculates the total completion percentage and categorizes the project status into three tiers: Project Ready, On Track, or Needs More Work.
##How to Run It
#To execute this Python script, follow these steps:
#Prepare the Environment: 
Ensure you have Python installed. Save the script as a .py file and run it via your terminal or IDE.
#Authentication Phase: 
Enter "System Management" when prompted for the title.
Enter "Squad Goal" when prompted for the group name.
#Input Data: 
For each of the four assignment slots:
#Task Selection: 
Enter a number (1–4) based on the menu, or 0 to skip that slot.
#Member Name: 
Assign a student to the task.
#Status: 
Type done or pending.
#View Output: 
The program generates a "Project Board" summary including a detailed breakdown of each task, point totals, and the final percentage-based status report.