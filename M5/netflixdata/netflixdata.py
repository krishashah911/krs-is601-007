from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from netflixdata.forms import NetflixdataForm, NetflixdataSearchForm , RatingsdataForm, EditRatingsdataForm # Import your NetflixdataForm class
from roles.permissions import admin_permission, users_permission
from flask_login import current_user

netflixdata = Blueprint('netflixdata', __name__, url_prefix='/netflixdata', template_folder='templates')
@netflixdata.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = NetflixdataSearchForm()
    if form.validate_on_submit():
        try:
            from utils.netflixdata import Unogs
            from utils.lazy import DictToObject
            # Create a new netflixdata record in the database
            results = Unogs.get_movie_info(form.title_type.data)
            for result in results:
                print(result)
                if result:
                    result = DictToObject(result)
                    result = DB.insertOne(
                        """INSERT INTO IS601_Watchlist (title, title_type, netflix_id, synopsis, `year`, imdb_id, title_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            title = VALUES(title),
                            title_type = VALUES(title_type),
                            netflix_id = VALUES(netflix_id),
                            synopsis = VALUES(synopsis),
                            `year` = VALUES(`year`),
                            imdb_id = VALUES(imdb_id),
                            title_date = VALUES(title_date)""",
                    result.title, result.title_type, result.netflix_id, result.synopsis, result.year, result.imdb_id, result.title_date
                    )
                    if result.status:
                        flash(f"Loaded netflix data", "success")
                        print("OKKK")
        except Exception as e:
            flash(f"Error loading netflix record: {e}", "danger")
            print("Not OK")
    return render_template("netflixdata_search.html", form=form)

## UCID: krs
## Date: 11/27/23
@netflixdata.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = NetflixdataForm()    
    if request.method == "POST" and form.validate_on_submit():
        try:
            # Create a new netflix record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Watchlist (title, title_type, netflix_id, synopsis, `year`, title_date) VALUES (%s, %s, %s, %s, %s, %s)",
                form.title.data, form.title_type.data, form.netflix_id.data, form.synopsis.data, form.year.data, form.title_date.data
            )
            if result.status:
                flash(f"Created netflix data record", "success")
        except Exception as e:
            flash(f"Error creating netflix record: {e}", "danger")
    else:
        if request.method == "POST":
            flash("Form has validation errors. Please check the fields.", "danger")

    return render_template("netflixdata_form.html", form=form, type="Create")

@netflixdata.route("/add_ratings", methods=["GET", "POST"])
def add_ratings():
    user_id = current_user.get_id()
    form = RatingsdataForm()    
    if request.method == "POST" and form.validate_on_submit():
        try:
            # Create a new rating in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Ratings (watchlist_id, ratings, heading, comments, user_id) VALUES (%s, %s, %s, %s, %s)",
                form.watchlist_id.data, form.ratings.data, form.heading.data, form.comments.data, user_id
            )
            if result.status:
                flash(f"Added a rating", "success")
        except Exception as e:
            flash(f"Error adding a rating: {e}", "danger")
    else:
        if request.method == "POST":
            flash("Form has validation errors. Please check the fields.", "danger")

    return render_template("add_ratings.html", form=form, type="Create")

