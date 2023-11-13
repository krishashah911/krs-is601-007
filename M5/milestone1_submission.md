<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 11/13/2023 1:33:37 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T00.54.29image.png.webp?alt=media&token=cc7de142-2eae-46ff-a1be-b55e20fcef15"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Email Verification<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T00.55.59image.png.webp?alt=media&token=6160304c-d179-4d1d-85c1-52f1d408174f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T00.57.10image.png.webp?alt=media&token=d9cb686e-3f2e-4c02-859e-037fa3b909b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords don&#39;t match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.16.29image.png.webp?alt=media&token=280a9999-7729-41ac-adba-d03ef6914c21"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid registration<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.11.42image.png.webp?alt=media&token=df8acd07-207e-40bc-bfd1-eb92f4dc4c2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email already registered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.13.41image.png.webp?alt=media&token=9785d440-bb5f-4635-a4f7-5b3fa5f02d5b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username already taken<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.15.13image.png.webp?alt=media&token=4e346dc8-e5f6-410f-a2cb-3c4a9450f0bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Row 3 is the new user from Task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/16">https://github.com/krishashah911/krs-is601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The webpage process user-submitted data via HTML forms, validating it on both the<br>frontend and backend, and respond with appropriate feedback messages. The frontend validation offers<br>real-time feedback to users, while backend validation ensures data integrity and security, including<br>password hashing. Passwords here are securely stored through hashing and salting, preventing plaintext<br>storage, and Flask extensions like Flask-Bcrypt or Flask-Login are used for password management.<br>We use SQL database to store user information, enabling registration, login, and user<br>management through secure database interactions.</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T01.17.25image.png.webp?alt=media&token=6fb2810f-79fc-4cb1-880c-e6686a9bd0b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password incorrect<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T01.18.15image.png.webp?alt=media&token=c4924db6-d76d-4bd4-89a7-d9eb47fbb3c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>User does not exist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T01.22.34image.png.webp?alt=media&token=733419ea-94ea-4585-9a13-957130c39eb9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/16">https://github.com/krishashah911/krs-is601-007/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The same as registration. Login webpage processes user-submitted data via HTML forms, validating<br>it on both the frontend and backend, and respond with appropriate feedback messages.<br>Email ID and passwords here are matched with the ones stored in the<br>database. If it matches, then that particular session login takes place.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T01.26.27image.png.webp?alt=media&token=07ae2754-1292-4dd5-a4ad-fde2837c256f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful logout<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T01.30.15image.png.webp?alt=media&token=fd12d994-a22a-4cd9-b6ce-73b021416daf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied to particular user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/17">https://github.com/krishashah911/krs-is601-007/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In the login page, the session logic is used to handle user authentication<br>and maintain login states. It checks for email and password of the user<br>in the database with the user credentials verified on the html page, and<br>upon a successful login, a secure session is initiated, storing user-specific data. A<br>session variable [&#39;logged_in&#39;] = True, signifies that the user&#39;s logged-in status is checked.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.27.57image.png.webp?alt=media&token=abff86f2-11be-4828-b130-2650965d6003"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page not found. Redirected to login/register<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.26.20image.png.webp?alt=media&token=40702523-c0af-48b8-85e7-5b2037d4e0db"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.29.49image.png.webp?alt=media&token=2387beef-f06e-4fb2-977f-29215bd85bbd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with Admin and Manager roles<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.32.59image.png.webp?alt=media&token=99c4f14b-642b-460d-9d4e-c11dacd0e49a"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Id 1 is admin user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/17">https://github.com/krishashah911/krs-is601-007/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>We need to handle user authentication, manage user sessions, and control the routing<br>to ensure that only authorized users can access certain pages. To do this,<br>we use Flask extensions like Flask-WTF for handling forms and Flask-Login for managing<br>user sessions. So, imagine you&#39;re the student logging in. When you try to<br>access a protected page, the application checks if you&#39;re logged in and have<br>the necessary permissions. If you are, it lets you in; otherwise, you&#39;ll be<br>redirected to the login page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>In our Flask application, we&#39;ve got some special pages that only certain people,<br>like the admin, can access. It&#39;s kind of like having a secret room<br>in a clubhouse. To make sure only the right people get in, we<br>use Flask extensions like Flask-WTF for handling forms and Flask-Login for keeping track<br>of who&#39;s who.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.42.00image.png.webp?alt=media&token=4cedf784-eac4-4f2d-829b-5ceda3aaab18"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navbar is styled for mobile users as well.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.42.52image.png.webp?alt=media&token=688255c4-a18d-4cdf-b6a9-63d0c3087590"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clean Table output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T03.43.46image.png.webp?alt=media&token=bc006b26-9406-46b2-acb6-e9dc748d7d83"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clean form style<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/18">https://github.com/krishashah911/krs-is601-007/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Majorly used bootstrap for all the CSS styling. For dropdown navbar we have<br>used class &quot;nav-link dropdown-toggle&quot; and for color we used &quot;navbar navbar-expand-lg bg-light&quot;. Similarly<br>for forms we use &quot;form-group mb-3&quot; which provides spacing of 3tabs. Some header<br>and footer styles are explicitly coded in layout.html file.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T08.50.41image.png.webp?alt=media&token=d3acf9fa-0c2c-41cb-b0c2-2289cd9fbf39"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords don&#39;t match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T08.54.06image.png.webp?alt=media&token=c0e5145b-51c7-4a9c-b1c7-7dd6ce540ab4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T08.58.16image.png.webp?alt=media&token=2ac84d20-978b-4516-80c6-91e12f9c05da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password not as per requirement.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/18">https://github.com/krishashah911/krs-is601-007/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>We use Flask&#39;s flash method to display temporary messages that persist for one<br>request/response cycle, such as success or error messages. These messages should be simple<br>for a layman to understand and non-technical.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T08.59.48image.png.webp?alt=media&token=cd30c14c-f408-4c1c-b344-c66866dbf19b"/></td></tr>
<tr><td> <em>Caption:</em> <p>User&#39;s profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/19">https://github.com/krishashah911/krs-is601-007/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>In the auth.py file code, a ProfileForm (WTForms) is used to edit user<br>profile information. The form&#39;s submission and validity are checked. If valid, it processes<br>email, username, and optionally, a secure password change. The user&#39;s current password is<br>verified before making changes. Successful changes trigger updates in the database, followed by<br>flashed success messages. The form also retrieves the user&#39;s profile data from the<br>database and displays it for editing, and the profile page uses the &quot;profile.html&quot;<br>template to render the form with pre-filled user data.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T09.05.24image.png.webp?alt=media&token=00ec77cd-ad12-4330-bace-8f54ea85131c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username validated and changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T09.06.16image.png.webp?alt=media&token=c1a82c2a-76b8-4297-9929-622e584279a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Id validated and changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T09.32.32image.png.webp?alt=media&token=d1e15093-eca7-483f-ba42-0406909f77af"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T09.52.40image.png.webp?alt=media&token=328b0e5e-5432-478b-944b-64dead1a85b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password does not match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T09.57.14image.png.webp?alt=media&token=4e6ef026-4746-4735-8807-dbb5873d7567"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email id already used.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T10.08.42image.png.webp?alt=media&token=b55f83dd-0574-4dce-b38c-80528a733d2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>row 3 user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-11T10.15.09image.png.webp?alt=media&token=490f0e3d-fa18-4c23-99f8-3d1d773c54dd"/></td></tr>
<tr><td> <em>Caption:</em> <p>row 3 user modified<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/19">https://github.com/krishashah911/krs-is601-007/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>In the web application, updating email, username, and password involves users interacting with<br>a form. The submitted data is examined on the server, ensuring email and<br>username uniqueness and verifying the current password&#39;s accuracy. If a password change is<br>requested, it is securely processed using hashing and salting techniques. After successful validation,<br>the user&#39;s data is updated in the database, and informative feedback messages are<br>displayed. The profile page is subsequently refreshed, enabling users to easily modify their<br>profile details while emphasizing data integrity and security.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I was facing issue with registering a new user. The problem lied in<br>the auth/register.html file. I had to add a render field for username so<br>that the username is fetched and stored in the database. While this issue<br>persists, I was not getting any error messages neither did the code break.<br>So, it was difficult to detect the issue. But eventually I realized that<br>I had to add the following line of code:&nbsp;{{render_field(form.username)}}<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-krs-prod-0ebfd8f27fae.herokuapp.com/login">https://is601-krs-prod-0ebfd8f27fae.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/krs" target="_blank">Grading</a></td></tr></table>