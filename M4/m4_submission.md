<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 10/12/2023 7:14:11 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.15.20image.png.webp?alt=media&token=997ba1fe-cef2-4706-8c29-4013e10e8dcd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Created a class called Calc. Addition function takes two variable input and stores<br>the answer in self.ans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.29.09image.png.webp?alt=media&token=3561a0a8-696b-4f4f-b570-668cd50195bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Additional screenshot of run function with user input conditions.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.34.28image.png.webp?alt=media&token=3fa76fea-4269-471e-af29-46f6e38210e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Additional screenshot of run function with user input conditions.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.19.02image.png.webp?alt=media&token=9037eff1-c2e0-40d3-9587-d46dccff44a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Created a class called Calc. Subtraction function takes two variable input and stores<br>the answer in self.ans<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.19.30image.png.webp?alt=media&token=1a0ecd09-a20c-4159-929c-45426386007f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Created a class called Calc. Multiplication function takes two variable input and stores<br>the answer in self.ans<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-11T19.23.42image.png.webp?alt=media&token=98ce89b1-9340-4d21-85cd-1c1705ce3b1f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Created a class called Calc. Division function takes two variable input and stores<br>the answer in self.ans<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.40.46image.png.webp?alt=media&token=5cf6ef97-ba3c-4fa1-8571-a0741ac6349b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for add function and negate add function.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.42.26image.png.webp?alt=media&token=e91180a7-7635-4e3e-8413-c6aadad6a62f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.44.36image.png.webp?alt=media&token=7c39bec4-82e3-46e6-9f32-43ae42125c8a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for ans-add-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.45.37test_case_passed.png.webp?alt=media&token=0b273ad6-87bb-487d-a1d2-e905441c2fec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.48.01image.png.webp?alt=media&token=33f48577-5b2e-4d0b-824f-086a97ed269d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for subtract function and negate sub <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.48.43test_case_passed.png.webp?alt=media&token=9807b6fe-f5e0-4aa7-b17c-1cadbf4cd663"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.52.02image.png.webp?alt=media&token=8ad33095-2dd3-4942-be6a-d2578372d1b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for ans-sub-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.52.19test_case_passed.png.webp?alt=media&token=6866d7f2-eced-4bd7-9ce9-fa055facf445"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.55.05image.png.webp?alt=media&token=af19f069-a665-4702-aec2-41d835625614"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for number-mult-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.55.52test_case_passed.png.webp?alt=media&token=d372a131-ace7-4762-a67d-fdbbd5d237bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.57.40image.png.webp?alt=media&token=3ffd662f-cebc-4269-86d8-3ee00a10e902"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for ans-mult-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T22.57.48test_case_passed.png.webp?alt=media&token=af9da305-672a-47b1-9d87-bc1871a91f94"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T23.00.18image.png.webp?alt=media&token=c7955dd9-71bd-4045-98f6-1d39813f7e8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for number-div-number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T23.01.44test_case_passed.png.webp?alt=media&token=c207af87-aff9-45c8-87b7-67aa7afc20c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T23.04.55image.png.webp?alt=media&token=84de7646-e078-43f9-b12f-e23a18a17bb1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for ans-div-number using fixtures<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-10-12T23.05.05test_case_passed.png.webp?alt=media&token=d31a032e-1767-4877-a724-03cf1418fc7f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>There are multiple ways how one can define the previous answer variable. I<br>used a method where I define the previous value within the arguments of<br>the function and later call the class Calc. Fixtures also help to do<br>the same.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>Normally test cases work well with simple addition subtraction etc. Negating the test<br>case is also a good practice to make sure the answer does not<br>equal to something we don&#39;t want it to be. Using fixtures helped me<br>define previous answers in an easier manner and calling it directly in the<br>answer-div-number function.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/7">https://github.com/krishashah911/krs-is601-007/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/krs" target="_blank">Grading</a></td></tr></table>