@netflixdata.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = NetflixdataForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("netflixdata.list"))


    if request.method == "POST" and form.validate_on_submit() and id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_Watchlist SET title = %s, title_type = %s, netflix_id = %s, synopsis = %s, year = %s, title_date = %s WHERE id = %s",
                form.title.data, form.title_type.data, form.netflix_id.data, form.synopsis.data, form.year.data, form.title_date.data,id
            )
            if result.status:
                flash(f"Updated netflix data record", "success")
        except Exception as e:
            flash(f"Error updating netflix record: {e}", "danger")
    else:
        if request.method == "POST":
            flash("Form has validation errors. Please check the fields.", "danger")
    try:
        result = DB.selectOne(
            "SELECT title, title_type, netflix_id, synopsis, `year`, imdb_id, title_date FROM IS601_Watchlist WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = NetflixdataForm(data=result.row)
    except Exception as e:
        flash("Error fetching netflix record", "danger")
    return render_template("netflixdata_form.html", form=form, type="Edit")

@netflixdata.route("/edit_rating", methods=["GET", "POST"])
@users_permission.require(http_exception=403)
def edit_rating():
    form = RatingsdataForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("netflixdata.view_my_ratings"))


    if request.method == "POST" and form.validate_on_submit() and id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_Ratings SET watchlist_id = %s, ratings = %s, heading = %s, comments = %s WHERE id = %s",
                form.watchlist_id.data, form.ratings.data, form.heading.data, form.comments.data, id
            )
            if result.status:
                flash(f"Updated rating record", "success")
        except Exception as e:
            flash(f"Error updating rating record: {e}", "danger")
    else:
        if request.method == "POST":
            flash("Form has validation errors. Please check the fields.", "danger")
    try:
        result = DB.selectOne(
            "SELECT watchlist_id, ratings, heading, comments FROM IS601_Ratings WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = RatingsdataForm(data=result.row)
    except Exception as e:
        flash("Error fetching ratings", "danger")
    return render_template("edit_ratings.html", form=form, type="Edit")

@netflixdata.route("/admin_edit_rating", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def admin_edit_rating():
    form = EditRatingsdataForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("netflixdata.view_my_ratings"))

    if request.method == "POST" and form.validate_on_submit() and id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_Ratings SET user_id = %s, ratings = %s, heading = %s, comments = %s WHERE id = %s",
                form.user_id.data, form.ratings.data, form.heading.data, form.comments.data, id
            )
            if result.status:
                flash(f"Updated rating record", "success")
        except Exception as e:
            flash(f"Error updating rating record: {e}", "danger")
    else:
        if request.method == "POST":
            flash("Form has validation errors. Please check the fields.", "danger")
    try:
        result = DB.selectOne(
            "SELECT user_id, ratings, heading, comments FROM IS601_Ratings WHERE id = %s", id
        )
        if result.status and result.row:
            form = EditRatingsdataForm(data=result.row)
    except Exception as e:
        flash("Error fetching ratings", "danger")
    return render_template("edit_ratings.html", form=form, type="Edit")

@netflixdata.route("/list", methods=["GET"])
def list():
    rows = []
    has_error = False

    query = "SELECT id, title, title_type, netflix_id, synopsis, `year`, imdb_id, title_date FROM IS601_Watchlist WHERE 1=1"
    args = {}
    allowed_columns = ["id", "title", "title_type", "netflix_id", "year", "created", "modified"]
    title = request.args.get("title")
    column = request.args.get("column")  
    order = request.args.get("order")  
    limit = request.args.get("limit", 10) 

    if title:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{title}%"

    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True
    if not has_error:
        try:
            result = DB.selectAll(query,args)
            if result.status and result.rows:
                rows = result.rows
            else:
                flash("No record found.","info")
        except Exception as e:
            print(e)
            flash("Error getting netflix records", "danger")

    return render_template("netflixdata_list.html", rows=rows)

@netflixdata.route("/manage_ratings", methods=["GET"])
@admin_permission.require(http_exception=403)
def manage_ratings():
    title = ""
    rows = []
    has_error = False
    query = """
        SELECT
        IS601_Watchlist.id as 'watchlist_id',
        IS601_Watchlist.title as 'title',
        (SELECT COUNT(*) FROM IS601_Ratings WHERE IS601_Watchlist.id = IS601_Ratings.watchlist_id) as total_ratings,
        IS601_Watchlist.created as created,
        IS601_Watchlist.modified as modified
        FROM
        IS601_Watchlist
        WHERE 1=1
    """

    args = {}
    allowed_columns = ["watchlist_id","title", "created", "modified"]
    watchlist_id = request.args.get("watchlist_id")
    title = request.args.get("title")
    column = request.args.get("column")  
    order = request.args.get("order")  
    limit = request.args.get("limit", 10) 

    if watchlist_id:
        query += " AND IS601_Watchlist.id = %(watchlist_id)s"
        args["watchlist_id"] = watchlist_id

    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True
    if not has_error:
        try:
            result = DB.selectAll(query,args)
            if result.status and result.rows:
                rows = result.rows
            else:
                flash("No record found.","info")
        except Exception as e:
            print(e)
            flash("Error getting netflix ratings", "danger")

    return render_template("manage_ratings.html", rows=rows)

@netflixdata.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            # Delete the netflix data record from the database
            result = DB.delete("DELETE FROM IS601_Watchlist WHERE id = %s", id)
            if result.status:
                flash("Deleted netflix record", "success")
        except Exception as e:
            flash(f"Error deleting netflix record: {e}", "danger")
        del args["id"]
    else:
        flash("No ID present", "warning")
    return redirect(url_for("netflixdata.list", **args))

@netflixdata.route("/delete_rating", methods=["GET"])
@users_permission.require(http_exception=403)
def delete_rating():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            # Delete the rating from the database
            result = DB.delete("DELETE FROM IS601_Ratings WHERE id = %s", id)
            if result.status:
                flash("Deleted rating", "success")
        except Exception as e:
            flash(f"Error deleting rating: {e}", "danger")
        del args["id"]
    else:
        flash("No ID present", "warning")
    return redirect(url_for("netflixdata.view_my_ratings", **args))

