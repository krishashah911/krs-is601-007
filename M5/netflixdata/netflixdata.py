from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from netflixdata.forms import NetflixdataForm, NetflixdataSearchForm  # Import your NetflixdataForm class
from roles.permissions import admin_permission

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
            result = Unogs.get_movie_info(form.title_type.data)
            if result and result.get("status") == "success":
                # result = DictToObject(result)
                # result.change_percent = result.change_percent.replace("%","")
                result = DB.insertOne(
                    """INSERT INTO IS601_Watchlist (title, title_type, netflix_id, synopsis, rating, `year`, imdb_id, title_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        title = VALUES(title),
                        title_type = VALUES(title_type),
                        netflix_id = VALUES(netflix_id),
                        synopsis = VALUES(synopsis),
                        rating = VALUES(rating),
                        `year` = VALUES(`year`),
                        imdb_id = VALUES(imdb_id),
                        title_date = VALUES(title_date)""",
                result.title, result.title_type, result.netflix_id, result.synopsis, result.rating, result.year, result.imdb_id, result.title_date
                )
                if result.status:
                    flash(f"Loaded netflix data", "success")
        except Exception as e:
            flash(f"Error loading netflix record: {e}", "danger")
    return render_template("netflixdata_search.html", form=form)

@netflixdata.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = NetflixdataForm()
    if form.validate_on_submit():
        try:
            # Create a new netflix record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Watchlist (title, title_type, netflix_id, synopsis, rating, `year`, imdb_id, title_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                form.title, form.title_type, form.netflix_id, form.synopsis, form.rating, form.year, form.imdb_id, form.title_date
            )
            if result.status:
                flash(f"Created netflix data record", "success")
        except Exception as e:
            flash(f"Error creating netflix record: {e}", "danger")
    return render_template("netflixdata_form.html", form=form, type="Create")

@netflixdata.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = NetflixdataForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("netflixdata.list"))
    if form.validate_on_submit() and id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_Watchlist SET title = %s, title_type = %s, netflix_id = %s, synopsis = %s, rating = %s, year = %s, imdb_id = %s, title_date = %s WHERE id = %s",
                form.title, form.title_type, form.netflix_id, form.synopsis, form.rating, form.year, form.imdb_id, form.title_date
            )
            if result.status:
                flash(f"Updated netflix data record", "success")
        except Exception as e:
            flash(f"Error updating netflix record: {e}", "danger")
    try:
        result = DB.selectOne(
            "SELECT title, title_type, netflix_id, synopsis, rating, `year`, imdb_id, title_date FROM IS601_Watchlist WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = NetflixdataForm(data=result.row)
    except Exception as e:
        flash("Error fetching netflix record", "danger")
    return render_template("netflixdata_form.html", form=form, type="Edit")

@netflixdata.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, title, title_type, netflix_id, synopsis, rating, `year`, imdb_id, title_date FROM IS601_Watchlist LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting netflix records", "danger")
    return render_template("netflixdata_list.html", rows=rows)

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

@netflixdata.route("/view", methods=["GET"])
def view():
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("netflixdata.list"))
    try:
        result = DB.selectOne(
            "SELECT title, title_type, netflix_id, synopsis, rating, `year`, imdb_id, title_date FROM IS601_Watchlist WHERE id = %s",
            id
        )
        if result.status and result.row:
            return render_template("netflixdata_view.html", netflixdata=result.row)
        else:
            flash("Netflix record not found", "danger")
    except Exception as e:
        print(f"Netflix data error {e}")
        flash("Error fetching netflix record", "danger")
    return redirect(url_for("netflixdata.list"))