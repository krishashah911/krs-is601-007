<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 11/22/2023 1:18:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.36.48image.png.webp?alt=media&token=87d7d2d0-c52d-46c1-9f9c-c44cc9c66d33"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index.html page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.37.42image.png.webp?alt=media&token=dfdc7b15-e96b-4cb9-aafe-6b823e2a49c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index.html code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.38.55image.png.webp?alt=media&token=7d19a905-1b74-406a-b8d3-29c85972251f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navbar on index.html page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.39.57image.png.webp?alt=media&token=9d6fd04e-f811-4a23-9028-d67da5fda856"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization dropdown nav code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.40.56image.png.webp?alt=media&token=538f3849-b512-49c1-a3ac-d8cc9584f18c"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations dropdown nav code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T16.58.28image.png.webp?alt=media&token=6b94b76a-20c7-4b8a-ae09-981304e420d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>importcsv-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T16.59.39image.png.webp?alt=media&token=94a8db96-efe4-4f25-be1c-2adb11435611"/></td></tr>
<tr><td> <em>Caption:</em> <p>importcsv-2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.00.35image.png.webp?alt=media&token=06d74abb-2be4-401d-848a-b87242ab846b"/></td></tr>
<tr><td> <em>Caption:</em> <p>importcsv-4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.01.30image.png.webp?alt=media&token=abbfe2b5-3e5f-4549-acef-d5533a35fbc2"/></td></tr>
<tr><td> <em>Caption:</em> <p>importcsv-5,6,7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.02.38image.png.webp?alt=media&token=1e78a8a3-35d4-4491-8633-1a7a99258c5b"/></td></tr>
<tr><td> <em>Caption:</em> <p>importcsv-8<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.43.30image.png.webp?alt=media&token=fe12a479-b578-4a2d-ac21-6b168fddefe0"/></td></tr>
<tr><td> <em>Caption:</em> <p>donation create view 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.44.30image.png.webp?alt=media&token=917533d5-3f64-440b-8640-374213872d23"/></td></tr>
<tr><td> <em>Caption:</em> <p>donation edit view 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.46.27image.png.webp?alt=media&token=4341afba-34dc-466c-8d16-b1a4cccd299c"/></td></tr>
<tr><td> <em>Caption:</em> <p>donation create view 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.47.09image.png.webp?alt=media&token=aceb75ae-0654-4da8-8a36-147959d3e336"/></td></tr>
<tr><td> <em>Caption:</em> <p>donation edit view 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.51.36image.png.webp?alt=media&token=eb11ae9f-0426-46c4-9321-6bc2b55804d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>create edit view code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T00.53.02image.png.webp?alt=media&token=ab944fd7-735c-456c-bd96-df4f7984c18f"/></td></tr>
<tr><td> <em>Caption:</em> <p>create edit view code continued<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.07.44image.png.webp?alt=media&token=7b7fea47-ea28-40a3-ad75-2b954cf6f452"/></td></tr>
<tr><td> <em>Caption:</em> <p>donation search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.09.41image.png.webp?alt=media&token=6071e78d-64e2-48f3-b3a9-71409311c8a3"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.28.14image.png.webp?alt=media&token=f5c3cc94-4be6-44cb-ac69-f45911dd288b"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.29.24image.png.webp?alt=media&token=42b31c6d-6cb8-4d24-a21e-23886c0e3028"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code continued 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.31.12image.png.webp?alt=media&token=c73f237d-16d5-42b9-abf7-965ea968837b"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code continued 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.32.11image.png.webp?alt=media&token=37ea3868-e5f1-4bca-bc66-4efe6620f332"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code continued 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.44.05image.png.webp?alt=media&token=6d1db6d5-026c-4555-a9d0-42623630b87d"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.44.52image.png.webp?alt=media&token=b0394140-e5cc-4197-90aa-66aa2303cbc2"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 2,3,4,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.45.51image.png.webp?alt=media&token=52f974a9-d122-489d-aa8d-1c253d98442d"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 6,7,8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.46.51image.png.webp?alt=media&token=62a29cbc-270f-4e88-ab05-12c809a22aa3"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.48.18image.png.webp?alt=media&token=7676e5f5-2c63-4b48-ad57-01c013a6aebe"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 11,12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.50.30image.png.webp?alt=media&token=55282b30-3114-46c1-9547-db0906008cd7"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.52.30image.png.webp?alt=media&token=34d470ed-e63d-4cc3-950f-eab82175d284"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 4,4a,5,6,7,8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.54.01image.png.webp?alt=media&token=8e82bd2e-b80a-494b-8a2b-f66071bacb01"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.55.36image.png.webp?alt=media&token=45b6e38f-40c5-4260-8ca6-228309b4364a"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 11,7<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.58.44image.png.webp?alt=media&token=e6d10041-c012-45c6-be92-7fb246fbdade"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T06.59.47image.png.webp?alt=media&token=1def0ea0-819b-4d6b-b8ba-be0b4e64d495"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 4,5,5a,6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T07.00.46image.png.webp?alt=media&token=c1c38a53-3721-4e79-a40c-a26e3dacd2d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 7,8,9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T07.02.30image.png.webp?alt=media&token=05ae1f26-3db4-42f2-9c38-772449db545c"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 11,12<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T07.03.40image.png.webp?alt=media&token=fce79a95-a7f6-4089-b206-6664fa9151c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 13,14,15<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T07.05.24image.png.webp?alt=media&token=bf0f5571-fbd4-4b30-afe6-55344b1fdafa"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3,4,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T07.08.00image.png.webp?alt=media&token=3af2215f-eaee-4d04-a57b-76235cd166cf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful delete from website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.05.21image.png.webp?alt=media&token=d24ac3e7-1af0-41b9-82e0-70b90567331a"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization create view 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.07.02image.png.webp?alt=media&token=7c74c927-54e3-449d-9ed7-98176e31205a"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization create view 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.08.38image.png.webp?alt=media&token=7c6f00f7-f8bf-4fd4-bea4-c08a4cc7a98e"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization edit view 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.09.09image.png.webp?alt=media&token=9b223e00-cce8-4885-92e0-e36b5df7d2b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization edit view 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.10.40image.png.webp?alt=media&token=e82f41e5-cd3f-4aca-9e52-a439ca85f1d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.11.13image.png.webp?alt=media&token=785142c0-04ca-4a62-b15d-facfdf936ad0"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.12.00image.png.webp?alt=media&token=e1ed33e0-f593-4356-a7cd-94eb3dc64e29"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.15.59image.png.webp?alt=media&token=e87cbc36-1b65-40c9-8a64-8c8300ad0542"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter-state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.17.48image.png.webp?alt=media&token=d1c2690a-0a9c-470d-9864-1ebf911826cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.18.52image.png.webp?alt=media&token=e9cda389-d18d-473e-9101-9170d43872b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code continued<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.20.39image.png.webp?alt=media&token=69c4c996-006a-44c1-85f4-db397380ef6b"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code continued<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.25.31image.png.webp?alt=media&token=2280ee9b-f51c-48a6-9c7b-993009524e71"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.26.07image.png.webp?alt=media&token=ac02dbec-cf36-4d2a-a6d4-d4304d6c7c1c"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 2,3,4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.26.51image.png.webp?alt=media&token=a0f4717f-74d5-4c46-bbab-ca4642076a9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 5,6,7,8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.28.30image.png.webp?alt=media&token=4e0e70d1-263a-427a-8a6c-e8827f4dbadb"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.29.53image.png.webp?alt=media&token=5e33940e-b7de-4031-9f8c-796bc3661b74"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.30.43image.png.webp?alt=media&token=fbef115b-5ba2-43c8-a20e-f6f92b38adc5"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 4,5,5a,6,6a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.32.25image.png.webp?alt=media&token=98ba208d-d664-4324-9d63-a1f462a86849"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 7,8,9,10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.33.10image.png.webp?alt=media&token=551450e2-29e1-45e1-9173-434004110306"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 11<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.34.12image.png.webp?alt=media&token=254b3897-694e-49aa-b078-8f2fdc76a2e0"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.35.00image.png.webp?alt=media&token=121bae2a-e0c5-4c06-ac3f-0ca367134c32"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 4,5,6,6a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.36.10image.png.webp?alt=media&token=2ccf3d34-ba83-4628-9eb0-9dbbce6aaebe"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 7,7a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.36.55image.png.webp?alt=media&token=edd1f4c6-8a42-4215-a62c-73686d60e5bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 8,9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.37.30image.png.webp?alt=media&token=781e428d-07e8-4552-a710-7ae6a0cac18f"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.38.01image.png.webp?alt=media&token=e51ffe31-3766-4265-8f8e-277fe097bc3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 11,12,13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.38.58image.png.webp?alt=media&token=2856971f-57a9-43b4-b29d-ad1ff1f5b158"/></td></tr>
<tr><td> <em>Caption:</em> <p>TODO 1,2,3,4,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.40.43image.png.webp?alt=media&token=6523c99b-5637-47a2-9907-268e0ad31feb"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful delete from website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.48.42image.png.webp?alt=media&token=93df8fa3-416a-43d5-bd39-ac2579f7df94"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases pass <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.51.27image.png.webp?alt=media&token=db0023b1-d557-482e-ae2e-7b8b3fdb1dd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases pass <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.53.29image.png.webp?alt=media&token=68169830-0327-448b-9407-dcdc5ae2be17"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T17.55.12image.png.webp?alt=media&token=6f625f2f-442a-44a5-aaa5-a1c406c04be4"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases pass<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>All test cases passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/23">https://github.com/krishashah911/krs-is601-007/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T18.07.01image.png.webp?alt=media&token=655bc1c6-09b5-4e4a-8fee-67e0c6d9151d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commit history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T18.14.19image.png.webp?alt=media&token=c5f90599-2f75-4e2e-bad1-cd02d7b79c9b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dashboard<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T18.15.15image.png.webp?alt=media&token=c504c2b9-512f-406a-a4f8-ea9e91a0a745"/></td></tr>
<tr><td> <em>Caption:</em> <p>Projects: krs-is601-007<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-22T18.17.26image.png.webp?alt=media&token=2e7e603e-83fd-474c-b17f-ae824ab8e433"/></td></tr>
<tr><td> <em>Caption:</em> <p>Projects: krs-is601-007<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-krs-td-3250a06ea368.herokuapp.com/">https://is601-007-krs-td-3250a06ea368.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/krs" target="_blank">Grading</a></td></tr></table>