@netflixdata.route("/view", methods=["GET"])
@users_permission.require(http_exception=403)
def view():
    rows = []
    title = ""
    has_error = False

    query = """
        SELECT
        IS601_Ratings.id as 'id',
        IS601_Ratings.watchlist_id as 'watchlist_id',
        IS601_Ratings.ratings as 'ratings',
        IS601_Ratings.heading as 'heading',
        IS601_Ratings.comments as 'comments',
        IS601_Watchlist.title as 'title',
        IS601_Ratings.created as created,
        IS601_Ratings.modified as modified
        FROM
        IS601_Ratings
        LEFT JOIN
        IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id
        WHERE IS601_Ratings.watchlist_id=1
    """

    args = {}
    allowed_columns = ["ratings", "heading", "comments", "created", "modified"]
    watchlist_id = request.args.get("watchlist_id")
    id = request.args.get("id")
    ratings = request.args.get("ratings")
    heading = request.args.get("heading")
    comments = request.args.get("comments")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit",10)
    


    if ratings:
        query += " AND IS601_Ratings.ratings = %(ratings)s"
        args["ratings"] = ratings


    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"


    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True

    if not has_error:
        try:
            result = DB.selectAll("SELECT IS601_Ratings.id as 'id', IS601_Ratings.watchlist_id as 'watchlist_id', IS601_Ratings.ratings as 'ratings', IS601_Ratings.heading as 'heading', IS601_Ratings.comments as 'comments', IS601_Watchlist.title as 'title', IS601_Ratings.created as created, IS601_Ratings.modified as modified FROM IS601_Ratings LEFT JOIN IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id WHERE IS601_Ratings.watchlist_id=%s", watchlist_id)
            if result.status:
                rows = result.rows
                # print(f"rows: {rows}")
            else:
                flash("Error retrieving rating. Please try again.", "error")
        except Exception as e:
            flash("An unexpected error occured. Please try again later.", "error")
        
    if watchlist_id:
        try:
            result = DB.selectOne("SELECT title FROM IS601_Watchlist WHERE id = %s", watchlist_id)
            if result.status:
                watchlist_id = result.row.get("id")
                title = result.row.get("title")
            else:
                flash("An error occurred while fetching title. Please try again later.", "error")
        except Exception as e:
            print(f"Title name fetch error {e}")
            flash("An error occurred while fetchingtitle name. Please try again later.", "danger")
    else:
        title = ""  

    return render_template("netflixdata_view.html", title=title, rows=rows, allowed_columns=allowed_columns)

