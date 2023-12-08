<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Krisha Shah (krs)</td></tr>
<tr><td> <em>Generated: </em> 12/7/2023 8:55:35 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/krs" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <p>The API data consists of Netflix titles (movies/series) and a bunch of details<br>regarding those titles. Now the user can add Ratings for each of these<br>titles. The benefit for the users is that they can recommend a movie<br>or series based on the good or bad ratings given. Also, when the<br>user adds a rating, he/she gets points for that rating. Thus, more and<br>more users are encouraged to rate the movies/series. A user can see all<br>the ratings given by himself/herself. Be able to edit or delete them.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <p>A single movie/series can have multiple ratings from multiple users. Thus, the relation<br>here is one to many. When a title/movie is updated, the user sees<br>the updated version automatically. If the movie is deleted, then the ratings belonging<br>to that movie are automatically removed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.41.58image.png.webp?alt=media&token=279a8285-0f6f-44cc-b614-95086f8365ba"/></td></tr>
<tr><td> <em>Caption:</em> <p>ratings given by user login<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.02.52image.png.webp?alt=media&token=a638770a-6d9a-419a-a0bd-829e25d9185a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Associating data to user - Code 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.03.58image.png.webp?alt=media&token=a6586a8c-0da1-4aa5-8397-882c1a27c422"/></td></tr>
<tr><td> <em>Caption:</em> <p>Associating data to user - Code 2<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.09.01image.png.webp?alt=media&token=6d3050fc-cb56-4f4e-b19c-3bdeec5b1aed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Main watchlist page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.10.35image.png.webp?alt=media&token=7c44e26a-ebe7-4e16-849a-4365efcf9d1b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limit 4 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.11.13image.png.webp?alt=media&token=ec9841e0-58a3-4107-902f-505945db08e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Limit above 100 not valid.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.17.33image.png.webp?alt=media&token=812aefbe-b0a1-4ef8-beea-59ba5614691c"/></td></tr>
<tr><td> <em>Caption:</em> <p>View ratings page based on title name. Here total count of ratings is<br>2 for the series Wednesday.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.20.00image.png.webp?alt=media&token=60d6fa93-d12e-4f0c-81cb-14a62ce98375"/></td></tr>
<tr><td> <em>Caption:</em> <p>User can delete one of the ratings given by themselves.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.46.40image.png.webp?alt=media&token=2c2925bc-153b-47ed-98ef-cc57208a0eab"/></td></tr>
<tr><td> <em>Caption:</em> <p>User can delete all the ratings by clicking on the delete all button<br>besides back button.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.47.41image.png.webp?alt=media&token=198611c5-d1ee-403b-b9f2-eca2b46e9942"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete all code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/32">https://github.com/krishashah911/krs-is601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.23.56image.png.webp?alt=media&token=e2ab0da5-3c90-41c8-bd84-742c94e7d4c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage ratings page is only an admin access page. Column to show Number<br>of ratings for each title. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.26.27image.png.webp?alt=media&token=61ceff69-0293-4ca9-8eeb-693deff614b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter and sorting based on title name descending order.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-05T23.28.02image.png.webp?alt=media&token=86bd72e7-49b5-407f-9953-8b8f7842b1a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter for limit 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/32">https://github.com/krishashah911/krs-is601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.50.29image.png.webp?alt=media&token=bde095ea-fbdc-43c0-82a1-625ad6bfcff1"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is admin related manage ratings page where the admin can see all<br>the ratings given by different users based on the title name.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.51.51image.png.webp?alt=media&token=3cc08c37-ac22-45da-a9db-e45d83aae4bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>When selecting all ratings for a particular title, admin is able to add,<br>edit or delete a rating for the specific user.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.53.22image.png.webp?alt=media&token=20b44a01-019a-4d95-bfe3-4a6de9a9afc0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin adds a rating for series title Wednesday on behalf of user &quot;john&quot;.<br>This reflects on user&#39;s view my ratings page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-08T01.54.37image.png.webp?alt=media&token=e09852bd-e95a-4ba7-bb27-d4d2c96b0809"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin edits the given rating for series title Wednesday on behalf of user<br>&quot;john&quot;. This reflects on user&#39;s view my ratings page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/32">https://github.com/krishashah911/krs-is601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-06T22.56.41image.png.webp?alt=media&token=2b21aaea-7fcf-43a0-b4cb-39e7ddfd7c67"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin page to show each title&#39;s ratings by different users.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fkrs%2F2023-12-06T22.58.41image.png.webp?alt=media&token=17c97cd2-a14c-4eb2-82c7-15f07b23e170"/></td></tr>
<tr><td> <em>Caption:</em> <p>Upon clicking username. User profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <p>For the first image, I am trying to show an admin all the<br>ratings that are given by various users based on the title of the<br>movie. They can then fetch the user details by clicking on the username<br>link as shown in second image. The admin has access permission to edit<br>or completely delete the rating. Thus, disassociating the rating from the user. The<br>edited rating gets reflected on the user&#39;s account as well. However, it does<br>not affect their overall points earned from that rating.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/krishashah911/krs-is601-007/pull/32">https://github.com/krishashah911/krs-is601-007/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learning:&nbsp; My code for Milestone3 demonstrates the integration of various web development concepts,<br>from building forms and handling database interactions to implementing user authentication and permissions.<br>I have had an active learning process and a willingness to address challenges<br>as they arise. Overall, I have understood how active user data can be<br>fetched and passed on to the next page for accessing data only related<br>to that particular user.&nbsp;<br><br>Pertaining to this learning, I faced difficulty fetching the ratings<br>in View My Ratings page that only pertain to a specific user. Somehow,<br>the user_id was not being fetched properly in the query:<br><div style="color: rgb(212, 212,<br>212); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; line-height: 19px; white-space:<br>pre;"><div>&nbsp; &nbsp; <span style="color: #9cdcfe;">query</span> = <span style="color: #ce9178;">&quot;&quot;&quot;</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp;<br>&nbsp; SELECT</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Ratings.id as &#39;id&#39;,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp;<br>&nbsp; &nbsp; IS601_Ratings.watchlist_id as &#39;watchlist_id&#39;,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Watchlist.title as &#39;title&#39;,</span></div><div>&lt;span<br>style=&quot;color: #ce9178;&quot;&gt;&nbsp; &nbsp; &nbsp; &nbsp; IS601_Ratings.ratings as &#39;ratings&#39;,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp;<br>IS601_Ratings.heading as &#39;heading&#39;,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Ratings.comments as &#39;comments&#39;,</span></div><div><span style="color: #ce9178;">&nbsp;<br>&nbsp; &nbsp; &nbsp; IS601_Ratings.created as created,</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Ratings.modified as<br>modified</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; FROM</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Ratings</span></div><div>&lt;span<br>style=&quot;color: #ce9178;&quot;&gt;&nbsp; &nbsp; &nbsp; &nbsp; LEFT JOIN</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; IS601_Watchlist<br>ON IS601_Ratings.watchlist_id = IS601_Watchlist.id</span></div><div><span style="color: #ce9178;">&nbsp; &nbsp; &nbsp; &nbsp; WHERE IS601_Ratings.user_id=</span><span style="color: #569cd6;">%s</span></div><div>&lt;span<br>style=&quot;color: #ce9178;&quot;&gt;&nbsp; &nbsp; &quot;&quot;&quot;</span></div></div><div><br></div><div>My solution/ a round about this problem was to directly<br>call the query here:<br><div style="color: rgb(212, 212, 212); background-color: rgb(30, 30, 30); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; line-height: 19px; white-space: pre;"><div><span style="color: #c586c0;">if</span> <span style="color: #569cd6;">not</span><br><span style="color: #9cdcfe;">has_error</span>:</div><div>&nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #c586c0;">try</span>:</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; <span style="color: #9cdcfe;">result</span> = <span style="color: #4ec9b0;">DB</span>.<span style="color: #dcdcaa;">selectAll</span>(<span style="color: #ce9178;">&quot;SELECT IS601_Ratings.id<br>as &#39;id&#39;, IS601_Ratings.watchlist_id as &#39;watchlist_id&#39;, </span></div><div><span style="color: #ce9178;">IS601_Watchlist.title as &#39;title&#39;, IS601_Ratings.ratings as &#39;ratings&#39;,<br>IS601_Ratings.heading as &#39;heading&#39;, </span></div><div><span style="color: #ce9178;">IS601_Ratings.comments as &#39;comments&#39;, IS601_Ratings.created as created, IS601_Ratings.modified as<br>modified </span></div><div><span style="color: #ce9178;">FROM IS601_Ratings LEFT JOIN IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id </span></div><div>&lt;span<br>style=&quot;color: #ce9178;&quot;&gt;WHERE IS601_Ratings.user_id=</span><span style="color: #569cd6;">%s</span><span style="color: #ce9178;">&quot;</span>, <span style="color: #9cdcfe;">user_id</span>)</div><div>&nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; <span style="color: #c586c0;">if</span> <span style="color: #9cdcfe;">result</span>.status:</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>&nbsp; &nbsp; <span style="color: #9cdcfe;">rows</span> = <span style="color: #9cdcfe;">result</span>.rows</div></div></div><div><br></div><div>I understand this was not<br>a complete solution but, it solved my issue to some extent.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/krs" target="_blank">Grading</a></td></tr></table>