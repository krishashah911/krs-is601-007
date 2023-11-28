<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 7:06:48 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p>I used uNoGS netflix movie and series data API.<br><a href="https://rapidapi.com/unogs/api/unogs/details">Unofficial Netflix API (Free<br>API Key) | uNoGS API Documentation (rapidapi.com)</a><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <p>Currently I am using API under GET&nbsp;/search/titles&nbsp;<div>Later on, for user related task in<br>Milestone2 I plan on using other API endpoints.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <p>{&#39;title&#39;: &#39;Get Gotti&#39;, &#39;img&#39;: &#39;<a href="https://occ-0-1373-2567.1.nflxso.net/dnm/api/v6/WNk1mr9x_Cd_2itp6pUM7-lXMJg/AAAABbm_wK2fYH2h2Fq43hPMuf2pC48epeG19MHhb0-TdqW7b2-Zr6Gnayvl4lfZ4WLostBEI5tpF9gjBGstvY6uMXX4Oj3gFFiLHWlrm1goI_J0UfgZIfZCSNhmNvaqmzFR64LMcaRWd4bgz8X0nK-918fKK3s4EdSO__u2AnzlM5gSzD42U4PpCRvr-qjaUkDZmUXoORE8ik46efY8efuaWPVU6GRjO7NQCNkxmINVkdfEyp6J0lm3kk0dXUFGxFPOYiQ0FGRbb6F8L9LJDoYp9S_KxIk0akoboKPs2kq1tmy2sD0KXh6duxc.jpg?r=1ab">https://occ-0-1373-2567.1.nflxso.net/dnm/api/v6/WNk1mr9x_Cd_2itp6pUM7-lXMJg/AAAABbm_wK2fYH2h2Fq43hPMuf2pC48epeG19MHhb0-TdqW7b2-Zr6Gnayvl4lfZ4WLostBEI5tpF9gjBGstvY6uMXX4Oj3gFFiLHWlrm1goI_J0UfgZIfZCSNhmNvaqmzFR64LMcaRWd4bgz8X0nK-918fKK3s4EdSO__u2AnzlM5gSzD42U4PpCRvr-qjaUkDZmUXoORE8ik46efY8efuaWPVU6GRjO7NQCNkxmINVkdfEyp6J0lm3kk0dXUFGxFPOYiQ0FGRbb6F8L9LJDoYp9S_KxIk0akoboKPs2kq1tmy2sD0KXh6duxc.jpg?r=1ab</a>&#39;, &#39;title_type&#39;: &#39;series&#39;, &#39;netflix_id&#39;: 81628150, &#39;synopsis&#39;: &#39;Told from both<br>sides of the law, this docuseries from the makers of &quot;Fear City&quot; follows<br>the FBI&amp;#39;s battle to bring down infamous mob boss John Gotti.&#39;, &#39;rating&#39;: &#39;&#39;,<br>&#39;year&#39;: &#39;2023&#39;, &#39;runtime&#39;: &#39;0&#39;, &#39;imdb_id&#39;: &#39;&#39;, &#39;poster&#39;: &#39;&#39;, &#39;top250&#39;: 0, &#39;top250tv&#39;: 0, &#39;title_date&#39;:<br>&#39;2023-10-24&#39;}<br><br>From the above fetched API data sample, I am using (title, title_type, netflix_id,<br>synopsis, rating, year, imdb_id, title_date)<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>A Netflix data list page consists of all the different type of movie<br>and series available from the API using the above columns to explain each<br>one of them. Later a user can view each Netflix content to see<br>their ratings. Now these ratings are user generated and shown for each title<br>id. Other functions like edit, delete and fetch can be done only by<br>the admin.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.14.10image.png.webp?alt=media&token=4e2ffc6b-6f52-4f26-80d1-35a4ed986877"/></td></tr>
<tr><td> <em>Caption:</em> <p>create form with valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.15.20image.png.webp?alt=media&token=fb1675a0-e197-4f17-b972-698f1973456f"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message for invalid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.16.33image.png.webp?alt=media&token=fd81a9fb-9a11-47ec-8254-bb34b3cdcb4f"/></td></tr>
<tr><td> <em>Caption:</em> <p>success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.19.09image.png.webp?alt=media&token=bfad8a78-3a10-4c7a-a208-c4781c88060f"/></td></tr>
<tr><td> <em>Caption:</em> <p>python code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.19.54image.png.webp?alt=media&token=2e68da44-3270-415d-accc-da5041e95399"/></td></tr>
<tr><td> <em>Caption:</em> <p>html code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.21.48image.png.webp?alt=media&token=f49164e4-7cc2-4991-afe5-1382c2060878"/></td></tr>
<tr><td> <em>Caption:</em> <p>database with new data created.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.23.56image.png.webp?alt=media&token=4ee130fa-cd6c-492f-81c1-2ba623eb8797"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record with imdb_id as None are custom records and rest are API generated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.25.29image.png.webp?alt=media&token=acccb2dc-f2a8-4945-a50e-a94158f9ac30"/></td></tr>
<tr><td> <em>Caption:</em> <p>search by title name &#39;pol&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.27.33image.png.webp?alt=media&token=20658644-abbb-4c6d-b825-e327a44ae88b"/></td></tr>
<tr><td> <em>Caption:</em> <p>limit 1-100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.28.28image.png.webp?alt=media&token=e0bad213-84f5-407c-a058-5a7985bd0ade"/></td></tr>
<tr><td> <em>Caption:</em> <p>no records for this filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.30.12image.png.webp?alt=media&token=44861873-f7f4-4a20-996c-49bf9ed8a20b"/></td></tr>
<tr><td> <em>Caption:</em> <p>view ratings for each movie/series title id<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.32.35image.png.webp?alt=media&token=ece84525-115c-4f70-900b-254e4151b54f"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page by id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.34.43image.png.webp?alt=media&token=32b6259b-7e07-4192-888d-f65469c41aaa"/></td></tr>
<tr><td> <em>Caption:</em> <p>data invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.35.54image.png.webp?alt=media&token=ded1fcdb-605f-452f-a85c-04d6924b2282"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.38.00image.png.webp?alt=media&token=4c17ab73-b27c-4a82-8fe5-5b7c6bc28c9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>after<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.38.52image.png.webp?alt=media&token=036a718b-cace-4756-b0dc-903831196d12"/></td></tr>
<tr><td> <em>Caption:</em> <p>before<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.43.33image.png.webp?alt=media&token=ddf1193e-b455-4521-b9f2-77a45322eb04"/></td></tr>
<tr><td> <em>Caption:</em> <p>before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.44.26image.png.webp?alt=media&token=d4222064-25be-4149-b7c6-64ce149f1090"/></td></tr>
<tr><td> <em>Caption:</em> <p>after delete - with filters<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.42.07image.png.webp?alt=media&token=698df9d6-748c-4372-a7e0-2fb516ff5cdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion - Id-11 Adventure by Accident<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.45.22image.png.webp?alt=media&token=499ea8df-8ba7-4e29-978c-b202f37e4c3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deletion - Id-11 not available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.48.14image.png.webp?alt=media&token=67192c42-8e49-4d83-bf40-8a8636c623ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>api.py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.50.14image.png.webp?alt=media&token=172a0669-3863-497f-b707-0db78f2df52d"/></td></tr>
<tr><td> <em>Caption:</em> <p>netflixdata.py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-27T23.51.36image.png.webp?alt=media&token=97b15e35-55bf-4d20-aa89-a47a1e8d444d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to fetch data from webpage using Admin access only.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <p>The data loading process starts when the user triggers the operation through a<br>web interface, a form named NetflixdataSearchForm class. The admin picks the data type<br>(movie or series) they want to fetch by interacting with the form, leading<br>to the invocation of the fetch function in the Flask application upon form<br>submission. Inside this function, the Unogs.get_movie_info method is called, making an API request<br>to Unogs to get information about the chosen movie or series type. The<br>API response, which includes a list of results, is then handled in a<br>loop. Each result goes through a transformation where keys are renamed, and spaces<br>are swapped with underscores. Afterward, the altered data is added to the MySQL<br>database using an INSERT statement, incorporating the ON DUPLICATE KEY UPDATE clause to<br>manage potential duplicates. This streamlined process ensures the dynamic retrieval, transformation, and storage<br>of movie or series data in the database, all based on user preferences.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/26">https://github.com/krishashah911/krs-is601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learnings: I looked through WTForms documentations online to understand the process. Apart from<br>that, CSS modifications were done using layout.html template and bootstrap.&nbsp;<div>Apart from that learning<br>how to make API requests, handle responses, and incorporate external data into your<br>application is a valuable skill.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-krs-prod-0ebfd8f27fae.herokuapp.com/login">https://is601-krs-prod-0ebfd8f27fae.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-28T00.02.24image.png.webp?alt=media&token=5842d72a-3423-452e-a222-79b6e3e4c4b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dashboard<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-28T00.03.08image.png.webp?alt=media&token=300d164d-5b97-44e0-a9b8-8d4f74a87bc0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Project - krs-is601-007<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-28T00.04.04image.png.webp?alt=media&token=9d47e8ad-c04e-4278-955a-a0490611c985"/></td></tr>
<tr><td> <em>Caption:</em> <p>Milestone2 files in M5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-11-28T00.05.55image.png.webp?alt=media&token=ed05bd75-f614-492b-ace9-228118b6fcb4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Milestone2 files in M5<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/krs" target="_blank">Grading</a></td></tr></table>