@netflixdata.route("/view_by_title", methods=["GET"])
@admin_permission.require(http_exception=403)
def view_by_title():
    rows = []
    title = ""
    has_error = False

    query = """
        SELECT
        IS601_Ratings.id as 'id',
        IS601_Ratings.watchlist_id as 'watchlist_id',
        IS601_Ratings.user_id as 'user_id' ,
        IS601_Ratings.ratings as 'ratings',
        IS601_Ratings.heading as 'heading',
        IS601_Ratings.comments as 'comments',
        IS601_Watchlist.title as 'title',
        IS601_Ratings.created as created,
        IS601_Ratings.modified as modified
        FROM
        IS601_Ratings
        LEFT JOIN
        IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id
        WHERE 1=1
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["user_id", "ratings", "heading", "comments", "created", "modified"]
    
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    # UCID: krs
    # Date: 11/21/23
    id = request.args.get("id")
    watchlist_id = request.args.get("watchlist_id")
    ratings = request.args.get("ratings")
    heading = request.args.get("heading")
    comments = request.args.get("comments")
    user_id = request.args.get("user_id")
    column = request.args.get("column")  
    order = request.args.get("order")  
    limit = request.args.get("limit", 10) 
    
    if user_id:
        query += " AND IS601_Ratings.user_id = %(user_id)s"
        args["user_id"] = user_id
    if ratings:
        query += " AND IS601_Ratings.ratings = %(ratings)s"
        args["ratings"] = ratings

    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True
    
    print("query",query)
    print("args", args)

    if not has_error:
        try:
            result = DB.selectAll("SELECT IS601_Ratings.id as 'id', IS601_Ratings.watchlist_id as 'watchlist_id', IS601_Ratings.user_id as 'user_id' , IS601_Ratings.ratings as 'ratings', IS601_Ratings.heading as 'heading', IS601_Ratings.comments as 'comments', IS601_Watchlist.title as 'title', IS601_Ratings.created as created, IS601_Ratings.modified as modified FROM IS601_Ratings LEFT JOIN IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id WHERE IS601_Ratings.watchlist_id=%s", watchlist_id)
            if result.status:
                rows = result.rows
                # print(f"rows: {rows}")
            else:
                flash("Error retrieving records. Please try again.", "error")
        except Exception as e:
            flash("An unexpected error occured. Please try again later.", "error")

    if watchlist_id:
        try:
            result = DB.selectOne("SELECT title FROM IS601_Watchlist WHERE id = %s", watchlist_id)
            if result.status:
                watchlist_id = result.row.get("id")
                title = result.row.get("title")
            else:
                flash("An error occurred while fetching title. Please try again later.", "error")
        except Exception as e:
            print(f"Title name fetch error {e}")
            flash("An error occurred while fetching title name. Please try again later.", "danger")
    else:
        title = ""  

    return render_template("view_by_title.html", title=title, rows=rows, allowed_columns=allowed_columns)

@netflixdata.route("/view_my_ratings", methods=["GET"])
@users_permission.require(http_exception=403)
def view_my_ratings():
    user_id = current_user.get_id()
    rows = []
    title = ""
    has_error = False

    query = """
        SELECT
        IS601_Ratings.id as 'id',
        IS601_Ratings.watchlist_id as 'watchlist_id',
        IS601_Watchlist.title as 'title',
        IS601_Ratings.ratings as 'ratings',
        IS601_Ratings.heading as 'heading',
        IS601_Ratings.comments as 'comments',
        IS601_Ratings.created as created,
        IS601_Ratings.modified as modified
        FROM
        IS601_Ratings
        LEFT JOIN
        IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id
        WHERE IS601_Ratings.user_id=1
    """

    args = {}
    allowed_columns = ["id", "watchlist_id", "title", "ratings", "heading", "comments", "created", "modified"]
    watchlist_id = request.args.get("watchlist_id")
    id = request.args.get("id")
    ratings = request.args.get("ratings")
    heading = request.args.get("heading")
    comments = request.args.get("comments")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit",10)
    


    if ratings:
        query += " AND IS601_Ratings.ratings = %(ratings)s"
        args["ratings"] = ratings

    if watchlist_id:
        query += " AND IS601_Ratings.watchlist_id = %(watchlist_id)s"
        args["watchlist_id"] = watchlist_id

    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"


    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True

    if not has_error:
        try:
            result = DB.selectAll("SELECT IS601_Ratings.id as 'id', IS601_Ratings.watchlist_id as 'watchlist_id', IS601_Watchlist.title as 'title', IS601_Ratings.ratings as 'ratings', IS601_Ratings.heading as 'heading', IS601_Ratings.comments as 'comments', IS601_Ratings.created as created, IS601_Ratings.modified as modified FROM IS601_Ratings LEFT JOIN IS601_Watchlist ON IS601_Ratings.watchlist_id = IS601_Watchlist.id WHERE IS601_Ratings.user_id=%s", user_id)
            if result.status:
                rows = result.rows
                # print(f"rows: {rows}")
            else:
                flash("Error retrieving rating. Please try again.", "error")
        except Exception as e:
            flash("An unexpected error occured. Please try again later.", "error")
        
    if watchlist_id:
        try:
            result = DB.selectOne("SELECT title FROM IS601_Watchlist WHERE id = %s", watchlist_id)
            if result.status:
                watchlist_id = result.row.get("id")
                title = result.row.get("title")
            else:
                flash("An error occurred while fetching title. Please try again later.", "error")
        except Exception as e:
            print(f"Title name fetch error {e}")
            flash("An error occurred while fetchingtitle name. Please try again later.", "danger")
    else:
        title = ""  

    return render_template("view_my_ratings.html", title=title, rows=rows, allowed_columns=allowed_columns)  

@netflixdata.route("/user_profile", methods=["GET"])
def user_profile():
    user_id = request.args.get("user_id")
    rows = []
    has_error = False

    query = "SELECT id, email, username, points FROM IS601_Users WHERE id=%s",user_id
    args = {}
    allowed_columns = ["id", "email", "username", "points", "created", "modified"]

    if not has_error:
        try:
            result = DB.selectAll( "SELECT id, email, username, points FROM IS601_Users WHERE id=%s",user_id)
            print(result)
            if result.status and result.rows:
                rows = result.rows
            else:
                flash("No record found.","info")
        except Exception as e:
            print(e)
            flash("Error getting profile info", "danger")

    return render_template("netflixdata_profile.html", rows=rows, user_id=user_id, allowed_columns=allowed_columns)