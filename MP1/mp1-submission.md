<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 5:15:50 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.23.37add_code.png.webp?alt=media&token=f5224f90-3453-49ca-8426-20bf33845745"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code: First step is to add current datetime value to update last Activity.<br>Later we check conditions for each value and only if it matches the<br>type of data we allow to append to the main task. Else it<br>prints error messages.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.33.49image.png.webp?alt=media&token=be9635ed-5fee-49e0-aca1-2e077152d792"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Task for laptop repair added properly<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.36.06image.png.webp?alt=media&token=d69d3958-e813-4b73-afb5-94953397ba3f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Description of task missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.37.32image.png.webp?alt=media&token=00f5cd49-559d-4839-9dfc-556aafe1fd15"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Due date not in the correct format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>I have made sure to update lastActivity with the current datetime value using<br>following code: task['lastActivity'] = datetime.now(). Set the name, description, and due date. Due<br>date matches one of the formats mentioned in str_to_datetime() and a new task<br>is added to the tasks list.</div><div>Here I output a message confirming the new<br>task was added or if the addition was rejected due to missing data<br>based on the prior checks.</div><div>Try except block is used to help check if<br>the due date is in the right format only then append to the<br>list.</div><div>Lastly use the save() function.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.43.49process_update_code.png.webp?alt=media&token=0254d21d-6b9e-435f-9a72-0889047e8879"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code: Fetch name, description and due of the index task given. We show<br>the old data in TODOtask and input the new updated data which is<br>further passed to update_task.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>Here I try to fetch name, description and due of the index task<br>given and later show the old data in TODOtask and input the new<br>updated data which is further passed to update_task. The only thing to take<br>care here is index out of bound using if loop.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-08T23.47.35update_task_code.png.webp?alt=media&token=4f5edb96-5b47-41dc-9094-7838e4b5934d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code: Check if name, description or due have been updated for the index<br>task given. Update it in the original task.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.17.53image.png.webp?alt=media&token=820e6e20-1b64-4144-adf4-fd0f9392f465"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Updating repairing task with new name description and due date.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.21.11image.png.webp?alt=media&token=04179273-c273-42da-831c-36e2a7093ca6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Index value was out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>We first find the task by index and also consider index out of<br>bounds scenarios and include appropriate message(s) for invalid index. Update incoming task data<br>if it's provided (if it's not provided use the original task property value).<br>This is done using if-else loops. Also updated lastActivity with the current datetime<br>value using the following code: task['lastActivity'] = datetime.now(). Output that the task was<br>updated if any items were changed, otherwise mention task was not updated. Lastly<br>use the save() function.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.30.35done_code.png.webp?alt=media&token=4c934975-e2ae-4c8f-b81b-e0899450aa52"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code: Check if task_done in the template is False. If yes, then update<br>it with current datetime. Later if we try to mark the same task<br>it shows that it has already been completed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.32.58image.png.webp?alt=media&token=cc740fab-ae1e-4e91-b5d8-fc027e3681b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Marked task 4 as complete/done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.34.12image.png.webp?alt=media&token=d1342c9f-897b-4fea-86b1-4d3206724da8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Since task 2 was already completed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.35.19image.png.webp?alt=media&token=491228de-6000-4089-bfea-0e818875e96c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Index value out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>Check if task_done in the template is False. This is checked using if<br>condition. If yes, then update it with current datetime. Later if we try<br>to mark the same task it shows that it has already been completed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.42.27view_code.png.webp?alt=media&token=9bccb2e3-26d8-49f4-891d-22381044fffd"/></td></tr>
<tr><td> <em>Caption:</em> <p>If condition checks whether the index value is in range from 0 to<br>max length of list, it further prints the task name, desc and due<br>date. Else, prints an invalid statement.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.44.41image.png.webp?alt=media&token=a071b84f-c5a1-4119-a9da-de7ecc9614cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Shows task 3 details<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.50.01image.png.webp?alt=media&token=7b8e1305-eac0-45a6-b0f7-7ad38b6c84f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Index value out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.53.26image.png.webp?alt=media&token=53c3339d-551f-47dd-a8e4-5d8320b4588e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.54.14image.png.webp?alt=media&token=b6c70a4f-03fd-40c7-bbcd-c52a306d47d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task 2 shows completed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.55.14image.png.webp?alt=media&token=cc9b8b3d-14b9-4d88-80a1-54833c384acc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.57.01image.png.webp?alt=media&token=239243a2-daa4-4ce5-b36c-d7c8782c726b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task 5<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T00.58.39delete_code.png.webp?alt=media&token=a6fbe7ec-33b1-4977-8040-2c1efeaa4192"/></td></tr>
<tr><td> <em>Caption:</em> <p>If condition checks whether the index value is in range from 0 to<br>max length of list, it further deletes the task or else prints an<br>invalid statement.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T01.13.58image.png.webp?alt=media&token=24f7994a-50d6-4ae7-a175-21db39e76616"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Task 5 was deleted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T01.16.01image.png.webp?alt=media&token=27159ce7-83d1-4a99-9d2e-634a467c62e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: Index value out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>We try to show message if it was successful or not considering index<br>out of bounds scenarios and include appropriate message(s) for invalid index. Lastly, make<br>sure to use the save() function.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T01.33.25incomplete_code.png.webp?alt=media&token=1e96be7b-52d2-44e3-b248-46096f337dfe"/></td></tr>
<tr><td> <em>Caption:</em> <p>The below code checks if any task within tasks has task_done as &quot;False&quot;.<br>Prints all incomplete task.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T01.26.04image.png.webp?alt=media&token=26c9b78b-fc8c-4f20-b07c-26c3cdf245fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Gives a list of incomplete task.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T01.34.35image.png.webp?alt=media&token=316f6447-eb93-4762-b847-7cbcd66f5673"/></td></tr>
<tr><td> <em>Caption:</em> <p>No incomplete tasks to show.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>The above code checks if any task within tasks has task_done as &quot;False&quot;.<br>Prints all incomplete tasks. If no incomplete task pending it shows a message.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.03.41overdue_code.png.webp?alt=media&token=c6588322-161c-4bd5-9170-8d12b92e541b"/></td></tr>
<tr><td> <em>Caption:</em> <p>The below code checks if any task within tasks has task_done as &quot;False&quot;<br>and due date earlier than current date. Later print all overdue tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.02.39image.png.webp?alt=media&token=0a7a0110-8e29-430c-843d-fc845409367a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure: No overdue tasks to show<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.15.14image.png.webp?alt=media&token=af11bb07-c741-43d9-88f1-7d84214dab6b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success: Shows overdue task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>We try to generate a list of tasks where the due date is<br>older than "now" and that are not complete (i.e., not done). Later pass<br>that list into list_tasks().</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.16.32remaining_code1.png.webp?alt=media&token=ed391e8e-ed89-4fc6-8915-37ec76fd6810"/></td></tr>
<tr><td> <em>Caption:</em> <p>First half of the code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.17.41remaining_code2.png.webp?alt=media&token=6814b86f-01d2-4265-bca3-f1d5443170ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code continued<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.20.01image.png.webp?alt=media&token=8919a8cd-ae2c-4d48-aac0-fb8d04b6da18"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task already completed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.22.08image.png.webp?alt=media&token=46509607-cd46-47d1-b21a-cc6547e06a64"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index value out of bound.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.23.27image.png.webp?alt=media&token=111afdfd-cfbf-448b-8cf4-1d7096e13e43"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows remaining time from current time until due date.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.24.56image.png.webp?alt=media&token=227d3654-004e-46ac-996b-4405fc6a1946"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows overdue time of the task.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>First, we try to get the task by index considering index out of<br>bounds scenarios and include appropriate message(s) for invalid index using if-else loop. Get<br>the days, hours, minutes, seconds between the due date and current date.&nbsp; In<br>case, the due date is past already then print out how many days,<br>hours, minutes, seconds the task is overdue. Here divmod function helps calculate hours<br>and minutes from seconds. Remaining time is calculated by subtracting due date time<br>from current time or vice versa depending on whether the task is overdue<br>or pending.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.43.48image.png.webp?alt=media&token=0797d5ec-7e3e-43aa-9238-4239d0242fef"/></td></tr>
<tr><td> <em>Caption:</em> <p>Some running tasks from the terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.45.25image.png.webp?alt=media&token=32a64626-bc4d-4c09-a7da-fb93863f9df0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Another set of running tasks from terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-09T02.39.44image.png.webp?alt=media&token=588c3275-7ef8-41fc-8bd5-52a1ce58ba46"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows Json file with varying data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>Overall, the concept of switch case to try and perform various tasks was<br>clear to me. It helped me understand multiple conditions and try except blocks<br>to be used at the right place. I faced problems in outputting remaining<br>time for a task due in the form of days, hours, minutes and<br>seconds. Later found out a solution using divmode function. First, we need to<br>calculate everything in seconds. Later divide by 3600 to convert into hours. The<br>remaining seconds will definitely be less than 1hour so then we divide by<br>60 to convert into minutes. And finally, the remaining seconds are printed as<br>well.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/5">https://github.com/krishashah911/krs-is601-007/pull/5</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/krs" target="_blank">Grading</a></td></tr></table>